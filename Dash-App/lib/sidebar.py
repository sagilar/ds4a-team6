#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html


#Dash Bootstrap Components
import dash_bootstrap_components as dbc

#Data
import json
from datetime import datetime as dt


#Recall app
from app import app



##############################################################################
# Date Picker
##############################################################################

date_picker=dcc.DatePickerRange(
                id='date_picker',
                min_date_allowed=dt(2009, 1, 2),
                max_date_allowed=dt(2019, 12, 31),
                start_date=dt(2016,1,1).date(),
                end_date=dt(2017, 1, 1).date()
            )


#############################################################################
# Sidebar Layout
#############################################################################
sidebar=html.Div(
    [   ####################################################
        #Place the rest of Layout here
        ####################################################
        #html.H5("Select dates"),
        #date_picker,
        #html.Hr(),

    ],className='mj-sidebar'

)
