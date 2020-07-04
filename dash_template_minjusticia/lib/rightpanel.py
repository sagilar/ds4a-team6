#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html

#Recall app
from app import app

rightpanel= html.Div(
    className = "col-lg-3 ds",
    children = [
        html.Div(
            className = "donut-main",
            children= [
                html.H4(
                    "Datos Demográficos"
                )
            ]
        )
    ]
)