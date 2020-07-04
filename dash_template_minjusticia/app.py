#######################################################
# Main APP definition.
#
# Dash Bootstrap Components used for main theme and better
# organization. 
#######################################################

import dash


external_scripts=[
    {
        'src': "https://kit.fontawesome.com/09e110781e.js",
        'crossorigin': "anonymous"
    }
]

app = dash.Dash(__name__, external_scripts = external_scripts)
server = app.server

#We need this for function callbacks not present in the app.layout
app.config.suppress_callback_exceptions = True




