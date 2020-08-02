#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html

#Recall app
from app import app


card1 = html.Div(
    className = "col-md-4 col-sm-4 mb",
    children = [
        html.Div(
            className = "grey-panel pn donut-chart",
            children = [
                html.Div(
                    className = "grey-header",
                    children=[
                        html.H5(
<<<<<<< HEAD
                            "Información por Género"
=======
                            "Tasa de Reincidencia"
>>>>>>> d17ec26a8dd76b1ca1502eb23dd585e8b5ba8e00
                        )
                    ]
                ),
                html.Div(
                    className = "row",
                    children = [
                        html.Div(
                            className = "col-sm-6 col-xs-6 goleft",
                            children = [
                                html.P(
                                    children = [
                                        "Porcentaje",
                                        html.Br(),
<<<<<<< HEAD
                                        "Hombres: "
=======
                                       
>>>>>>> d17ec26a8dd76b1ca1502eb23dd585e8b5ba8e00
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            className = "col-sm-6 col-xs-6 goleft",
                            children = [
<<<<<<< HEAD
                                html.H2("56%")
=======
                                html.H2("50%")
>>>>>>> d17ec26a8dd76b1ca1502eb23dd585e8b5ba8e00
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)

card2 = html.Div(
    className = "col-md-4 col-sm-4 mb",
    children = [
        html.Div(
            className = "darkblue-panel pn",
            children = [
                html.Div(
                    className = "darkblue-header",
                    children=[
                        html.H5(
<<<<<<< HEAD
                            "Información por Género"
=======
                            "Hijos Menores"
>>>>>>> d17ec26a8dd76b1ca1502eb23dd585e8b5ba8e00
                        )
                    ]
                ),
                html.Div(
                    className = "row",
                    children = [
<<<<<<< HEAD
                        html.P(
                                    children = [
                                        html.B("1500"),
                                        " Hombres"
                                    ],
                                    className="mt"
                                )
=======
                        html.Div(
                            className = "col-sm-6 col-xs-6",
                            children = [
                                html.P(
                                    children = [
                                        "Tienen Hijos",
                                        html.Br(),
                                       
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            className = "col-sm-6 col-xs-6 goleft",
                            children = [
                                html.H2("79%")
                            ]
                        )
>>>>>>> d17ec26a8dd76b1ca1502eb23dd585e8b5ba8e00
                    ]
                )
            ]
        )
    ]
)

<<<<<<< HEAD
=======

>>>>>>> d17ec26a8dd76b1ca1502eb23dd585e8b5ba8e00
card3 = html.Div(
    className = "col-md-4 col-sm-4 mb",
    children = [
        html.Div(
            className = "green-panel pn",
            children = [
                html.Div(
                    className = "green-header",
                    children=[
                        html.H5(
                            "Información por Género"
                        )
                    ]
                ),
                html.Div(
                    className = "row",
                    children = [
                        html.Div(
<<<<<<< HEAD
                            className = "col-sm-6 col-xs-6 goleft",
=======
                            className = "col-sm-6 col-xs-6",
>>>>>>> d17ec26a8dd76b1ca1502eb23dd585e8b5ba8e00
                            children = [
                                html.P(
                                    children = [
                                        "Porcentaje",
                                        html.Br(),
                                        "Hombres: "
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            className = "col-sm-6 col-xs-6 goleft",
                            children = [
<<<<<<< HEAD
                                html.H2("56%")
=======
                                html.H2("90%")
>>>>>>> d17ec26a8dd76b1ca1502eb23dd585e8b5ba8e00
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)
