# Dash_App.py
### Import Packages ########################################
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import numpy as np
import pickle


### Setup ###################################################
app = dash.Dash(__name__)
app.title = 'Washington DC Car Crash Prediction Dashboard'
server = app.server


### load ML model ###########################################
with open(r'/Users/samuelclark/Documents/UMBC Data Science /Capstone/model/rfr_model.pickle', 'rb') as f:
    regressor = pickle.load(f)
    
##joannes model
    
    
### App Layout ###############################################
app.layout = html.Div([
    dbc.Row([html.H3(children='Predict Number of Car Crashes')]),
    dbc.Row([
        dbc.Col(html.Label(children='Hour of the Day:'), width={"order": "first"}),
        dbc.Col(dcc.Input(value= 3, type='number', id='HOUR')) 
    ]),
    dbc.Row([
        dbc.Col(html.Label(children='Day of the Week:'), width={"order": "first"}),
        dbc.Col(dcc.Input(value = 3, type='number', id='WEEKDAY')) 
    ]),
    dbc.Row([
        dbc.Col(html.Label(children='Month):'), width={"order": "first"}),
        dbc.Col(dcc.Input(value = 3, type='number', id='MONTH')) 
    ]),
    dbc.Row([
       dbc.Col(html.Label(children='Maximum Temperature):'), width={"order": "first"}),
       dbc.Col(dcc.Input(value = 3, type='number', id='Maximum Temperature'))     
    ]),
    dbc.Row([
       dbc.Col(html.Label(children='Minimum Temperature):'), width={"order": "first"}),
       dbc.Col(dcc.Input(value = 3, type='number', id='Minimum Temperature'))     
    ]),
    dbc.Row([
       dbc.Col(html.Label(children='Temperature):'), width={"order": "first"}),
       dbc.Col(dcc.Input(value = 3, type='number', id='Temperature'))     
    ]),
    dbc.Row([
       dbc.Col(html.Label(children='Wind Chill):'), width={"order": "first"}),
       dbc.Col(dcc.Input(value = 3, type='number', id='Wind Chill'))     
    ]),
    dbc.Row([
       dbc.Col(html.Label(children='Heat Index):'), width={"order": "first"}),
       dbc.Col(dcc.Input(value = 3, type='number', id='Heat Index'))     
    ]),
    dbc.Row([
       dbc.Col(html.Label(children='Snow):'), width={"order": "first"}),
       dbc.Col(dcc.Input(value = 3, type='number', id='Snow'))     
    ]),
    dbc.Row([
       dbc.Col(html.Label(children='Snow Depth):'), width={"order": "first"}),
       dbc.Col(dcc.Input(value = 3, type='number', id='Snow Depth'))     
    ]),
    dbc.Row([
       dbc.Col(html.Label(children='Wind Speed):'), width={"order": "first"}),
       dbc.Col(dcc.Input(value = 3, type='number', id='Wind Speed'))     
    ]),
    dbc.Row([
       dbc.Col(html.Label(children='Wind Gust):'), width={"order": "first"}),
       dbc.Col(dcc.Input(value = 3, type='number', id='Wind Gust'))     
    ]),
    dbc.Row([
       dbc.Col(html.Label(children='Visibility):'), width={"order": "first"}),
       dbc.Col(dcc.Input(value = 3, type='number', id='Visibility'))     
    ]),
    dbc.Row([dbc.Button('Submit', id='submit-val', n_clicks=0, color="primary")]),
    html.Br(),
    dbc.Row([html.Div(id='prediction output')])
    
    
    ], style = {'padding': '0px 0px 0px 150px', 'width': '50%'})



### Callback to produce the prediction ######################### 
@app.callback(
    Output('prediction output', 'children'),
    Input('submit-val', 'n_clicks'),
    State('HOUR', 'value'),
    State('WEEKDAY', 'value'),
    State('MONTH', 'value'),
    State('Maximum Temperature', 'value'),
    State('Minimum Temperature', 'value'),
    State('Temperature', 'value'),
    State('Wind Chill', 'value'),
    State('Heat Index', 'value'),
    State('Snow', 'value'),
    State('Snow Depth', 'value'),
    State('Wind Speed', 'value'),
    State('Wind Gust', 'value'),
    State('Visibility', 'value')

)
   
def update_output(n_clicks, HOUR, WEEKDAY, MONTH, ):    
    x = np.array([[HOUR, WEEKDAY, MONTH]])
    prediction = regressor.predict(x)[0]
    return f'The predicted number of car accidents is {prediction}.'### Run the App ###############################################
if __name__ == '__main__':
    app.run_server(debug=True)
    
