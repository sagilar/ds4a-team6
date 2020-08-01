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
import requests

from app import app
# Call Webservice to get Crimes List:
r = requests.get("http://ds4at6api.azurewebsites.net/api/Crimes")
df_crimes =pd.read_json(r.text)
df_crimes = df_crimes.rename(columns={'name': 'label', 'crimeId': 'value'})
df_dropdown_crimes = df_crimes[['label', 'value']]
#df_crimes = df_crimes.drop(['crimeId'], axis = 1)
# Convert to a dictionary to let dropdown use it
crimes = json.loads(df_dropdown_crimes.to_json(orient="records"))

education_levels = [
                {'label': 'ANALFABETA', 'value': '1'},
                {'label': 'CICLO I', 'value': '2'},
                {'label': 'CICLO II', 'value': '3'},
                {'label': 'CICLO III', 'value': '4'},
                {'label': 'CICLO IV', 'value': '5'},
                {'label': 'PROFESIONAL', 'value': '9'},
                {'label': 'TECNICO', 'value': '10'},
                {'label': 'TECNICO PROFESIONAL', 'value': '11'},
                {'label': 'TECNOLOGICO', 'value': '12'},
                {'label': 'ESPECIALIZACION', 'value': '6'},
                {'label': 'MAGISTER', 'value': '7'},
                {'label': 'POST GRADO', 'value': '8'}                
            ]

age_input = dbc.FormGroup(
    [
        dbc.Label("Edad:", html_for="age_text"),
        html.Div(id='age_slider-container'),
        dbc.Input(type="number", min=18, max=100, value="21", step=1, id="age_text")
        
    ]
)

events_input = dbc.FormGroup(
    [
        dbc.Label("Reincidencias:", html_for="events_text"),
        dbc.Input(type="number", value="2", min=0, max=5, step=1, id="events_text")
    ]
)

education_input = dbc.FormGroup(
    [
        dbc.Label("Nivel de Educación:", html_for="education_dropdown"),
        dcc.Dropdown(
            id='education_dropdown',
            options= education_levels,
            value='9'
        )
    ]
)

studies_input = dbc.FormGroup(
    [
        dbc.Checklist(
            options=[
                {"label": "Realiza estudios en el centro de reclusión", "value": 1},
            ],
            value=[],
            id="studies_toogle",
            switch=True,
        ),
    ]
)
teaching_input = dbc.FormGroup(
    [
        dbc.Checklist(
            options=[
                {"label": "Realiza actividades de enseñanza", "value": 1},
            ],
            value=[],
            id="teaching_toogle",
            switch=True,
        ),
    ]
)
crime_input = dbc.FormGroup(
    [
        dbc.Label("Crimen:", html_for="crime_dropdown"),
        dcc.Dropdown(
            id='crime_dropdown',
            options= crimes,
            value="260"
        )
    ]
)

intento_switch = dbc.FormGroup(
    [
        dbc.Label("Clasificación:"),
        dbc.Checklist(
            options=[
                {"label": "Intento", "value": 1},
            ],
            value=[],
            id="intento_toogle",
            switch=True,
        ),
    ]
)
calificado_switch = dbc.FormGroup(
    [
        dbc.Checklist(
            options=[
                {"label": "Calificado", "value": 1},
            ],
            value=[],
            id="calificado_toogle",
            switch=True,
        ),
    ]
)
agravado_switch = dbc.FormGroup(
    [
        dbc.Checklist(
            options=[
                {"label": "Agravado", "value": 1},
            ],
            value=[],
            id="agravado_toogle",
            switch=True,
        ),
    ]
)

formLayout = html.Div(
    [ 
        dbc.Row(
            [
                dbc.Col(
                    children = [
                        age_input,
                        events_input,
                        education_input,
                        studies_input,
                        teaching_input,
                        crime_input,
                        intento_switch,
                        calificado_switch,
                        agravado_switch
                        
                    ],
                    md="4"
                ),
                dbc.Col(
                    children = [
                        dcc.Graph(id='result_output')
                    ],
                    md="8"
                )
            ]
        )
        
    ]
)

@app.callback(
    Output("result_output", "figure"), 
    [Input('age_text', 'value'),
     Input('events_text', 'value'),
     Input('education_dropdown', 'value'),
     Input('crime_dropdown', 'value'),
     Input('studies_toogle', 'value'),
     Input('teaching_toogle', 'value'),
     Input('intento_toogle', 'value'),
     Input('calificado_toogle', 'value'),
     Input('agravado_toogle', 'value'),
     
     ]
)
def update_graph(age, events, education, crime, studies, teaching, intento, calificado, agravado):
    # Load crime weight:
    if len(df_crimes[df_crimes.value == int(crime)]) > 0:
        weight = int(df_crimes[df_crimes.value == int(crime)].weight)
    else:
        weight = 5
    # Create payload with form values:
    payload = {"age": int(age),
        "cases": int(events),
        "education_level": int(education),
        "study": len(studies),
        "teaching": len(teaching),
        "attemp": len(intento),
        "aggravated": len(calificado),
        "qualified": len(agravado),
        "weight": weight
    }
    print(payload)
    # Generate chart:
    #1. Get Info from web service
    url = "https://team6flaskapi.azurewebsites.net/survival"
    requestSurvival = requests.post(url, json=payload)
    df_model = pd.read_json(requestSurvival.text)
    #2. Generate scatter chart with info
    fig = go.Figure(data=go.Scatter(x=df_model.dia, y=df_model.prob))
    fig.update_layout(xaxis_title ="Días",yaxis_title = "Probabilidad", title = "Probabilidad de Reincidencia en el Tiempo", width=800, height=400)
    return fig