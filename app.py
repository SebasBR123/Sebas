import pandas as pd
import plotly.graph_objects as go


#Recolección de Data


i=2023
año=str(i)
año1=str(i-2000)

mes={"Enero":"01","Febrero":"02","Marzo":"03","Abril":"04","Mayo":"05","Junio":"06","Julio":"07","Agosto":"08","Setiembre":"09","Octubre":"10","Noviembre":"11","Diciembre":"12"}
mesM={"Enero":"ENERO","Febrero":"FEBRERO","Marzo":"MARZO","Abril":"ABRIL","Mayo":"MAYO","Junio":"JUNIO","Julio":"JULIO","Agosto":"AGOSTO","Setiembre":"SETIEMBRE","Octubre":"OCTUBRE","Noviembre":"NOVIEMBRE","Diciembre":"DICIEMBRE"}

lista_clientes=[]
data_clientes=[]

for m in ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Setiembre","Octubre","Noviembre","Diciembre"]: 
    lista_clientes.append( pd.read_excel("CELEPSA\2023_" +mes[m]+".xlsx", sheet_name = "REPORTE"))
    data_clientes.append( pd.read_excel("CELEPSA\2023_" +mes[m]+".xlsx", sheet_name = "DATOS"))

data_cliente1=[]
for i in range(12):
    df=data_clientes[i]
    
    df1=df.drop([0])
    df1["fecha"]=pd.to_datetime(df1.iloc[:, 0],format="%d/%m/%Y %H:%M")
    df1.set_index('fecha', inplace=True)
    df1=df1.drop(["Unnamed: 0"], axis=1)
    data_cliente1.append(df1)
    
#Codigo concatenado
Entrega_Men=[]
Retiro_Men=[]
for i in range(12):
    Entrega=pd.DataFrame(data_cliente1[i][data_cliente1[i].columns[0]])
    Retiro=pd.DataFrame(data_cliente1[i][data_cliente1[i].columns.drop(data_cliente1[i].columns[0])])
    Retiro_Total=pd.DataFrame(Retiro.sum(axis=1))
    Entrega.rename(columns = {Entrega.columns.to_list()[0] : "Energía" }, inplace =True)
    Retiro_Total.rename(columns = {Retiro_Total.columns.to_list()[0] : "Energía" }, inplace =True)
    
    Entrega_Men.append(Entrega)
    Retiro_Men.append(Retiro_Total)
    

import pandas as pd

i=2023
año=str(i)
año1=str(i-2000)

mes={"Enero":"01","Febrero":"02","Marzo":"03","Abril":"04","Mayo":"05","Junio":"06","Julio":"07","Agosto":"08","Setiembre":"09","Octubre":"10","Noviembre":"11","Diciembre":"12"}
mesM={"Enero":"ENERO","Febrero":"FEBRERO","Marzo":"MARZO","Abril":"ABRIL","Mayo":"MAYO","Junio":"JUNIO","Julio":"JULIO","Agosto":"AGOSTO","Setiembre":"SETIEMBRE","Octubre":"OCTUBRE","Noviembre":"NOVIEMBRE","Diciembre":"DICIEMBRE"}

lista_clientes=[]
data_clientes=[]

for m in ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Setiembre","Octubre","Noviembre","Diciembre"]: 
    lista_clientes.append( pd.read_excel("CERE\2023_" +mes[m]+".xlsx", sheet_name = "REPORTE"))
    data_clientes.append( pd.read_excel("CERE\2023_" +mes[m]+".xlsx", sheet_name = "DATOS"))

data_cliente1=[]
for i in range(12):
    df=data_clientes[i]
    
    df1=df.drop([0])
    df1["fecha"]=pd.to_datetime(df1.iloc[:, 0],format="%d/%m/%Y %H:%M")
    df1.set_index('fecha', inplace=True)
    df1=df1.drop(["Unnamed: 0"], axis=1)
    data_cliente1.append(df1)

#Codigo concatenado
Entrega_Men_CERE=[]
Retiro_Men_CERE=[]

for i in range(12):
    Entrega=pd.DataFrame(data_cliente1[i][data_cliente1[i].columns[0]])
    Retiro=pd.DataFrame(data_cliente1[i][data_cliente1[i].columns.drop(data_cliente1[i].columns[0])])
    Retiro_Total=pd.DataFrame(Retiro.sum(axis=1))
    Entrega.rename(columns = {Entrega.columns.to_list()[0] : "Energía" }, inplace =True)
    Retiro_Total.rename(columns = {Retiro_Total.columns.to_list()[0] : "Energía" }, inplace =True)
    
    Entrega_Men_CERE.append(Entrega)
    Retiro_Men_CERE.append(Retiro_Total)
    

