import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
from pathlib import Path
import os.path
#from lifelines import KaplanMeierFitter, CoxPHFitter


from datetime import datetime as dt
import json
import numpy as np
import pandas as pd

#Recall app
from app import app
try:
    if os.path.exists('output_data/time_analysis_df.csv'):
        df_mj_mod = pd.read_csv('output_data/time_analysis_df.csv',parse_dates=['FECHA_INGRESO','FECHA_SALIDA','FECHA_CAPTURA'])
    else:
        df_mj = pd.read_csv('../retomintic/Data_UpdateJune13/reincidencia11junio2020_clean.csv', parse_dates=['FECHA_INGRESO','FECHA_SALIDA','FECHA_CAPTURA'])

        df_mj_mod = df_mj.copy()

        #Date variables are parsed to datetime
        df_mj_mod["FECHA_CAPTURA"] = pd.to_datetime(df_mj_mod["FECHA_CAPTURA"])
        df_mj_mod["FECHA_INGRESO"] = pd.to_datetime(df_mj_mod["FECHA_INGRESO"])
        df_mj_mod["FECHA_SALIDA"] = pd.to_datetime(df_mj_mod["FECHA_SALIDA"])
        #Month and year variables are defined
        df_mj_mod["MES_INGRESO_INT"]=df_mj_mod["FECHA_INGRESO"].dt.strftime('%m')
        df_mj_mod["ANO_INGRESO_INT"]=df_mj_mod["FECHA_INGRESO"].dt.strftime('%y')
        #Calculations on how much time have the criminal being outside since its last stay in jail
        for column in ['FECHA_INGRESO', 'FECHA_SALIDA', 'FECHA_CAPTURA']:
            df_mj_mod = df_mj_mod.sort_values(['INTERNOEN', column], ascending = False)

            df_mj_mod['DIAS' + column[5:]] = -1*(df_mj_mod[column].diff()/timedelta(days = 1))

            df_mj_mod.loc[(df_mj_mod.INTERNOEN != df_mj_mod.INTERNOEN.shift(1)) | (df_mj_mod['DIAS' + column[5:]] == 0),
                      ['DIAS' + column[5:]]] = (datetime.today() - df_mj_mod[column])/timedelta(days = 1)

        #It seems that sometimes entering and gettint out is switched, that's why we computed in absolute values
        df_mj_mod['DIAS_CONDENA'] = abs(df_mj_mod['FECHA_SALIDA'] - df_mj_mod['FECHA_INGRESO'])/timedelta(days = 1)
        df_mj_mod['DIAS_JUDICIALIZACION'] = df_mj_mod['FECHA_INGRESO'] - df_mj_mod['FECHA_CAPTURA']
        df_mj_mod['DIAS_LIBRE'] = df_mj_mod['DIAS_INGRESO'] - df_mj_mod['DIAS_CONDENA']
        #The individual finishes its sentence but she's incarcelated inmediately for another crime
        df_mj_mod.loc[df_mj_mod.DIAS_CAPTURA < 0, 'DIAS_CAPTURA'] = 0
        df_mj_mod.loc[df_mj_mod.DIAS_INGRESO < 0, 'DIAS_INGRESO'] = 0
        df_mj_mod.loc[df_mj_mod.DIAS_LIBRE < 0, 'DIAS_LIBRE'] = 0
        #The individual is still on jail
        df_mj_mod.loc[df_mj_mod['DIAS_LIBRE'].isnull(), 'DIAS_LIBRE'] = 0

        #Find the last date the criminal went out the jail, so that these observations are marked as censored
        last_df = df_mj_mod[['INTERNOEN', 'FECHA_INGRESO']].groupby('INTERNOEN').apply(lambda x: x.sort_values('FECHA_INGRESO', ascending = False).head(1)).reset_index(drop = True)
        #Censored
        last_df['CENSURADO_LIBRES'] = 0
        df_mj_mod = df_mj_mod.merge(last_df, on = ['INTERNOEN', 'FECHA_INGRESO'], how = 'left')
        #Event
        df_mj_mod.loc[df_mj_mod['CENSURADO_LIBRES'].isnull(), 'CENSURADO_LIBRES'] = 1
        #All criminals that haven't got out of jail yet have zero days out and they are not censored.
        df_mj_mod.loc[df_mj_mod['FECHA_SALIDA'].isnull(), 'CENSURADO_LIBRES'] = 1
        #Turned censored variables to integers instead of float
        df_mj_mod['CENSURADO_LIBRES'] = df_mj_mod['CENSURADO_LIBRES'].astype('int64')

        #We create a variable to count the amount of times the individual re-entered in jail
        df_mj_mod = df_mj_mod.merge(df_mj_mod.drop_duplicates(['INTERNOEN', 'FECHA_INGRESO']).groupby(['INTERNOEN']).size().reset_index(name = 'NUMERO_REINCIDENCIAS'), on = 'INTERNOEN', how = 'left')

        #We dropped SITUACION_JURIDICA and REINCIDENTE as both columns are constants
        df_mj_mod = df_mj_mod.drop(columns = ['SITUACION_JURIDICA', 'REINCIDENTE'])

        df_mj_mod.to_csv('output_data/time_analysis_df.csv',index=False)
