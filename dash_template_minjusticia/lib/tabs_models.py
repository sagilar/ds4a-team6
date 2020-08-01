#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import base64


#Recall app
from app import app

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
    ]
)
