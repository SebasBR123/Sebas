# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:47:05 2024

@author: joaquin.asto
"""

#Importamos librerias
import pandas as pd #Manejo de input y output
from pyomo.environ import * #Modelamiento de optimización
from amplpy import modules #Solvers

Data = "Data_joaquin.xlsx"
#Inputs
df_barras=pd.read_excel(Data, sheet_name="Barras")
df_lineas=pd.read_excel(Data, sheet_name="Lineas")
df_GT=pd.read_excel(Data, sheet_name="G. Termico")
#df_GT = df_GT.map(lambda x: None if pd.isna(x) else x)
df_demanda=pd.read_excel(Data, sheet_name="Demanda")
df_MttLinea=pd.read_excel(Data, sheet_name="Mantt. Lineas")
df_Indisp_Term=pd.read_excel(Data, sheet_name="Indisp. Termicas")
df_Grupos_CC = pd.read_excel(Data, sheet_name="GruposCC")
df_Transi_CC = pd.read_excel(Data, sheet_name="TransCC")

# ==============================================================================
#                         Sets y Parámetros
# ==============================================================================

# Parametros de Calculo y simulación

Sbase=100

#Sets
Bi = df_barras["ID"].to_list() #Set de barras
GT = df_GT["ID"].to_list() #Set de generadores
L = df_lineas["ID"].to_list() #Set de lineas
CC = df_Grupos_CC["ID"].to_list()
Modos_CC = pd.unique(df_Grupos_CC.iloc[:, 2:].values.flatten()[~pd.isnull(df_Grupos_CC.iloc[:, 2:].values.flatten())]).tolist()

Grupos_CC = {}

for index, row in df_Grupos_CC.iterrows():
    key = row.iloc[0]
    values = row.iloc[2:].dropna().tolist()
    Grupos_CC[key] = values
    
Transiciones_CC = {}

for index, row in df_Transi_CC.iterrows():
    key = row.iloc[0]
    values = row.iloc[1:].dropna().tolist()
    Transiciones_CC[key] = values


#Horizonte de simulación

T=[]
for i in range(24):
    T.append("t"+str(i+1))

#Parametros de barras

Dem = {}
Referencia = {}
for i in Bi:
    #filtramos en df_demanda la barra y seleccionamos solo el T que queremos, luego convertimos a lista
    aux_dt = {}
    for t in T:
        aux_dt[t] = df_demanda.loc[df_demanda["ID"] == i, t].values[0]/Sbase

    Dem[i] = aux_dt

    Referencia[i] = df_barras.loc[df_barras["ID"] == i, "Referencia"].values[0]

#Parametros de las térmicas

Pmax = {} #Potencia Maxima
Pmin = {} #Potencia Minima
Bg = {} #Barra de Generación
arr_ini = {} #Arranque inicial térmicas
Pcomb = {} #Costo Combustible
Consumo1 = {} #Consumo tramo1
Potencia1 = {} #Potencia tramo1
Consumo2 = {} #Consumo tramo2
Potencia2 = {} #Potencia tramo2
C_arr_term = {} #Costo de arranque térmicas
coeff1 = {}
coeff2 = {}
indisp_term = {}
arranques_max_t = {}
paradas_max_t = {}


for gt in GT:
    Pmax[gt] = df_GT.loc[df_GT["ID"] == gt, "Pmax"].values[0] / Sbase
    Pmin[gt] = df_GT.loc[df_GT["ID"] == gt, "Pmin"].values[0] / Sbase
    Bg[gt] = df_GT.loc[df_GT["ID"] == gt, "Barra"].values[0]
    arr_ini[gt] = df_GT.loc[df_GT["ID"] == gt, "u_0"].values[0]
    Pcomb[gt] = df_GT.loc[df_GT["ID"] == gt, "Pcomb_soles"].values[0]
    C_arr_term[gt] = df_GT.loc[df_GT["ID"] ==gt, "Carranque"].values[0]
    Consumo1[gt] = df_GT.loc[df_GT["ID"] == gt, "Consumo_1"].values[0]
    Consumo2[gt] = df_GT.loc[df_GT["ID"] == gt, "Consumo_2"].values[0]
    Potencia1[gt] = df_GT.loc[df_GT["ID"] == gt, "Potencia_1"].values[0]
    Potencia2[gt] = df_GT.loc[df_GT["ID"] == gt, "Potencia_2"].values[0]
    coeff1[gt] = Consumo1[gt]*Pcomb[gt]
    coeff2[gt] = (Consumo2[gt]-Consumo1[gt])/Potencia2[gt]*Pcomb[gt]
    arranques_max_t[gt] = df_GT.loc[df_GT["ID"] == gt, "ArranquesMax"].values[0]
    paradas_max_t[gt] = df_GT.loc[df_GT["ID"] == gt, "ParadasMax"].values[0]
    
    aux_indt = {}
    for t in T:
        aux_indt[t] = df_Indisp_Term.loc[df_GT["ID"]==gt,t].values[0]
    indisp_term[gt] = aux_indt
    

#Parametros de lineas

BL_from = {} #Barra de Inicio
BL_to = {} #Barra de Llegada
x = {} # Reactancia en pu
R = {} #Resistencia en pu
gl = {} #conductancia de la linea en pu
bl = {} #suceptancia de la linea en pu
FlMAX = {} #Flujo maximo
Mant_Linea = {} #Mantenimiento de la linea horaria

for l in L:
    BL_from[l] = df_lineas.loc[df_lineas["ID"] == l, "Desde"].values[0]
    BL_to[l] = df_lineas.loc[df_lineas["ID"] == l, "Hasta"].values[0]
    x[l] = df_lineas.loc[df_lineas["ID"] == l, "X"].values[0]
    R[l] = df_lineas.loc[df_lineas["ID"] == l, "R"].values[0]
    gl[l] = R[l] / (R[l] ** 2 + x[l] ** 2)
    bl[l] = -x[l] / (R[l] ** 2 + x[l] ** 2)
    FlMAX[l] = df_lineas.loc[df_lineas["ID"] == l, "Pmax"].values[0] / Sbase

    aux_ml={}
    for t in T:
        aux_ml[t] = df_MttLinea.loc[df_MttLinea["ID"] == l, t].values[0]
    Mant_Linea[l] = aux_ml
    

#%%
# ==============================================================================
#                       MODELADO DE OPTIMIZACIÓN
# ==============================================================================
#       Variables
# ==============================================================================
model = ConcreteModel()


#model.dual = Suffix(direction=Suffix.IMPORT)
model.theta = Var(Bi,T, domain=Reals)
model.Ptg = Var(GT,T, domain=NonNegativeReals)
model.F = Var(L,T, domain=Reals)
model.r = Var(Bi,T, domain=NonNegativeReals)
model.Loss = Var(L,T, domain=NonNegativeReals)
#Estado de la unidad térmica
model.u = Var(GT,T, domain=Binary)
#Arranque de la unidad térmica
model.y = Var(GT,T, domain=Binary)
#Parada de la unidad térmica
model.w = Var(GT,T, domain=Binary)
# # Transición a un modo superior
# model.wtr = Var(G,T, domain=Binary)
# # Transición a un modo inferior
# model.ytr = Var(G,T, domain=Binary)

# def sum_transi_y(model,g,t):
#     if g in Transiciones_CC:
#         return sum(model.y[g_sup, t] for g_sup in Transiciones_CC[g])
#     else:
#         return 0
    
# def sum_transi_w(model,g,t):
#     if g in Transiciones_CC:
#         return sum(model.w[g_sup, t] for g_sup in Transiciones_CC[g])
#     else:
#         return 0

# ==============================================================================
#       Función Objetivo
# ==============================================================================
#model.obj = Objective(expr=sum(coeff1[g]*model.u[g,t]+coeff2[g]*model.Ptg[g,t] for g in G for t in T) + sum((model.y[g,t]-model.wtr[g,t]-model.ytr[g,t])*C_arr_term[g] for g in G for t in T) + sum(model.r[i,t] * 1000000 for i in Bi for t in T))
model.obj = Objective(expr=sum(coeff1[gt]*model.u[gt,t]+coeff2[gt]*model.Ptg[gt,t] for gt in GT for t in T) + sum((model.y[gt,t])*C_arr_term[gt] for gt in GT for t in T) + sum(model.r[i,t] * 100000 for i in Bi for t in T))
# ==============================================================================
#       Restricciones
# ==============================================================================
model.Balance_Pot = ConstraintList()
for t in T:
    for i in Bi:
        model.Balance_Pot.add(expr=sum(-model.F[l,t] - model.Loss[l,t] / 2 for l in L if BL_from[l] == i)
                                     + sum(model.F[l,t] - model.Loss[l,t] / 2 for l in L if BL_to[l] == i)
                                     + sum(model.Ptg[gt,t] for gt in GT if Bg[gt] == i)
                                     + model.r[i,t] - Dem[i][t] == 0)

model.Flujo_DC = ConstraintList()
for t in T:
    for l in L:
        model.Flujo_DC.add(expr=model.F[l,t] + bl[l] * (model.theta[BL_from[l],t] - model.theta[BL_to[l],t])*(1-Mant_Linea[l][t]) == 0)

model.Gen_t_max = ConstraintList()
for t in T:
    for gt in GT:
        model.Gen_t_max.add(expr=model.Ptg[gt,t] <= Pmax[gt]*model.u[gt,t]*(1-indisp_term[gt][t]/100))
        
model.Gen_t_min = ConstraintList()
for t in T:
    for gt in GT:
        model.Gen_t_min.add(expr=model.Ptg[gt,t] >= Pmin[gt]*model.u[gt,t])

model.flujoMAX1 = ConstraintList()
for t in T:
    for l in L:
        model.flujoMAX1.add(expr=model.F[l,t] <= FlMAX[l])

model.flujoMAX2 = ConstraintList()
for t in T:
    for l in L:
        model.flujoMAX2.add(expr=model.F[l,t] >= -FlMAX[l])

model.Perdidas = ConstraintList()
for t in T:
    for l in L:
        model.Perdidas.add(expr=model.Loss[l,t] - gl[l] * (model.theta[BL_from[l],t] - model.theta[BL_to[l],t]) ** 2 == 0)

model.ref = ConstraintList()
for t in T:
    for i in Bi:
        if Referencia[i] == 1:
            model.ref.add(model.theta[i,t] == 0)

model.unitcomitment = ConstraintList()
for t in T:
    t_num = int(t[1:])
    if t_num > 1:
        t_prev = 't'+str(t_num-1)
        for gt in GT:
            model.unitcomitment.add(expr=model.u[gt,t] - model.u[gt,t_prev] == model.y[gt,t] - model.w[gt,t])
    else:
        for gt in GT:
            model.unitcomitment.add(expr = model.u[gt,t] - arr_ini[gt] == model.y[gt,t] - model.w[gt,t])

model.unitcomitment_2 = ConstraintList()
for t in T:
    for gt in GT:
        model.unitcomitment_2.add(expr=model.y[gt,t] + model.w[gt,t] <= 1)

#===================================================
# Transicion de un modo inferior hacia modo superior
# model.transi_inf_sup_1 = ConstraintList()
# for t in T:
#     for g in Modos_CC:
#         model.transi_inf_sup_1.add(expr=model.w[g,t] + sum_transi_y(model,g,t) <= model.wtr[g,t] + 1)

# model.transi_inf_sup_2 = ConstraintList()
# for t in T:
#     for g in Modos_CC:
#         model.transi_inf_sup_2.add(expr=model.w[g,t] >= model.wtr[g,t])
        
# model.transi_inf_sup_3 = ConstraintList()
# for t in T:
#     for g in Modos_CC:
#         model.transi_inf_sup_3.add(expr=sum_transi_y(model,g,t) >= model.wtr[g,t])

#===================================================
# Transicion de un modo superior hacia modo inferior
# model.transi_sup_inf_1 = ConstraintList()
# for t in T:
#     for g in Modos_CC:
#         model.transi_sup_inf_1.add(expr=model.y[g,t] + sum_transi_w(model,g,t) <= model.ytr[g,t] + 1)

# model.transi_sup_inf_2 = ConstraintList()
# for t in T:
#     for g in Modos_CC:
#         model.transi_sup_inf_2.add(expr=model.y[g,t] >= model.ytr[g,t])
        
# model.transi_sup_inf_3 = ConstraintList()
# for t in T:
#     for g in Modos_CC:
#         model.transi_sup_inf_3.add(expr=sum_transi_w(model,g,t) >= model.ytr[g,t])
#===================================================

# model.excluyentes_CC = ConstraintList()
# for t in T:
#     for cc in CC:
#         model.excluyentes_CC.add(expr = sum(model.u[g,t] for g in Grupos_CC[cc]) <= 1)
#===================================================

# model.wtr_zero = ConstraintList()
# for t in T:
#     for g in G:
#         if g not in Modos_CC:
#             model.wtr_zero.add(expr = model.wtr[g,t] == 0)
              
# model.ytr_zero = ConstraintList()
# for t in T:
#     for g in G:
#         if g not in Modos_CC:
#             model.ytr_zero.add(expr = model.ytr[g,t] == 0)
#===================================================

model.arranque_max_term = ConstraintList()
for gt in GT:
    model.arranque_max_term.add(expr = sum(model.y[gt,t] for t in T) <= arranques_max_t[gt])

model.paradas_max_term = ConstraintList()
for gt in GT:
    model.paradas_max_term.add(expr = sum(model.w[gt,t] for t in T) <= paradas_max_t[gt])


#model.pprint()
# ==============================================================================
#                                RESULTADOS
# ==============================================================================
optimizer=SolverFactory("couenne", executable=modules.find("couenne"))
#optimizer=SolverFactory("ipopt")
results = optimizer.solve(model, tee=True)


print("El estado del Programa es:")
termination = results.solver.termination_condition
print("\nEl programa finalizó debido a que encontró un resultado: ", termination)
print("\nEstado del programa: ", results.solver.status)

objValue = model.obj.expr()

# ==============================================================================
#                                Resultados
# ==============================================================================

#Exportación de Resultados
Res_dem=pd.DataFrame(columns=["Tiempo"]+Bi)
Res_gen=pd.DataFrame(columns=["Tiempo"]+GT)
Res_u = pd.DataFrame(columns=["Tiempo"]+GT)
Res_y = pd.DataFrame(columns=["Tiempo"]+GT)
Res_w = pd.DataFrame(columns=["Tiempo"]+GT)
Res_theta = pd.DataFrame(columns=["Tiempo"]+Bi)
Res_flujo = pd.DataFrame(columns=["Tiempo"]+L)
Res_racionamiento = pd.DataFrame(columns=["Tiempo"]+Bi)

Res_gen["Tiempo"] = T
Res_dem["Tiempo"] = T
Res_u["Tiempo"] = T
Res_y["Tiempo"] = T
Res_w["Tiempo"] = T
Res_theta["Tiempo"] = T
Res_flujo["Tiempo"] = T
Res_racionamiento["Tiempo"] = T

for gt in GT:
    aux=[]
    for t in T:
       aux.append(model.Ptg[gt,t].value*100)
    Res_gen[gt]=aux

for i in Bi:
    aux=[]
    for t in T:
        aux.append(Dem[i][t]*100)
    Res_dem[i]=aux

Res_dem["Total"] = Res_dem[Bi].sum(axis=1)

for gt in GT:
    aux=[]
    for t in T:
       aux.append(model.u[gt,t].value)
    Res_u[gt]=aux
    
for gt in GT:
    aux=[]
    for t in T:
       aux.append(model.y[gt,t].value)
    Res_y[gt]=aux
    
for gt in GT:
    aux=[]
    for t in T:
       aux.append(model.w[gt,t].value)
    Res_w[gt]=aux
    
for i in Bi:
    aux=[]
    for t in T:
        aux.append(model.theta[i,t].value)
    Res_theta[i] = aux
    
for l in L:
    aux=[]
    for t in T:
        aux.append(model.F[l,t].value*100)
    Res_flujo[l] = aux

for i in Bi:
    aux=[]
    for t in T:
        aux.append(model.r[i,t].value)
    Res_racionamiento[i]=aux

Res_racionamiento["Total"] = Res_racionamiento[Bi].sum(axis=1)
    
print(f'\nCosto Total: {model.obj()}')

# ==============================================================================
#                                Dibujamos Resultados
# ==============================================================================

# import plotly.graph_objects as go
# # import plotly.io as pio

# # pio.renderers.default='browser'

# # Crear un objeto de figura
# fig = go.Figure()

# # Iterar sobre las columnas de producción y añadir barras al gráfico
# for columna in Res_gen.columns[1:]:
#     fig.add_trace(go.Bar(x=Res_gen['Tiempo'], y=Res_gen[columna], name=columna))

# # Actualizar el diseño del gráfico a barras apiladas
# fig.update_layout(barmode='stack', title='Producción apilada a lo largo del tiempo',
#                   xaxis_title='Tiempo', yaxis_title='Producción')
# fig.add_trace(go.Scatter(x=Res_dem["Tiempo"], y=Res_dem["Total"], name="Demanda Total"))
# # Mostrar el gráfico
# fig.show()