except:
    df_mj = pd.read_csv('../retomintic/Data_UpdateJune13/reincidencia11junio2020_clean.csv', parse_dates=['FECHA_INGRESO','FECHA_SALIDA','FECHA_CAPTURA'])

    df_mj_mod = df_mj.copy()

    #Date variables are parsed to datetime
    df_mj_mod["FECHA_CAPTURA"] = pd.to_datetime(df_mj_mod["FECHA_CAPTURA"])
    df_mj_mod["FECHA_INGRESO"] = pd.to_datetime(df_mj_mod["FECHA_INGRESO"])
    df_mj_mod["FECHA_SALIDA"] = pd.to_datetime(df_mj_mod["FECHA_SALIDA"])
    #Month and year variables are defined
    df_mj_mod["MES_INGRESO_INT"]=df_mj_mod["FECHA_INGRESO"].dt.strftime('%m')
    df_mj_mod["ANO_INGRESO_INT"]=df_mj_mod["FECHA_INGRESO"].dt.strftime('%y')
    #Calculations on how much time have the criminal being outside since its last stay in jail
    for column in ['FECHA_INGRESO', 'FECHA_SALIDA', 'FECHA_CAPTURA']:
        df_mj_mod = df_mj_mod.sort_values(['INTERNOEN', column], ascending = False)

        df_mj_mod['DIAS' + column[5:]] = -1*(df_mj_mod[column].diff()/timedelta(days = 1))

        df_mj_mod.loc[(df_mj_mod.INTERNOEN != df_mj_mod.INTERNOEN.shift(1)) | (df_mj_mod['DIAS' + column[5:]] == 0),
                  ['DIAS' + column[5:]]] = (datetime.today() - df_mj_mod[column])/timedelta(days = 1)

    #It seems that sometimes entering and gettint out is switched, that's why we computed in absolute values
    df_mj_mod['DIAS_CONDENA'] = abs(df_mj_mod['FECHA_SALIDA'] - df_mj_mod['FECHA_INGRESO'])/timedelta(days = 1)
    df_mj_mod['DIAS_JUDICIALIZACION'] = df_mj_mod['FECHA_INGRESO'] - df_mj_mod['FECHA_CAPTURA']
    df_mj_mod['DIAS_LIBRE'] = df_mj_mod['DIAS_INGRESO'] - df_mj_mod['DIAS_CONDENA']
    #The individual finishes its sentence but she's incarcelated inmediately for another crime
    df_mj_mod.loc[df_mj_mod.DIAS_CAPTURA < 0, 'DIAS_CAPTURA'] = 0
    df_mj_mod.loc[df_mj_mod.DIAS_INGRESO < 0, 'DIAS_INGRESO'] = 0
    df_mj_mod.loc[df_mj_mod.DIAS_LIBRE < 0, 'DIAS_LIBRE'] = 0
    #The individual is still on jail
    df_mj_mod.loc[df_mj_mod['DIAS_LIBRE'].isnull(), 'DIAS_LIBRE'] = 0

    #Find the last date the criminal went out the jail, so that these observations are marked as censored
    last_df = df_mj_mod[['INTERNOEN', 'FECHA_INGRESO']].groupby('INTERNOEN').apply(lambda x: x.sort_values('FECHA_INGRESO', ascending = False).head(1)).reset_index(drop = True)
    #Censored
    last_df['CENSURADO_LIBRES'] = 0
    df_mj_mod = df_mj_mod.merge(last_df, on = ['INTERNOEN', 'FECHA_INGRESO'], how = 'left')
    #Event
    df_mj_mod.loc[df_mj_mod['CENSURADO_LIBRES'].isnull(), 'CENSURADO_LIBRES'] = 1
    #All criminals that haven't got out of jail yet have zero days out and they are not censored.
    df_mj_mod.loc[df_mj_mod['FECHA_SALIDA'].isnull(), 'CENSURADO_LIBRES'] = 1
    #Turned censored variables to integers instead of float
    df_mj_mod['CENSURADO_LIBRES'] = df_mj_mod['CENSURADO_LIBRES'].astype('int64')

    #We create a variable to count the amount of times the individual re-entered in jail
    df_mj_mod = df_mj_mod.merge(df_mj_mod.drop_duplicates(['INTERNOEN', 'FECHA_INGRESO']).groupby(['INTERNOEN']).size().reset_index(name = 'NUMERO_REINCIDENCIAS'), on = 'INTERNOEN', how = 'left')

    #We dropped SITUACION_JURIDICA and REINCIDENTE as both columns are constants
    df_mj_mod = df_mj_mod.drop(columns = ['SITUACION_JURIDICA', 'REINCIDENTE'])

    df_mj_mod.to_csv('output_data/time_analysis_df.csv',index=False)