i=2023
año=str(i)
año1=str(i-2000)

mes={"Enero":"01","Febrero":"02","Marzo":"03","Abril":"04","Mayo":"05","Junio":"06","Julio":"07","Agosto":"08","Setiembre":"09","Octubre":"10","Noviembre":"11","Diciembre":"12"}
mesM={"Enero":"ENERO","Febrero":"FEBRERO","Marzo":"MARZO","Abril":"ABRIL","Mayo":"MAYO","Junio":"JUNIO","Julio":"JULIO","Agosto":"AGOSTO","Setiembre":"SETIEMBRE","Octubre":"OCTUBRE","Noviembre":"NOVIEMBRE","Diciembre":"DICIEMBRE"}

lista_clientes=[]
data_clientes=[]

for m in ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Setiembre","Octubre","Noviembre","Diciembre"]: 
    lista_clientes.append( pd.read_excel("TCH\2023_" +mes[m]+".xlsx", sheet_name = "REPORTE"))
    data_clientes.append( pd.read_excel("TCH\2023_" +mes[m]+".xlsx", sheet_name = "DATOS"))
    
data_cliente1=[]
for i in range(12):
    df=data_clientes[i]
    
    df1=df.drop([0])
    df1["fecha"]=pd.to_datetime(df1.iloc[:, 0],format="%d/%m/%Y %H:%M")
    df1.set_index('fecha', inplace=True)
    df1=df1.drop(["Unnamed: 0"], axis=1)
    data_cliente1.append(df1)

#Codigo concatenado
Entrega_Men_TCH=[]
Retiro_Men_TCH=[]
for i in range(12):
    Entrega=pd.DataFrame(data_cliente1[i][data_cliente1[i].columns[0]])
    Retiro=pd.DataFrame(data_cliente1[i][data_cliente1[i].columns.drop(data_cliente1[i].columns[0])])
    Retiro_Total=pd.DataFrame(Retiro.sum(axis=1))
    Entrega.rename(columns = {Entrega.columns.to_list()[0] : "Energía" }, inplace =True)
    Retiro_Total.rename(columns = {Retiro_Total.columns.to_list()[0] : "Energía" }, inplace =True)
    
    Entrega_Men_TCH.append(Entrega)
    Retiro_Men_TCH.append(Retiro_Total)

firma_Entrega=[Entrega_Men,Entrega_Men_CERE,Entrega_Men_TCH]

firma_Retiro=[Retiro_Men,Retiro_Men_CERE,Retiro_Men_TCH]

import pandas as pd

i=2023
año=str(i)
año1=str(i-2000)

mes={"Enero":"01","Febrero":"02","Marzo":"03","Abril":"04","Mayo":"05","Junio":"06","Julio":"07","Agosto":"08","Setiembre":"09","Octubre":"10","Noviembre":"11","Diciembre":"12"}
mesM={"Enero":"ENERO","Febrero":"FEBRERO","Marzo":"MARZO","Abril":"ABRIL","Mayo":"MAYO","Junio":"JUNIO","Julio":"JULIO","Agosto":"AGOSTO","Setiembre":"SETIEMBRE","Octubre":"OCTUBRE","Noviembre":"NOVIEMBRE","Diciembre":"DICIEMBRE"}


data_clientes=[]

for m in ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Setiembre","Octubre","Noviembre","Diciembre"]: 
    data_clientes.append( pd.read_excel("Cobertura.xlsx", sheet_name = año+"_"+mes[m]))
    
data_cliente1=[]
for i in range(12):
    df=data_clientes[i]
#    df1=df.drop([0])
    df["fecha"]=pd.to_datetime(df.iloc[:, 0],format="%d/%m/%Y %H:%M")
    df.set_index('fecha', inplace=True)
    data_cliente1.append(df)

Compra=[]
Venta=[]
for i in range(12):
    COM=pd.DataFrame()
    COM["Energía"] = data_cliente1[i]["Fenix"]
    VEN=pd.DataFrame()
    VEN["Energía"] = data_cliente1[i]["Atria"]/4+data_cliente1[i]["Engie"]
    Compra.append(COM)
    Venta.append(VEN)
    
    
