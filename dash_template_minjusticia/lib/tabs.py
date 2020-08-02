#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
<<<<<<< HEAD
=======
import dash_bootstrap_components as dbc
>>>>>>> d17ec26a8dd76b1ca1502eb23dd585e8b5ba8e00
import base64


#Recall app
from app import app

from lib import demographic, geographic, gender, timeanalysis, crimeanalysis

<<<<<<< HEAD
navigationTabs = html.Div(
            className = "panel-heading",
            children = [
                html.Ul(
                    className = "nav nav-tabs nav-justified",
                    children = [
                        html.Li(
                            className = "active",
                            children = [
                                html.A(
                                    **{'data-toggle': 'tab'},
                                    href="#nav-demographic",
                                    children = [
                                        "Análisis Demográfico"
                                    ]
                                ),                
                            ]
                        ),
                        html.Li(
                            children = [
                                html.A(
                                    **{'data-toggle': 'tab'},
                                    href="#nav-geographic",
                                    children = [
                                        "Análisis Geográfico"
                                    ]
                                ),                
                            ]
                        ),
                        html.Li(
                            children = [
                                html.A(
                                    **{'data-toggle': 'tab'},
                                    href="#nav-gender",
                                    children = [
                                        "Análisis Por Género"
                                    ]
                                ),                
                            ]
                        ),
                        html.Li(
                            children = [
                                html.A(
                                    **{'data-toggle': 'tab'},
                                    href="#nav-timeanalysis",
                                    children = [
                                        "Análisis de Tiempo"
                                    ]
                                ),                
                            ]
                        ),
                        html.Li(
                            children = [
                                html.A(
                                    **{'data-toggle': 'tab'},
                                    href="#nav-crimeanalysis",
                                    children = [
                                        "Análisis de Crimen"
                                    ]
                                ),                
                            ]
                        ),
                        
                    ]
                )
            ]
        )

content = html.Div(
    className = "panel-body",
    children = [
        html.Div (
            className = "tab-content",
            children = [
                html.Div(
                    id = "nav-demographic",
                    className = "tab-pane active",
                    children = [
                        html.Div(
                            className = "row",
                            children = [
                                html.Div(
                                    className = "col-md-12",
                                    children = [
                                        demographic.demographic_output
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                html.Div(
                    id = "nav-geographic",
                    className = "tab-pane",
                    children = [
                        html.Div(
                            className = "row",
                            children = [
                                html.Div(
                                    className = "col-md-12",
                                    children = [
                                        geographic.geographic_histogram
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                html.Div(
                    id = "nav-gender",
                    className = "tab-pane",
                    children = [
                        html.Div(
                            className = "row",
                            children = [
                                html.Div(
                                    className = "col-md-12",
                                    children = [
                                        gender.gender_output
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                html.Div(
                    id = "nav-timeanalysis",
                    className = "tab-pane",
                    children = [
                        html.Div(
                            className = "row",
                            children = [
                                html.Div(
                                    className = "col-md-12",
                                    children = [
                                        timeanalysis.timeanalysis_output
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                html.Div(
                    id = "nav-crimeanalysis",
                    className = "tab-pane",
                    children = [
                        html.Div(
                            className = "row",
                            children = [
                                html.Div(
                                    className = "col-md-12",
                                    children=[
                                        crimeanalysis.output_html
                                    ]
                                    
                                )
                            ]
                        )
                    ]
                )
            ]
        )
=======

tab1_content = html.Div(
    className = "container mt-3",
    children = [
        demographic.demographic_output
    ]
)

tab2_content = html.Div(
    className = "container mt-3",
    children = [
        geographic.geographic_histogram
    ]
)
tab3_content = html.Div(
    className = "container mt-3",
    children = [
        gender.gender_output
    ]
)
tab4_content = html.Div(
    className = "container mt-3",
    children = [
        timeanalysis.timeanalysis_output
    ]
)
tab5_content = html.Div(
    className = "container mt-3",
    children = [
        crimeanalysis.output_html
    ]
)

navigationTabs = dbc.Tabs(
    children = [
        dbc.Tab(tab1_content, label="Análisis Demográfico"),
        dbc.Tab(tab2_content, label="Análisis Geográfico"),
        dbc.Tab(tab3_content, label="Análisis Por Género"),
        dbc.Tab(tab4_content, label="Análisis de Tiempo"),
        dbc.Tab(tab5_content, label="Análisis de Crimen"),
>>>>>>> d17ec26a8dd76b1ca1502eb23dd585e8b5ba8e00
    ]
)
