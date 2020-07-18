import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px


from datetime import datetime as dt
import json
import numpy as np
import pandas as pd

#Recall app
from app import app

df_mj = pd.read_csv('data/reincidencia11junio2020_clean.csv', parse_dates=['FECHA_INGRESO','FECHA_SALIDA','FECHA_CAPTURA'])

df_mj_no_duplicates = df_mj[~df_mj.duplicated(['INTERNOEN'])]
df_mj_no_duplicates_ec = df_mj_no_duplicates['ESTADO_CIVIL'].value_counts().reset_index()
df_mj_no_duplicates_ec.columns = ["ESTADO_CIVIL","count"]
MS_hist = px.histogram(df_mj_no_duplicates_ec,x="ESTADO_CIVIL",y="count",nbins=50,hover_data=["ESTADO_CIVIL","count"])
MS_hist.update_layout(title="Marital Status Histogram")

df_mj_no_duplicates_mc = df_mj_no_duplicates["HIJOS_MENORES"].value_counts().reset_index()
df_mj_no_duplicates_mc.columns = ["HIJOS_MENORES","count"]
MC_hist = px.histogram(df_mj_no_duplicates_mc,x="HIJOS_MENORES",y="count",nbins=50,hover_data=["HIJOS_MENORES","count"],color="HIJOS_MENORES")
MC_hist.update_layout(title="Minor Children Histogram")

df_mj_no_duplicates_el = df_mj_no_duplicates["NIVEL_EDUCATIVO"].value_counts().reset_index()
df_mj_no_duplicates_el.columns = ["NIVEL_EDUCATIVO","count"]
EL_hist = px.histogram(df_mj_no_duplicates_el,x="NIVEL_EDUCATIVO",y="count",nbins=50,hover_data=["NIVEL_EDUCATIVO","count"])
EL_hist.update_layout(title="Education Level Histogram")

df_mj_etn=df_mj_no_duplicates["CONDIC_EXPECIONAL"].value_counts().reset_index()
df_mj_etn.columns=["CONDIC_EXPECIONAL","count"]
ET_hist = px.histogram(df_mj_etn,x="CONDIC_EXPECIONAL",y="count",nbins=50,hover_data=["CONDIC_EXPECIONAL","count"])
ET_hist.update_layout(title="Race/Ethnicity Histogram")

df_mj_men = df_mj_no_duplicates[df_mj_no_duplicates["GENERO"]=="MASCULINO"]
df_mj_men_hg=df_mj_men["EDAD"].value_counts().reset_index()
df_mj_men_hg.columns = ["EDAD","count"]
MA_hist = px.histogram(df_mj_men_hg,x="EDAD",y="count",nbins=50,hover_data=["EDAD","count"])
MA_hist.update_layout(title="Age Histogram of Male Recidivists")

df_mj_women = df_mj_no_duplicates[df_mj_no_duplicates["GENERO"]=="FEMENINO"]
df_mj_women_hg=df_mj_women["EDAD"].value_counts().reset_index()
df_mj_women_hg.columns = ["EDAD","count"]
WA_hist = px.histogram(df_mj_women_hg,x="EDAD",y="count",nbins=50,hover_data=["EDAD","count"])
WA_hist.update_layout(title="Age Histogram of Female Recidivists")

#################################################################################
# Here the layout for the plots to use.
#################################################################################
demographic_output=html.Div([
	#Place the different graph components here.
	dbc.Row([
        dbc.Col(dcc.Graph(figure=MS_hist, id='MS_hist')),
        dbc.Col(dcc.Graph(figure=MC_hist, id='MC_hist')),
	]),
	html.Hr(),
	dbc.Row([
        dbc.Col(dcc.Graph(figure=EL_hist, id='EL_hist')),
        dbc.Col(dcc.Graph(figure=ET_hist, id='ET_hist')),
	]),
	html.Hr(),
	dbc.Row([
        dbc.Col(dcc.Graph(figure=MA_hist, id='MA_hist')),
        dbc.Col(dcc.Graph(figure=WA_hist, id='WA_hist')),
	]),
	html.Hr(),
	],className="mj-body")
