#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px

#Data 
import math
import numpy as np
import datetime as dt
import pandas as pd
import json

#Recall app
from app import app



###########################################################
#
#           APP LAYOUT:
#
###########################################################

#LOAD THE DIFFERENT FILES
from lib import header, sidebar, main

#PLACE THE COMPONENTS IN THE LAYOUT
app.layout =html.Div(
    [ 
      header.header,
      sidebar.sidebar,
      main.content
    ],
    id="container"
)

 
    
###############################################   
#
#           APP INTERACTIVITY:
#
###############################################

###############################################################
#Load and modify the data that will be used in the app.
#################################################################




#############################################################
# LINE PLOT : Add sidebar interaction here
#############################################################



#############################################################
# PROFITS BY CATEGORY : Add sidebar interaction here
#############################################################



#############################################################
# TREEMAP PLOT : Add sidebar interaction here
#############################################################



#############################################################
# MAP : Add interactions here
#############################################################

#MAP date interaction



#MAP click interaction





    





                                                 
           
        

if __name__ == "__main__":
    app.run_server(debug=True, port=9050)
