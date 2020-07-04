#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px

#Dash Bootstrap Components
import dash_bootstrap_components as dbc

#Data
import math
import numpy as np
import datetime as dt
import pandas as pd
import json

#Recall app
from app import app
from lib import rightpanel, cards, geographic

content = html.Section(
    id="main-content",
    children = [
        html.Section(
            className = "wrapper",
            children = [
                html.Div(
                    className = "row",
                    children = [
                        html.Div(
                            className = "col-lg-9 main-chart",
                            children = [
                                html.Div(
                                    children = [
                                        html.Div(
                                            className = "border-head",
                                            children= [
                                                html.H3(
                                                    "Información Geográfica"
                                                )
                                            ]
                                        ),
                                        geographic.geographic_output,
                                        html.Div(
                                            className = "row mt",
                                            children= [
                                                cards.card1,
                                                cards.card2,
                                                cards.card3
                                            ]
                                        ),
                                        
                                        
                                    ]
                                )
                            ]
                        ),
                        rightpanel.rightpanel
                    ]
                )
            ]
        )
    ]
) 