#Funciones
## Reporte de energía de TCH por bloques horarios

def check_time(hour, minute):
    if hour > 8 and hour < 12:
        return "B2"
    elif hour == 8 and minute >= 15:
        return "B2"
    else:
      if hour == 12 and minute ==0:
        return "B2"
      else:
            if hour > 12 and hour < 18:
                return "B3"
            elif hour == 12 and minute >= 15:
                return "B3"
            else:
              if hour == 18 and minute ==0:
                return "B3"
              else:
                if hour > 18 and hour < 23:
                    return "B4"
                elif hour == 18 and minute >= 15:
                    return "B4"
                else:
                  if hour == 23 and minute ==0:
                    return "B4"
                  else:
                    return "B1"


Nombre={0:"CELEPSA",1:"CERE",2:"TERMOCHILCA"}
def DibujarPorMes(mes,empresa):
    import plotly.graph_objects as go
    fig2 = go.Figure()
    for j in empresa:
        if j == empresa[0]:
            fig2.add_trace(go.Scatter(x=Entrega_Men_TCH[mes].index, y=firma_Entrega[j][mes]["Energía"]*4 ,line=dict(color='skyblue'),fill='tozeroy', mode='none', stackgroup='one', name="Entrega Spot "+Nombre[j]))
        else:
            fig2.add_trace(go.Scatter(x=Entrega_Men_TCH[mes].index, y=firma_Entrega[j][mes]["Energía"]*4 ,line=dict(color='skyblue'),fill='tonexty', mode='none', stackgroup='one', name="Entrega Spot "+Nombre[j]))
    
    if 0 in empresa:
        fig2.add_trace(go.Scatter(x=Entrega_Men_TCH[mes].index, y=Compra[mes]["Energía"]*4,fill='tonexty',line=dict(color='blue'), mode='lines', stackgroup='one', name='Compra Energía.'))

    # Agregar traza de líneas
    fig2.add_trace(go.Scatter(x=Retiro_Men_TCH[mes].index, y=sum(firma_Retiro[j][mes]["Energía"]*4  for j in empresa),line=dict(color='orange'), mode='lines', name='Retiro Spot'))
    if 2 in empresa:
        fig2.add_trace(go.Scatter(x=Retiro_Men_TCH[mes].index, y=sum(firma_Retiro[j][mes]["Energía"]*4  for j in empresa) + Venta[mes]["Energía"]*4,line=dict(color='red'), mode='lines', name='Venta Energía'))

    # Actualizar el diseño y mostrar el gráfico
    fig2.update_layout( xaxis_title='Fecha', yaxis_title='Potencia')
    
    return fig2