#df_genero = df_mj.loc[df_mj.duplicated(['INTERNOEN', 'ANO_INGRESO_INT']), ['GENERO', 'ANO_INGRESO_INT', 'INTERNOEN']].copy()
#df_genero['value'] = 1
#df_genero['GENERO'].replace({'FEMENINO':'Femenino', 'MASCULINO':'Masculino'}, inplace = True)
#df_genero.columns = ['Sexo', 'ANO_INGRESO_INT', 'INTERNOEN', 'value']
#df_genero = df_genero.pivot_table(values = 'value', index = ['INTERNOEN', 'ANO_INGRESO_INT'], columns = 'Sexo').fillna(0)

#df_graph_genero = df_genero.reset_index().groupby('ANO_INGRESO_INT').sum()
#df_graph_genero['Femenino'] = df_graph_genero['Femenino']/365
#df_graph_genero['Masculino'] = df_graph_genero['Masculino']/365

#fig_genero = px.box(df_graph_genero,y="DIAS_LIBRE",x="GENERO")

#fig_genero = px.box(df_mj_mod.sort_values('FECHA_INGRESO').loc[df_mj_mod.duplicated('INTERNOEN', 'last'), ['GENERO', 'DIAS_LIBRE']],y="DIAS_LIBRE",x="GENERO")
#
#print(df_mj_mod)

df_gen_fin = df_mj_mod.groupby(['INTERNOEN', 'GENERO'])['DIAS_CONDENA'].mean().reset_index(name = 'DIAS_CONDENA')
df_gen_fin.columns = ['ID', 'GENERO', 'DIAS_CONDENA']
#print(df_gen_fin)
df_gen_fin['GENERO'].replace({"MASCULINO": "Masculino", "FEMENINO": "Femenino"}, inplace=True)

fig_genero = px.box(
    df_gen_fin,
    x='GENERO',
    y='DIAS_CONDENA',
    color = 'GENERO')
fig_genero.update_layout(title='TOTAL DAYS OUTSIDE JAIL BY GENDER',paper_bgcolor="#F8F9F9")

df = df_mj_mod.drop_duplicates(['INTERNOEN', 'FECHA_INGRESO']).groupby(['INTERNOEN', 'ACTIVIDADES_ESTUDIO'])['DIAS_CONDENA'].mean().reset_index(name = 'DIAS_CONDENA')
df.columns = ['id', 'Actividades de estudio', 'Días de condena']
df['Actividades de estudio'] = df['Actividades de estudio'].str.capitalize()

fig_act_est = px.box(
    df,
    x= 'Actividades de estudio',
    y='Días de condena',
    color = 'Actividades de estudio')
