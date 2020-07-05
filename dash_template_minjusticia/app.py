#######################################################
# Main APP definition.
#
# Dash Bootstrap Components used for main theme and better
# organization. 
#######################################################

import dash


external_scripts=[
    {
        'src': "https://use.fontawesome.com/591d8b1c6c.js"
    }
]

app = dash.Dash(__name__, external_scripts = external_scripts)
server = app.server

#We need this for function callbacks not present in the app.layout
app.config.suppress_callback_exceptions = True