def TablaEx(empresa):
    B1=[]
    B2=[]
    B3=[]
    B4=[]
    for mes in range(12):
        
        if 0 in empresa:
                Entregas_Mes_Total=sum(firma_Entrega[j][mes]["Energía"] for j in empresa)+Compra[mes]["Energía"]
                if 3 in empresa:
                    Retiros_Mes_Total=sum(firma_Retiro[j][mes]["Energía"] for j in empresa)+Venta[mes]["Energía"]
                else:
                    Retiros_Mes_Total=sum(firma_Retiro[j][mes]["Energía"] for j in empresa)
        else:
                Entregas_Mes_Total=sum(firma_Entrega[j][mes]["Energía"] for j in empresa)
                if 3 in empresa:
                    Retiros_Mes_Total=sum(firma_Retiro[j][mes]["Energía"] for j in empresa)+Venta[mes]["Energía"]
                else:
                    Retiros_Mes_Total=sum(firma_Retiro[j][mes]["Energía"] for j in empresa)
        
        
        
        Exposición=Entregas_Mes_Total-Retiros_Mes_Total    
        Exposición_CLASIFICADA= pd.DataFrame(Exposición)
        Exposición_CLASIFICADA['Bloque hora'] = Exposición_CLASIFICADA.index.map(lambda x: check_time(x.hour, x.minute))

        Exposición_B1=Exposición_CLASIFICADA.loc[Exposición_CLASIFICADA["Bloque hora"] == "B1"]
        Exposición_B2=Exposición_CLASIFICADA.loc[Exposición_CLASIFICADA["Bloque hora"] == "B2"]
        Exposición_B3=Exposición_CLASIFICADA.loc[Exposición_CLASIFICADA["Bloque hora"] == "B3"]
        Exposición_B4=Exposición_CLASIFICADA.loc[Exposición_CLASIFICADA["Bloque hora"] == "B4"]

        Exposición_B1=Exposición_B1.drop(["Bloque hora"], axis = 1)
        Exposición_B2=Exposición_B2.drop(["Bloque hora"], axis = 1)
        Exposición_B3=Exposición_B3.drop(["Bloque hora"], axis = 1)
        Exposición_B4=Exposición_B4.drop(["Bloque hora"], axis = 1)

        B1.append(Exposición_B1)
        B2.append(Exposición_B2)
        B3.append(Exposición_B3)
        B4.append(Exposición_B4)

    Tabla_EX=[]
    for i in range(12):
        df=pd.DataFrame(index=["[23 - 8]", "[8 - 12]", "[12 - 18]", "[18 - 23]"])
        Horas_Sup=[round(B1[i].loc[B1[i]["Energía"] >= 0].sum().values[0]/1000,2),
               round(B2[i].loc[B2[i]["Energía"] >= 0].sum().values[0]/1000,2),
               round(B3[i].loc[B3[i]["Energía"] >= 0].sum().values[0]/1000,2),
               round(B4[i].loc[B4[i]["Energía"] >= 0].sum().values[0]/1000,2)]
        Horas_Sup_prom=[round(B1[i].loc[B1[i]["Energía"] >= 0].mean().values[0]*4,2),
               round(B2[i].loc[B2[i]["Energía"] >= 0].mean().values[0]*4,2),
               round(B3[i].loc[B3[i]["Energía"] >= 0].mean().values[0]*4,2),
               round(B4[i].loc[B4[i]["Energía"] >= 0].mean().values[0]*4,2)]
        Horas_Sup_max=[round(B1[i].loc[B1[i]["Energía"] >= 0].max().values[0]*4,2),
               round(B2[i].loc[B2[i]["Energía"] >= 0].max().values[0]*4,2),
               round(B3[i].loc[B3[i]["Energía"] >= 0].max().values[0]*4,2),
               round(B4[i].loc[B4[i]["Energía"] >= 0].max().values[0]*4,2)]


        df["Bloques (hrs)"]=["[23 - 8]", "[8 - 12]", "[12 - 18]", "[18 - 23]"]
        df["Energía (GWh)"]=Horas_Sup
        df["Potencia Promedio (MW)"]=Horas_Sup_prom
        df["Potencia Máxima (MW)"]=Horas_Sup_max

        Tabla_EX.append(df)
            
    return Tabla_EX

