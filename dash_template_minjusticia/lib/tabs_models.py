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

<<<<<<< HEAD
from lib import survival, clusters

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
                                    href="#nav-survival",
                                    children = [
                                        "Modelo de Supervivencia"
                                    ]
                                ),
                            ]
                        ),
                        html.Li(
                            children = [
                                html.A(
                                    **{'data-toggle': 'tab'},
                                    href="#nav-clusters",
                                    children = [
                                        "Modelos de Clustering"
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
                    id = "nav-survival",
                    className = "tab-pane active",
                    children = [
                        html.Div(
                            className = "row",
                            children = [
                                html.Div(
                                    className = "col-md-12",
                                    children = [
                                        survival.formLayout
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                html.Div(
                    id = "nav-clusters",
                    className = "tab-pane",
                    children = [
                        html.Div(
                            className = "row",
                            children = [
                                html.Div(
                                    className = "col-md-12",
                                    children = [
                                        clusters.formLayout
                                    ]
                                )
                            ]
                        )
                    ]
                ),
            ]
        )
=======
from lib import survival, clusters, segmentacion


tab1_content = html.Div(
    className = "container mt-3",
    children = [
        survival.formLayout
    ]
)
tab2_content = html.Div(
    className = "container mt-3",
    children = [
        clusters.formLayout
    ]
)
tab3_content = html.Div(
    className = "container mt-3",
    children = [
        segmentacion.formLayout
    ]
)

navigationTabs = dbc.Tabs(
    children = [
        dbc.Tab(tab1_content, label="Modelo de Supervivencia"),
        dbc.Tab(tab2_content, label="Modelos de Clustering"),
        dbc.Tab(tab3_content, label="Modelo de Segmentación"),
>>>>>>> d17ec26a8dd76b1ca1502eb23dd585e8b5ba8e00
    ]
)
