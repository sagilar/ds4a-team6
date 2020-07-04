#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html

#Recall app
from app import app
from lib import rightpanel, cards, geographic

layout = html.Section(
    id="main-content",
    children = [
        html.Section(
                    className = "wrapper site-min-height",
                    children = [
                        html.Div(
                            className = "row mt mb",
                            children = [
                                html.Div(
                                    className = "col-lg-12",
                                    children = [
                                        html.H3(
                                            children = [
                                                
                                                html.I(
                                                    className = "fa fa-tasks"
                                                ),
                                                " Modelo 1",
                                            ]
                                        ),
                                        html.Br(),
                                        html.Div(
                                            className= "col-lg-4 col-md-4 col-sm-12",
                                            children=[
                                                html.Div(
                                                    className = "dmbox",
                                                    children = [
                                                        html.Div(
                                                            className = "service-icon",
                                                            children = [
                                                                html.A(
                                                                href="/",
                                                                children = [
                                                                    html.I(
                                                                        className = "dm-icon fa fa-question fa-3x"
                                                                    )
                                                                ]
                                                                )
                                                            ]
                                                        ),
                                                        html.H4(
                                                            "Modelo de Supervivencia"
                                                        ),
                                                        html.P(
                                                            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.."
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
    ]
) 