def TablaDef(empresa):
    B1=[]
    B2=[]
    B3=[]
    B4=[]
    for mes in range(12):
        
        if 0 in empresa:
                Entregas_Mes_Total=sum(firma_Entrega[j][mes]["Energía"] for j in empresa)+Compra[mes]["Energía"]
                if 3 in empresa:
                    Retiros_Mes_Total=sum(firma_Retiro[j][mes]["Energía"] for j in empresa)+Venta[mes]["Energía"]
                else:
                    Retiros_Mes_Total=sum(firma_Retiro[j][mes]["Energía"] for j in empresa)
        else:
                Entregas_Mes_Total=sum(firma_Entrega[j][mes]["Energía"] for j in empresa)
                if 3 in empresa:
                    Retiros_Mes_Total=sum(firma_Retiro[j][mes]["Energía"] for j in empresa)+Venta[mes]["Energía"]
                else:
                    Retiros_Mes_Total=sum(firma_Retiro[j][mes]["Energía"] for j in empresa)
        
        
        
        Exposición=Entregas_Mes_Total-Retiros_Mes_Total    
        Exposición_CLASIFICADA= pd.DataFrame(Exposición)
        Exposición_CLASIFICADA['Bloque hora'] = Exposición_CLASIFICADA.index.map(lambda x: check_time(x.hour, x.minute))

        Exposición_B1=Exposición_CLASIFICADA.loc[Exposición_CLASIFICADA["Bloque hora"] == "B1"]
        Exposición_B2=Exposición_CLASIFICADA.loc[Exposición_CLASIFICADA["Bloque hora"] == "B2"]
        Exposición_B3=Exposición_CLASIFICADA.loc[Exposición_CLASIFICADA["Bloque hora"] == "B3"]
        Exposición_B4=Exposición_CLASIFICADA.loc[Exposición_CLASIFICADA["Bloque hora"] == "B4"]

        Exposición_B1=Exposición_B1.drop(["Bloque hora"], axis = 1)
        Exposición_B2=Exposición_B2.drop(["Bloque hora"], axis = 1)
        Exposición_B3=Exposición_B3.drop(["Bloque hora"], axis = 1)
        Exposición_B4=Exposición_B4.drop(["Bloque hora"], axis = 1)

        B1.append(Exposición_B1)
        B2.append(Exposición_B2)
        B3.append(Exposición_B3)
        B4.append(Exposición_B4)

    Tabla_DEF=[]
    for i in range(12):
        df=pd.DataFrame(index=["[23 - 8]", "[8 - 12]", "[12 - 18]", "[18 - 23]"])
        Horas_Sup=[round(B1[i].loc[B1[i]["Energía"] <0].sum().values[0]*-1/1000,2),
               round(B2[i].loc[B2[i]["Energía"] < 0].sum().values[0]*-1/1000,2),
               round(B3[i].loc[B3[i]["Energía"] < 0].sum().values[0]*-1/1000,2),
               round(B4[i].loc[B4[i]["Energía"] < 0].sum().values[0]*-1/1000,2)]
        Horas_Sup_prom=[round(B1[i].loc[B1[i]["Energía"] < 0].mean().values[0]*-1*4,2),
               round(B2[i].loc[B2[i]["Energía"] < 0].mean().values[0]*-1*4,2),
               round(B3[i].loc[B3[i]["Energía"] < 0].mean().values[0]*-1*4,2),
               round(B4[i].loc[B4[i]["Energía"] < 0].mean().values[0]*-1*4,2)]
        Horas_Sup_max=[round(B1[i].loc[B1[i]["Energía"] < 0].min().values[0]*-1*4,2),
               round(B2[i].loc[B2[i]["Energía"] < 0].min().values[0]*-1*4,2),
               round(B3[i].loc[B3[i]["Energía"] < 0].min().values[0]*-1*4,2),
               round(B4[i].loc[B4[i]["Energía"] < 0].min().values[0]*-1*4,2)]


        df["Bloques (hrs)"]=["[23 - 8]", "[8 - 12]", "[12 - 18]", "[18 - 23]"]
        df["Energía (GWh)"]=Horas_Sup
        df["Potencia Promedio (MW)"]=Horas_Sup_prom
        df["Potencia Máxima (MW)"]=Horas_Sup_max

        Tabla_DEF.append(df)


    return Tabla_DEF

#Concatenado todo el año

#Año
Total_Entrega=[]
Total_Retiro=[]
for mes in range(12):
    Total_Entrega.append(Entrega_Men_TCH[mes]['Energía']+Entrega_Men_CERE[mes]['Energía']+Entrega_Men[mes]['Energía']+Compra[mes]["Energía"])
    Total_Retiro.append(Retiro_Men_TCH[mes]['Energía']+Retiro_Men_CERE[mes]['Energía']+Retiro_Men[mes]['Energía']+Venta[mes]["Energía"])
    
    Total_Entrega[mes] = pd.DataFrame(Total_Entrega[mes])
    Total_Retiro[mes] = pd.DataFrame(Total_Retiro[mes])
Entregas_concatenado = pd.concat(Total_Entrega, axis=0, ignore_index=False)
Retiros_concatenado = pd.concat(Total_Retiro, axis=0, ignore_index=False)

fig = go.Figure()

# Agregar traza de dispersión
fig.add_trace(go.Scatter(x=Entregas_concatenado.index, y=Entregas_concatenado['Energía']*4,fill='tozeroy', mode='lines', name='Entrega'))

# Agregar traza de líneas
fig.add_trace(go.Scatter(x=Retiros_concatenado.index, y=Retiros_concatenado['Energía']*4, mode='lines', name='Retiro'))

# Actualizar el diseño y mostrar el gráfico
fig.update_layout( xaxis_title='Fecha', yaxis_title='Potencia')


import dash
import dash_html_components as html
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from textwrap import dedent
import plotly.graph_objects as go
from dash_table import DataTable
#import weasyprint
#from io import BytesIO
#import base64

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')


data = [
    {'ID': 1, 'Nombre': 'Juan', 'Edad': 25},
    {'ID': 2, 'Nombre': 'María', 'Edad': 30},
    {'ID': 3, 'Nombre': 'Carlos', 'Edad': 22},
]

