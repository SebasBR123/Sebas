#Importamos librerias
import pandas as pd #Manejo de input y output
from pyomo.environ import * #Modelamiento de optimización
from amplpy import modules #Solvers


#Inputs
df_barras=pd.read_excel("Data.xlsx", sheet_name="Barras")
df_lineas=pd.read_excel("Data.xlsx", sheet_name="Lineas")
df_GT=pd.read_excel("Data.xlsx", sheet_name="G. Termico")
df_demanda=pd.read_excel("Data.xlsx", sheet_name="Demanda")
df_MttLinea=pd.read_excel("Data.xlsx", sheet_name="Mantt. Lineas")





# ==============================================================================
#                         Sets y Parámetros
# ==============================================================================

# Parametros de Calculo y simulación

Sbase=100


#Sets
Bi = df_barras["ID"].to_list() #Set de barras
G = df_GT["ID"].to_list() #Set de generadores
L = df_lineas["ID"].to_list() #Set de lineas

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

#Parametros de generadores
CI = {} #Costo incremental
Pmax = {} #Potencia Maxima
Pmin = {} #Potencia Minima
Bg = {} #Barra de Generación
for g in G:
    CI[g] = df_GT.loc[df_GT["ID"] == g, "CI"].values[0]
    Pmax[g] = df_GT.loc[df_GT["ID"] == g, "Pmax"].values[0] / Sbase
    Pmin[g] = df_GT.loc[df_GT["ID"] == g, "Pmin"].values[0] / Sbase
    Bg[g] = df_GT.loc[df_GT["ID"] == g, "Barra"].values[0]


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
# ==============================================================================
#                       MODELADO DE OPTIMIZACIÓN
# ==============================================================================
#       Variables
# ==============================================================================
model = ConcreteModel()


#model.dual = Suffix(direction=Suffix.IMPORT)
model.theta = Var(Bi,T, domain=Reals)
model.Pg = Var(G,T, domain=NonNegativeReals)
model.F = Var(L,T, domain=Reals)
model.r = Var(Bi,T, domain=NonNegativeReals)
model.Loss = Var(L,T, domain=NonNegativeReals)

# ==============================================================================
#       Función Objetivo
# ==============================================================================

model.obj = Objective(expr=sum(model.Pg[g,t]*CI[g] for g in G for t in T) + sum(model.r[i,t] * 10000 for i in Bi for t in T))

# ==============================================================================
#       Restricciones
# ==============================================================================
model.Balance_Pot = ConstraintList()
for t in T:
    for i in Bi:
        model.Balance_Pot.add(expr=sum(-model.F[l,t] - model.Loss[l,t] / 2 for l in L if BL_from[l] == i)
                                     + sum(model.F[l,t] - model.Loss[l,t] / 2 for l in L if BL_to[l] == i)
                                     + sum(model.Pg[g,t] for g in G if Bg[g] == i)
                                     + model.r[i,t] - Dem[i][t] == 0)

model.Flujo_DC = ConstraintList()
for t in T:
    for l in L:
        model.Flujo_DC.add(expr=model.F[l,t] + bl[l] * (model.theta[BL_from[l],t] - model.theta[BL_to[l],t])*(1-Mant_Linea[l][t]) == 0)

model.Gen = ConstraintList()
for t in T:
    for g in G:
        model.Gen.add(expr=model.Pg[g,t] <= Pmax[g])

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


# model.pprint()
# ==============================================================================
#                                RESULTADOS
# ==============================================================================
optimizer=SolverFactory("ipopt", executable=modules.find("ipopt"))
results = optimizer.solve(model, tee=True)


print("El estado del Programa es:")
termination = results.solver.termination_condition
print("\nEl programa finalizó debido a que encontró un resultado: ", termination)
print("\nEstado del programa: ", results.solver.status)

objValue = model.obj.expr()

# ==============================================================================
#                                Dibujamos Resultados
# ==============================================================================

#Exportación de Resultados
Res_dem=pd.DataFrame(columns=["Tiempo"]+Bi)
Res_gen=pd.DataFrame(columns=["Tiempo"]+G)

Res_gen["Tiempo"] = T
Res_dem["Tiempo"] = T

for g in G:
    aux=[]
    for t in T:
       aux.append(model.Pg[g,t].value*100)
    Res_gen[g]=aux

for i in Bi:
    aux=[]
    for t in T:
        aux.append(Dem[i][t]*100)
    Res_dem[i]=aux

Res_dem["Total"] = Res_dem[Bi].sum(axis=1)
#print(Res_dem)
import plotly.graph_objects as go

# Crear un objeto de figura
fig = go.Figure()

# Iterar sobre las columnas de producción y añadir barras al gráfico
for columna in Res_gen.columns[1:]:
    fig.add_trace(go.Bar(x=Res_gen['Tiempo'], y=Res_gen[columna], name=columna))


# Actualizar el diseño del gráfico a barras apiladas
fig.update_layout(barmode='stack', title='Producción apilada a lo largo del tiempo',
                  xaxis_title='Tiempo', yaxis_title='Producción')
fig.add_trace(go.Scatter(x=Res_dem["Tiempo"], y=Res_dem["Total"], name="Demanda Total"))
# Mostrar el gráfico
fig.show()