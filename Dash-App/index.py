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



###########################################################
#
#           APP LAYOUT:
#
###########################################################

#LOAD THE DIFFERENT FILES
from lib import title, sidebar, geographic, demographic, timeanalysis, gender

#PLACE THE COMPONENTS IN THE LAYOUT
app.layout =html.Div(
    [
      title.title,
      sidebar.sidebar,
      geographic.geographic_output,
      demographic.demographic_output,
      timeanalysis.timeanalysis_output,
      gender.gender_output,
    ],
    className="mj-app", #You can also add your own css files by locating them into the assets folder
)



###############################################
#
#           APP INTERACTIVITY:
#
###############################################

###############################################################
#Load and modify the data that will be used in the app.
#################################################################
#df = pd.read_csv('Data/superstore.csv', parse_dates=['Order Date', 'Ship Date'])
df = pd.read_csv('../retomintic/Data_UpdateJune13/reincidencia11junio2020_clean.csv', parse_dates=['FECHA_INGRESO','FECHA_SALIDA','FECHA_CAPTURA'])
#/retomintic/Data_UpdateJune13$

with open('../Colombia.geo.json') as geo:
    geojson = json.loads(geo.read())


#############################################################
# SCATTER & LINE PLOT : Add sidebar interaction here
#############################################################

'''
@app.callback(
    [Output("Line", "figure"),Output("Scatter","figure"), Output("Treemap",'figure')],
    [
        Input("state_dropdown", "value"),
        Input("date_picker", "start_date"),
        Input("date_picker", "end_date")
    ],
)
def make_line_plot(state_dropdown, start_date, end_date):
    ddf=df[df['State_abbr'].isin(state_dropdown)]
    ddf = ddf[(ddf['Order Date'] >= start_date) & (ddf['Order Date'] < end_date)]

    ddf1=ddf.groupby(['Order_Month', 'State']).sum()
    ddf1=ddf1.reset_index()

    Line_fig=px.line(ddf1,x="Order_Month",y="Sales", color="State")
    Line_fig.update_layout(title='Montly Sales in selected states',paper_bgcolor="#F8F9F9")

    Scatter_fig=px.scatter(ddf, x="Sales", y="Profit", color="Category", hover_data=['State_abbr','Sub-Category','Order ID','Product Name'])
    Scatter_fig.update_layout(title='Sales vs. Profit in selected states',paper_bgcolor="#F8F9F9")

    Treemap_fig=px.treemap(ddf, path=["Category","Sub-Category","State"],values="Sales",color_discrete_sequence=px.colors.qualitative.Dark24)

    return [Line_fig, Scatter_fig, Treemap_fig]



#############################################################
# TREEMAP PLOT : Add sidebar interaction here
#############################################################



#############################################################
# MAP : Add interactions here
#############################################################

#MAP date interaction
@app.callback(
    Output("Colombia_map", "figure"),
    [
        Input("date_picker", "start_date"),
        Input("date_picker", "end_date")
    ],
)
def update_map(start_date,end_date):
    dff = df[(df['Order Date'] >= start_date) & (df['Order Date'] < end_date)] # We filter our dataset for the daterange
    dff=dff.groupby("State_abbr").sum().reset_index()
    fig_map2=px.choropleth_mapbox(dff,
        locations='State_abbr',
        color='Sales',
        geojson=geojson,
        zoom=3,
        mapbox_style="carto-positron",
        center={"lat": 37.0902, "lon": -95.7129},
        color_continuous_scale="Viridis",
        opacity=0.5,
        title='US Sales'
        )
    fig_map2.update_layout(title="US State Sales",margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="#F8F9F9", plot_bgcolor="#F8F9F9",)
    return fig_map2


#MAP click interaction

@app.callback(
    Output('state_dropdown','value'),
    [
        Input('US_map','clickData')
    ],
    [
        State('state_dropdown','value')
    ]

)
def click_saver(clickData,state):
    if clickData is None:
        raise PreventUpdate

    #print(clickData)

    state.append(clickData['points'][0]['location'])

    return state

'''












if __name__ == "__main__":
    app.run_server(debug=True,port=8050,host="0.0.0.0")