# Radio constants
radio_categories = ["UMTS", "LTE", "GSM", "CDMA"]
radio_colors_list = ["green", "red", "blue", "orange"]
radio_colors = {cat: color for cat, color in zip(radio_categories, radio_colors_list)}

# Colors
bgcolor = "#f3f3f1"  # mapbox light map land color
bar_bgcolor = "#b0bec5"  # material blue-gray 200
bar_unselected_color = "#78909c"  # material blue-gray 400
bar_color = "#546e7a"  # material blue-gray 600
bar_selected_color = "#37474f"  # material blue-gray 800
bar_unselected_opacity = 0.8


# Colours
color_1 = "#003399"
color_2 = "#00ffff"
color_3 = "#002277"
color_b = "#F8F8FF"

def blank_fig(height):
    """
    Build blank figure with the requested height
    """
    return {
        "data": [],
        "layout": {
            "height": height,
            "template": template,
            "xaxis": {"visible": False},
            "yaxis": {"visible": False},
        },
    }

# Figure template
row_heights = [150, 500, 300]
template = {"layout": {"paper_bgcolor": bgcolor, "plot_bgcolor": bgcolor}}

def build_modal_info_overlay(id, side, content):
    """
    Build div representing the info overlay for a plot panel
    """
    div = html.Div(
        [  # modal div
            html.Div(
                [  # content div
                    html.Div(
                        [
                            html.H4(
                                [
                                    "Info",
                                    html.Img(
                                        id=f"close-{id}-modal",
                                        src="assets/times-circle-solid.svg",
                                        n_clicks=0,
                                        className="info-icon",
                                        style={"margin": 0},
                                    ),
                                ],
                                className="container_title",
                                style={"color": "white"},
                            ),
                            dcc.Markdown(content),
                        ]
                    )
                ],
                className=f"modal-content {side}",
            ),
            html.Div(className="modal"),
        ],
        id=f"{id}-modal",
        style={"display": "none"},
    )

    return div

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(id="full-layout",
    children=[
        html.Div(
            [
                html.H1(
                    children=[
                        "Exposición al Spot",
                        html.A(
                            html.Img(
                                src="assets/dash-logo.png",
                                style={"float": "right", "height": "50px"},
                            ),
                            href="https://dash.plot.ly/",
                        ),
                    ],
                    style={"text-align": "left"},
                ),
            ]
        ),
        html.Div(
            children=[
                build_modal_info_overlay(
                    "indicator",
                    "bottom",
                    dedent(
                        """
             Gráfica con resolución horaria cada 15 minutos del mes seleccionado de nuestra producción neta + compra de energía
             y de nuestros retiros netos + venta de energía neta.
            """
                    ),
                ),
                build_modal_info_overlay(
                    "map",
                    "bottom",
                    dedent(
                        """
             Gráfica con resolución horaria cada 15 minutos de los útlimos 12 meses de nuestra producción neta + compra de energía
             y de nuestros retiros netos + venta de energía neta.
        """
                    ),
                ),
                build_modal_info_overlay(
                    "range",
                    "top",
                    dedent(
                        """
            Cuando estamos en Superavit de Energía en un determinado intervalo de operación
            se refiere a que nuestra producción de las centrales pertenencientes al grupo más
            la energía que compramos a otras generadoras es mayor a los retiros del spot de todos
            los clientes del portafolio más la venta de energía a otros generadores.
        """
                    ),
                ),
                build_modal_info_overlay(
                    "created",
                    "top",
                    dedent(
                        """
            Cuando estamos en Déficit de Energía en un determinado intervalo de operación
            se refiere a que nuestra producción de las centrales pertenencientes al grupo más
            la energía que compramos a otras generadoras es menor a los retiros del spot de todos
            los clientes del portafolio más la venta de energía a otros generadores.
        """
                    ),
                ),
                html.Div(
                    children=[
                        html.Div([ "Mes",
                            dcc.Dropdown(
                               options=[
                                   {'label': 'Enero', 'value': '0'},
                                   {'label': 'Febrero', 'value': '1'},
                                   {'label': 'Marzo', 'value': '2'},
                                   {'label': 'Abril', 'value': '3'},
                                   {'label': 'Mayo', 'value': '4'},
                                   {'label': 'Junio', 'value': '5'},
                                   {'label': 'Julio', 'value': '6'},
                                   {'label': 'Agosto', 'value': '7'},
                                   {'label': 'Setiembre', 'value': '8'},
                                   {'label': 'Octubre', 'value': '9'},
                                   {'label': 'Noviembre', 'value': '10'},
                                   {'label': 'Diciembre', 'value': '11'}
                               ],
                               value='0', id = "BOTON"
                            )
                        ]),
                        html.Div([ "Empresa",
                            dcc.Dropdown(
                               options=[
                                   {'label': 'CELEPSA', 'value': '0'},
                                   {'label': 'CERE', 'value': '1'},
                                   {'label': 'TERMOCHILCA', 'value': '2'},
                               ],
                               value=['0',"1","2"], id = "BOTON2",multi=True
                            )
                        ]),
#                        html.Button("Imprimir a PDF", id="btn-print"),
                        html.Div(
                            children=[
                                html.H4(
                                    [
                                        "En Superavit por Bloques",
                                        html.Img(
                                            id="show-range-modal",
                                            src="assets/question-circle-solid.svg",
                                            className="info-icon",
                                        ),
                                    ],
                                    className="container_title",
                                ),
                                DataTable(
                                    id = "Tabla1",
#                                    data=adjustedSales.to_dict(
#                                        "records"
#                                    ),
#                                    columns=[
#                                        {"id": c, "name": c}
#                                        for c in adjustedSales.columns
#                                    ],
                                    style_data_conditional=[
                                        {
                                            "if": {"row_index": "odd"},
                                            "backgroundColor": color_b,
                                        },
                                        {
                                            "if": {
                                                "column_id": "Bloques (hrs)"
                                            },
                                            "backgroundColor": color_2,
                                            "color": "black",
                                        },
                                    ],
                                    style_header={
                                        "backgroundColor": color_1,
                                        "fontWeight": "bold",
                                        "color": "white",
                                    },
                                    fixed_rows={"headers": True},
                                    style_cell={"width": "150px"},
                                ),
                            ],
                            className="six columns pretty_container",
                            id="range-div",
                        ),
                        html.Div(
                            children=[
                                html.H4(
                                    [
                                        "En Deficit por Bloques",
                                        html.Img(
                                            id="show-created-modal",
                                            src="assets/question-circle-solid.svg",
                                            className="info-icon",
                                        ),
                                    ],
                                    className="container_title",
                                ),
                                DataTable(
                                    id= "Tabla2",
                                    style_data_conditional=[
                                        {
                                            "if": {"row_index": "odd"},
                                            "backgroundColor": color_b,
                                        },
                                        {
                                            "if": {
                                                "column_id": "Bloques (hrs)"
                                            },
                                            "backgroundColor": color_2,
                                            "color": "black",
                                        },
                                    ],
                                    style_header={
                                        "backgroundColor": color_1,
                                        "fontWeight": "bold",
                                        "color": "white",
                                    },
                                    fixed_rows={"headers": True},
                                    style_cell={"width": "150px"},
                                ),
                            ],
                            className="six columns pretty_container",
                            id="created-div",
                        ),
                        html.Div(
                        children=[
                        html.H4(
                            [
                                "Resolución Mensual",
                                html.Img(
                                    id="show-indicator-modal",
                                    src="assets/question-circle-solid.svg",
                                    className="info-icon",
                                ),
                            ],
                            className="container_title",
                        ),
                                dcc.Graph(
                                    id="Cada 15 min",
#                                    figure=  DibujarPorMes( html.Div(id='my-output') ),
#                                    blank_fig(row_heights[2]),
                                    config={"displayModeBar": False},
                                ),

                    ],
                    className="twelve columns pretty_container",
                    style={
                        "width": "98%",
                        "margin-right": "0",
                    },
                    id="indicator-div",
                ),
                        html.Div(
                        children=[
                        html.H4(
                            [
                                "Resolución Anual",
                                html.Img(
                                    id="show-map-modal",
                                    src="assets/question-circle-solid.svg",
                                    className="info-icon",
                                ),
                            ],
                            className="container_title",
                        ),
                        dcc.Graph(
                            id="map-graph",
                            figure=fig,
                            config={"displayModeBar": False},
                        ),

                    ],
                    className="twelve columns pretty_container",
                    style={
                        "width": "98%",
                        "margin-right": "0",
                    },
                    id="map-div",
                ),
                        
                    ]
                ),
            ]
        ),
        html.Div(
            [
                html.H4("Principales Acontecimientos del Mes", style={"margin-top": "0"}),
                dcc.Markdown(
                    """\
 - Dashboard written in Python using the [Dash](https://dash.plot.ly/) web framework.
 - Parallel and distributed calculations implemented using the [Dask](https://dask.org/) Python library.
 - Server-side visualization of the location of all 40 million cell towers performed 
 using the [Datashader] Python library (https://datashader.org/).
 - Base map layer is the ["light" map style](https://www.mapbox.com/maps/light-dark/)
 provided by [mapbox](https://www.mapbox.com/).
 - Cell tower dataset provided by the [OpenCelliD Project](https://opencellid.org/) which is licensed under a
[_Creative Commons Attribution-ShareAlike 4.0 International License_](https://creativecommons.org/licenses/by-sa/4.0/).
 - Mapping from cell MCC/MNC to network operator scraped from https://cellidfinder.com/mcc-mnc.
 - Icons provided by [Font Awesome](https://fontawesome.com/) and used under the
[_Font Awesome Free License_](https://fontawesome.com/license/free). 
"""
                ),
            ],
            style={
                "width": "98%",
                "margin-right": "0",
                "padding": "10px",
            },
            className="twelve columns pretty_container",
        ),
        html.Div(html.Button("Imprimir a PDF", id="btn-print")),
        html.Div(id="div-to-print", style={'display': 'none'}),
    ]
)