fig_act_est.update_layout(title='TOTAL CONVICTION DAYS BY EDUCATION ACTIVITIES',paper_bgcolor="#F8F9F9")

df = df_mj_mod.groupby(['INTERNOEN', 'ACTIVIDADES_ESTUDIO'])['DIAS_LIBRE'].mean().reset_index(name = 'DIAS_LIBRE')
df.columns = ['id', 'Actividades de estudio', 'Días en libertad']
df['Actividades de estudio'] = df['Actividades de estudio'].str.capitalize()

fig_freedom_days = px.box(
    df,
    x= 'Actividades de estudio',
    y='Días en libertad',
    color = 'Actividades de estudio')
fig_freedom_days.update_layout(title='TOTAL FREEDOM DAYS BY EDUCATION ACTIVITIES',paper_bgcolor="#F8F9F9")

df = df_mj_mod.groupby(['INTERNOEN', 'ACTIVIDADES_ENSEÑANZA'])['DIAS_CONDENA'].mean().reset_index(name = 'DIAS_CONDENA')
df.columns = ['id', 'Actividades de enseñanza', 'Días de condena']
df['Actividades de enseñanza'] = df['Actividades de enseñanza'].str.capitalize()

fig_teach = px.box(
    df,
    x= 'Actividades de enseñanza',
    y='Días de condena',
    color = 'Actividades de enseñanza')
fig_teach.update_layout(title='TOTAL CONVICTION DAYS BY TEACHING ACTIVITIES',paper_bgcolor="#F8F9F9")

df = df_mj_mod.groupby(['INTERNOEN', 'ACTIVIDADES_ENSEÑANZA'])['DIAS_LIBRE'].mean().reset_index(name = 'DIAS_LIBRE')
df.columns = ['id', 'Actividades de enseñanza', 'Días en libertad']
df['Actividades de estudio'] = df['Actividades de enseñanza'].str.capitalize()

fig_freedom_teach = px.box(
    df,
    x= 'Actividades de enseñanza',
    y='Días en libertad',
    color = 'Actividades de enseñanza')
fig_freedom_teach.update_layout(title='TOTAL FREEDOM DAYS BY TEACHING ACTIVITIES',paper_bgcolor="#F8F9F9")

df = df_mj_mod.groupby(['INTERNOEN', 'ACTIVIDADES_TRABAJO'])['DIAS_CONDENA'].mean().reset_index(name = 'DIAS_CONDENA')
df.columns = ['id', 'Actividades de trabajo', 'Días de condena']
df['Actividades de trabajo'] = df['Actividades de trabajo'].str.capitalize()

fig_work = px.box(
    df,
    x= 'Actividades de trabajo',
    y='Días de condena',
    color = 'Actividades de trabajo')
fig_work.update_layout(title='TOTAL CONVICTION DAYS BY WORKING ACTIVITIES',paper_bgcolor="#F8F9F9")

df = df_mj_mod.groupby(['INTERNOEN', 'ACTIVIDADES_TRABAJO'])['DIAS_LIBRE'].mean().reset_index(name = 'DIAS_LIBRE')
df.columns = ['id', 'Actividades de trabajo', 'Días en libertad']
df['Actividades de trabajo'] = df['Actividades de trabajo'].str.capitalize()

fig_freedom_work = px.box(
    df,
    x= 'Actividades de trabajo',
    y='Días en libertad',
    color = 'Actividades de trabajo')
fig_freedom_work.update_layout(title='TOTAL FREEDOM DAYS BY WORKING ACTIVITIES',paper_bgcolor="#F8F9F9")

#################################################################################
# Here the layout for the plots to use.
#################################################################################
timeanalysis_output=html.Div([
	#Place the different graph components here.
	dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_genero, id='time_outside_jail_gender')),
        dbc.Col(dcc.Graph(figure=fig_act_est, id='time_convictions_edu_act')),
	]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_freedom_days, id='time_freedom_edu_act')),
        dbc.Col(dcc.Graph(figure=fig_teach, id='time_convictions_tea_activities')),
	]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_freedom_teach, id='time_freedom_tea_act')),
        dbc.Col(dcc.Graph(figure=fig_work, id='time_convictions_work_activities')),
	]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_freedom_work, id='time_freedom_work_act')),
        dbc.Col(),
	]),
	],className="mj-body")
