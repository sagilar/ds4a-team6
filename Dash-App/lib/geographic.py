import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import geopandas


from datetime import datetime as dt
import json
import numpy as np
import pandas as pd

#Recall app
from app import app

df_mj = pd.read_csv('../retomintic/Data_UpdateJune13/reincidencia11junio2020_clean.csv', parse_dates=['FECHA_INGRESO','FECHA_SALIDA','FECHA_CAPTURA'])



dept_count = df_mj["DEPTO_ESTABLECIMIENTO"].value_counts()
df_dept_count = dept_count.reset_index()
df_dept_count.columns = ["DEPTO_ESTABLECIMIENTO","count"]
#print(df_dept_count.head())

##############################################################
# RECIDIVISM BY DEPARTMENT HISTOGRAM
###############################################################

Rec_dep_fig = px.histogram(df_dept_count,x="DEPTO_ESTABLECIMIENTO",y="count",nbins=50,hover_data=["DEPTO_ESTABLECIMIENTO","count"])
Rec_dep_fig.update_layout(title="Recidivism by department")

add_data = {'NOMBRE_DPT':["VAUPES","VICHADA","GUAVIARE","GUAINIA"],'count':[0,0,0,0]}
add_df = pd.DataFrame(data=add_data)


df_dept_count["DEPTO_ESTABLECIMIENTO"][df_dept_count["DEPTO_ESTABLECIMIENTO"]=="BOGOTA D.C."]="SANTAFE DE BOGOTA D.C"#]="BOGOTA D.C."
df_dept_count["DEPTO_ESTABLECIMIENTO"][df_dept_count["DEPTO_ESTABLECIMIENTO"]=="SAN ANDRES Y PROVIDENCIA"]="ARCHIPIELAGO DE SAN ANDRES PROVIDENCIA Y SANTA CATALINA"#]="SAN ANDRES Y PROVIDENCIA"
df_dept_count.columns = ["NOMBRE_DPT","count"]
df_dept_count_comp = pd.concat([df_dept_count,add_df],ignore_index=True)
df_dept_count_comp.fillna(0,inplace=True)
#############################
# Load map data
#############################
with open('../Colombia_mod.geo.json') as geo:
    geojson_file = json.loads(geo.read())
#Create the map:
Map_Fig=px.choropleth_mapbox(df_dept_count_comp,
        locations='NOMBRE_DPT',
        color='count',
        geojson=geojson_file,
        zoom=3,
        mapbox_style="carto-positron",
        center={"lat": 4.12, "lon": -73.22},
        color_continuous_scale="Viridis",
        opacity=0.5,
        labels={"count":"Recidivism by department"}
        )
Map_Fig.update_layout(title='Colombian Recividism Map',paper_bgcolor="#F8F9F9")


#################################################################################
# Here the layout for the plots to use.
#################################################################################
geographic_output=html.Div([
	#Place the different graph components here.
    dcc.Graph(figure=Rec_dep_fig,id="Recidivism_dept_hist"),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=Map_Fig, id='Colombia_map')),
        dbc.Col(),
	]),
    ],className="mj-body")