#@app.callback(
#    Output("full-layout", "children"),
#    [Input("btn-print", "n_clicks")]
#)
#def print_to_pdf(n_clicks):
#    if not n_clicks:
#        return dash.no_update

    # Obtén el contenido completo del diseño
#    layout_content = html.Div(id="full-layout").children

#    # Convierte el contenido HTML del diseño a un archivo PDF usando weasyprint
#    pdf_data = BytesIO(weasyprint.HTML(string=html.to_html(layout_content)).write_pdf())

    # Codifica el PDF en base64 para incrustarlo en un enlace de descarga
#    pdf_base64 = base64.b64encode(pdf_data.getvalue()).decode('utf-8')

    # Devuelve un enlace de descarga
#    return html.Div([
#        html.A("Descargar PDF", href=f"data:application/pdf;base64,{pdf_base64}", download="output.pdf", target="_blank")
#    ])





# Create show/hide callbacks for each info modal
for id in ["indicator", "radio", "map", "range", "created"]:

    @app.callback(
        [Output(f"{id}-modal", "style"), Output(f"{id}-div", "style")],
        [Input(f"show-{id}-modal", "n_clicks"), Input(f"close-{id}-modal", "n_clicks")],
    )
    def toggle_modal(n_show, n_close):
        ctx = dash.callback_context
        if ctx.triggered and ctx.triggered[0]["prop_id"].startswith("show-"):
            return {"display": "block"}, {"zIndex": 1003}
        else:
            return {"display": "none"}, {"zIndex": 0}

        
