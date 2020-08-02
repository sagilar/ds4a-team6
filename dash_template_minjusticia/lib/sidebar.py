#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html

#Recall app
from app import app

sidebar = html.Aside(
        children=[
            html.Div(
                id="sidebar",
                className="nav-collapse",
                children=[
                    html.Ul(
                        className="sidebar-menu",
                        id="nav-accordion",
                        children=[
                            html.Li(
                                className="mt",
                                children=[
                                    dcc.Link(
<<<<<<< HEAD
                                        className="active",
=======
>>>>>>> d17ec26a8dd76b1ca1502eb23dd585e8b5ba8e00
                                        href="dashboard",
                                        children=[
                                            html.I(
                                                className="fa fa-dashboard"
                                                
                                            ),
                                            html.Span(
                                                "Dashboard"
                                            )

                                        ]
                                    )
                                ]
                            ),
                            html.Li(
                                className="mt",
                                children=[
                                    dcc.Link(
                                        href="dataexploration",
                                        children=[
                                            html.I(
                                                className="fa fa-book"
                                                
                                            ),
                                            html.Span(
                                                "Exploración de Datos"
                                            )

                                        ]
                                    )
                                ]
                            ),
                            html.Li(
                                className="mt",
                                children=[
                                    dcc.Link(
                                        href="models",
                                        children=[
                                            html.I(
                                                className="fa fa-tasks"
                                                
                                            ),
                                            html.Span(
                                                "Modelos"
                                            )

                                        ]
                                    )
                                ]
                            ),
<<<<<<< HEAD
                            html.Li(
                                className="mt",
                                children=[
                                    html.A(
                                        href="dashboard",
                                        children=[
                                            html.I(
                                                className="fa fa-envelope"
                                                
                                            ),
                                            html.Span(
                                                "Recomendaciones"
                                            )

                                        ]
                                    )
                                ]
                            ),
                            
=======
>>>>>>> d17ec26a8dd76b1ca1502eb23dd585e8b5ba8e00
                        ]
                    )
                ]
            )
        ]
    )
