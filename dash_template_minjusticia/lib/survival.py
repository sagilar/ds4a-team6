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

import pickle ## to load models.
<<<<<<< HEAD
=======
import joblib
>>>>>>> d17ec26a8dd76b1ca1502eb23dd585e8b5ba8e00

from app import app
# Call Webservice to get Crimes List:
r = requests.get("http://ds4at6api.azurewebsites.net/api/Crimes")
df_crimes =pd.read_json(r.text)
df_crimes = df_crimes.rename(columns={'name': 'label', 'crimeId': 'value'})
df_dropdown_crimes = df_crimes[['label', 'value']]
#df_crimes = df_crimes.drop(['crimeId'], axis = 1)
# Convert to a dictionary to let dropdown use it
crimes = json.loads(df_dropdown_crimes.to_json(orient="records"))

## Loading models
#survival_model = pickle.load(open("data/modelo_COX_shdi_P4.pickle", 'rb'))
#with open(r"data/modelo_COX_shdi_P4.pickle", "rb") as input_file:
#    survival_model = pickle.load(input_file)
<<<<<<< HEAD

education_levels = [
=======
survival_model = joblib.load("data/modelo_cox_cluster.pickle")

'''education_levels = [
>>>>>>> d17ec26a8dd76b1ca1502eb23dd585e8b5ba8e00
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
<<<<<<< HEAD
            ]
=======
            ]'''
education_levels = [
                {'label': 'ANALFABETA', 'value': '0'},
                {'label': 'CICLO I', 'value': '2'},
                {'label': 'CICLO II', 'value': '5'},
                {'label': 'CICLO III', 'value': '9'},
                {'label': 'CICLO IV', 'value': '11'},
                {'label': 'PROFESIONAL', 'value': '16'},
                {'label': 'TECNICO', 'value': '13'},
                {'label': 'TECNICO PROFESIONAL', 'value': '13'},
                {'label': 'TECNOLOGICO', 'value': '14'},
                {'label': 'ESPECIALIZACION', 'value': '18'},
                {'label': 'MAGISTER', 'value': '18'},
                {'label': 'POST GRADO', 'value': '18'}
            ]
gnic_data = ['risaralda', 'bogota', 'caldas', 'antioquia', 'santander',
'cundinamarca', 'valle del cauca', 'quindio', 'atlantico',
'san andres']
departments_dd = [
                    {'label': 'amazonas', 'value': 'amazonas'},
                    {'label': 'antioquia', 'value': 'antioquia'},
                    {'label': 'arauca', 'value': 'arauca'},
                    {'label': 'atlantico', 'value': 'atlantico'},
                    {'label': 'bogota', 'value': 'bogota'},
                    {'label': 'bolivar', 'value': 'bolivar'},
                    {'label': 'boyaca', 'value': 'boyaca'},
                    {'label': 'caldas', 'value': 'caldas'},
                    {'label': 'caqueta', 'value': 'caqueta'},
                    {'label': 'casanare', 'value': 'casanare'},
                    {'label': 'cauca', 'value': 'cauca'},
                    {'label': 'cesar', 'value': 'cesar'},
                    {'label': 'choco', 'value': 'choco'},
                    {'label': 'cordoba', 'value': 'cordoba'},
                    {'label': 'cundinamarca', 'value': 'cundinamarca'},
                    {'label': 'guainia', 'value': 'guainia'},
                    {'label': 'guajira', 'value': 'guajira'},
                    {'label': 'guaviare', 'value': 'guaviare'},
                    {'label': 'huila', 'value': 'huila'},
                    {'label': 'magdalena', 'value': 'magdalena'},
                    {'label': 'meta', 'value': 'meta'},
                    {'label': 'narino', 'value': 'narino'},
                    {'label': 'norte de santander', 'value': 'norte de santander'},
                    {'label': 'putumayo', 'value': 'putumayo'},
                    {'label': 'quindio', 'value': 'quindio'},
                    {'label': 'risaralda', 'value': 'risaralda'},
                    {'label': 'san andres', 'value': 'san andres'},
                    {'label': 'santander', 'value': 'santander'},
                    {'label': 'sucre', 'value': 'sucre'},
                    {'label': 'tolima', 'value': 'tolima'},
                    {'label': 'valle del cauca', 'value': 'valle del cauca'},
                    {'label': 'vaupes', 'value': 'vaupes'},
                    {'label': 'vichada', 'value': 'vichada'}
                ]
>>>>>>> d17ec26a8dd76b1ca1502eb23dd585e8b5ba8e00

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
<<<<<<< HEAD
crime_input = dbc.FormGroup(
    [
        dbc.Label("Crimen:", html_for="crime_dropdown"),
        dcc.Dropdown(
            id='crime_dropdown',
            options= crimes,
            value="260"
=======


department_input = dbc.FormGroup(
    [
        dbc.Label("Departamento:", html_for="department_dropdown"),
        dcc.Dropdown(
            id='department_dropdown',
            options= departments_dd,
            value='antioquia'
>>>>>>> d17ec26a8dd76b1ca1502eb23dd585e8b5ba8e00
        )
    ]
)

<<<<<<< HEAD
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
=======
dias_condena_input = dbc.FormGroup(
    [
        dbc.Label("Días condena:", html_for="dias_condena_slider-container"),
        html.Div(id='dias_condena_slider-container'),
        dbc.Input(type="number", min=0, max=10000, value="100", step=1, id="dias_condena_text")

    ]
)

poblacion_input = dbc.FormGroup(
    [
        dbc.Label("Población (Millones):", html_for="poblacion_text"),
        html.Div(id='poblacion_slider-container'),
        dbc.Input(type="number", min=0, max=100, value="1", step=0.1, id="poblacion_text")

    ]
)
jail_switch = dbc.FormGroup(
    [
        dbc.Checklist(
            options=[
                {"label": "Carcel", "value": 1},
            ],
            value=[],
            id="jail_toogle_survival",
>>>>>>> d17ec26a8dd76b1ca1502eb23dd585e8b5ba8e00
            switch=True,
        ),
    ]
)

<<<<<<< HEAD
=======
cluster_input = dbc.FormGroup(
    [
        dbc.Label("Cluster 2:", html_for="cluster2_survival_text"),
        html.Div(id='cluster2_survival_slider-container'),
        dbc.Input(type="number", min=0, max=9, value="0", step=1, id="cluster2_survival_text")

    ]
)

>>>>>>> d17ec26a8dd76b1ca1502eb23dd585e8b5ba8e00
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
<<<<<<< HEAD
                        crime_input,
                        intento_switch,
                        calificado_switch,
                        agravado_switch
=======
                        department_input,
                        dias_condena_input,
                        poblacion_input,
                        jail_switch,
                        cluster_input,
>>>>>>> d17ec26a8dd76b1ca1502eb23dd585e8b5ba8e00

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
<<<<<<< HEAD
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
    #1.1. Get info from local model
    ##["EDAD","tentativa","agravado","calificado","educacion", "ACTIVIDADES_ESTUDIO", "ACTIVIDADES_ENSEÑANZA",
                  #"NUM_REINCIDENCIAS_ACUM", "En_Carcel","DIAS_CONDENA_ACUM_NORM","gnic_strata","pop**3"]

    '''input_array = np.array([int(age),int(events),int(education),len(studies),
                            len(teaching),len(intento),len(calificado),
                            len(agravado),weight])
    input_df = pd.DataFrame(data=input_array)
    model_result = survival_model.predict(input_df)
    print(model_result)'''
    #2. Generate scatter chart with info
    fig = go.Figure(data=go.Scatter(x=df_model.dia, y=df_model.prob))
=======
     Input('studies_toogle', 'value'),
     Input('teaching_toogle', 'value'),
     Input('department_dropdown', 'value'),
     Input('dias_condena_text', 'value'),
     Input('poblacion_text', 'value'),
     Input('jail_toogle_survival', 'value'),
     Input('cluster2_survival_text', 'value'),
     ]
)
def update_graph(age, events, education, studies, teaching,
                     department, dias_condena, poblacion,jail,cluster):

    #print(payload)
    # Generate chart:
    #1. Get Info from web service
    #url = "https://team6flaskapi.azurewebsites.net/survival"
    #requestSurvival = requests.post(url, json=payload)
    #df_model = pd.read_json(requestSurvival.text)
    #1.1. Get info from local model
    ##
    department_value = 0
    if department in gnic_data:
        department_value = 1
    input = pd.DataFrame([int(age), int(education), len(studies), len(teaching),
                                int(events), float(int(dias_condena)/360),int(department_value),
                                (float(poblacion)-3.381724814991324)**3,len(jail),int(cluster)]).T
    input.columns=["EDAD","educacion", "ACTIVIDADES_ESTUDIO", "ACTIVIDADES_ENSEÑANZA",
                "NUM_REINCIDENCIAS_ACUM", "DIAS_CONDENA_ACUM_NORM","gnic_strata","pop**3","En_Carcel","cluster_2"]
    #print(input)
    #INPUTS = [EDAD- educacion- ACTIVIDADES_ESTUDIO- ACTIVIDADES_ENSEÑANZA-
    #NUM_REINCIDENCIAS_ACUM- DIAS_CONDENA_ACUM_NORM+(DIAS/360) gnic_strata+('0-1') pop+(POBLACION_MILLONES-3.381724814991324)**3 En_Carcel cluster_2]
    model_result = survival_model.predict_survival_function(input)
    #print("model result survival: " + str(model_result))
    #2. Generate scatter chart with info
    fig = go.Figure(data=go.Scatter(x=model_result.index, y=model_result[0]))
>>>>>>> d17ec26a8dd76b1ca1502eb23dd585e8b5ba8e00
    fig.update_layout(xaxis_title ="Días",yaxis_title = "Probabilidad", title = "Probabilidad de Reincidencia en el Tiempo", width=800, height=400)
    return fig