@app.callback(
    [Output("Cada 15 min", "figure")],
    [Input("BOTON", "value"),
     Input("BOTON2", "value")]
)
def update_graph(value1,value2):
    # Llama a la función DibujarPorMes con el mes seleccionado
    valores2_enteros = [int(num) for num in value2]
    figure = DibujarPorMes(int(value1),valores2_enteros)
    return [figure]



@app.callback(
    Output('Tabla1', 'data'),
    [Input("BOTON", "value"),
     Input("BOTON2", "value")],
)
def update_table(mes,empresa):
    ga=[int(val) for val in empresa]
    data = TablaEx(ga)[int(mes)].to_dict("records")
    return data

@app.callback(
    Output('Tabla1', 'columns'),
    [Input("BOTON", "value"),
     Input("BOTON2", "value")],
)
def update_table(mes,empresa):
    ga=[int(val) for val in empresa]
    columns=[
    {"id": c, "name": c}
    for c in TablaEx(ga)[int(mes)].columns]
    return columns

@app.callback(
    Output('Tabla2', 'data'),
    [Input("BOTON", "value"),
     Input("BOTON2", "value")],
)
def update_table(mes,empresa):
    ga=[int(val) for val in empresa]
    data = TablaDef(ga)[int(mes)].to_dict("records")
    return data

@app.callback(
    Output('Tabla2', 'columns'),
    [Input("BOTON", "value"),
     Input("BOTON2", "value")],
)
def update_table(mes,empresa):
    ga=[int(val) for val in empresa]
    columns=[
    {"id": c, "name": c}
    for c in TablaDef(ga)[int(mes)].columns]
    return columns

    
if __name__ == '__main__':
    app.run_server(debug=server)
