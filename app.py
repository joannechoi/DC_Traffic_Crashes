import pandas as pd
import numpy as np
import pickle
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from user_input import options_years, options_wards, \
    options_months, options_weekdays, options_hours, create_dropdown_value

# load data
df = pd.read_csv('/Users/joanne/PycharmProjects/DATA606_DCCrash/map_data1.csv')
mapbox_access_token = 'pk.eyJ1IjoiaGNob2k0IiwiYSI6ImNsNHUybndoYjFyYTQzY3BhenRhNXB2djEifQ.XG8Jl_2gapRFufmepYe1mw'
with open(r'/Users/joanne/PycharmProjects/DATA606_DCCrash/assets/rf_severity', 'rb') as f1:
    rf_severity = pickle.load(f1)
with open(r'/Users/joanne/PycharmProjects/DATA606_DCCrash/assets/xgb_severity', 'rb') as f2:
    xgb_severity = pickle.load(f2)

# main app
app = dash.Dash()
app.layout = html.Div([
    html.Div([
        # map filters
        html.Div([
            html.Img(id='dc_flag',
                     height='180px',
                     src='assets/Flag_of_the_District_of_Columbia.svg',
                     style={"border-radius": "20px"}),
            html.P('Use the filters below to explore the \
                    historical traffic accident data on the map'),
            dbc.Row([html.H3(children='Map Filters:')]),
            dbc.Row([
                dbc.Col(html.Label("Year:", className="control_label")),
                dbc.Col(dcc.Dropdown(id='year-dropdown',
                                     className="dropdown",
                                     style={"flex-grow": "2"},
                                     options=options_years,
                                     multi=True,
                                     searchable=False,
                                     value=2019)),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col([html.Label("Month:", className="control_label")]),
                dbc.Col(dcc.Dropdown(id='month-dropdown',
                                     className="dropdown",
                                     style={"flex-grow": "2"},
                                     options=options_months,
                                     multi=True,
                                     searchable=False,
                                     value=9)),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col([html.Label("Weekday:", className="control_label")]),
                dbc.Col(dcc.Dropdown(id='weekday-dropdown',
                                     className="dropdown",
                                     style={"flex-grow": "2"},
                                     options=options_weekdays,
                                     multi=True,
                                     searchable=False,
                                     value=0)),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col([html.Label("Hour:", className="control_label")]),
                dbc.Col(dcc.Dropdown(id='hour-dropdown',
                                     className="dropdown",
                                     style={"flex-grow": "2"},
                                     options=options_hours,
                                     multi=True,
                                     searchable=False,
                                     value=1)),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col([html.Label("Ward:", className="control_label")]),
                dbc.Col(dcc.Dropdown(id='choose-ward',
                                     className="dropdown",
                                     style={"flex-grow": "2"},
                                     options=options_wards,
                                     multi=True,
                                     searchable=False,
                                     value='Ward 5')),
            ]),
            html.Br(),
        ], className="pretty-container three columns"),

        # title
        html.Div([
            html.Div([
                html.H1('Traffic Accidents in Washington D.C.',
                        style={"textAlign": "center",
                               "display": "flex",
                               "alignItems": "center",
                               "justifyContent": "center"}),
            ], className='pretty-container'),

            # second graphic
            html.Div([
                html.H2("Car Accidents in Washington D.C. (2016-2019)",
                        style={"textAlign": "center"}),
                dcc.Graph(id='map-graph'),
            ], className="pretty-container"),

        ], className="basic-container-column twelve columns"),

    ], className='basic-container'),

    # Second Row
    html.Div([
        # Poisson/Negative Regression Model
        html.Div([
            dbc.Row([html.H3(children='Predict Number of Car Crashes',
                             style={"textAlign": "center"})]),
            html.Div([
                html.P("Describe the model here"),
            ], className='basic-container-column'),
            html.Div([
                dbc.Row([
                    dbc.Col(html.Label(children='Hour of the Day:'), width={"order": "first"}),
                    dbc.Col(dcc.Input(value=3, type='number', id='HOUR'))
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col(html.Label(children='Day of the Week:'), width={"order": "first"}),
                    dbc.Col(dcc.Input(value=3, type='number', id='WEEKDAY'))
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col(html.Label(children='Month:'), width={"order": "first"}),
                    dbc.Col(dcc.Input(value=3, type='number', id='MONTH'))
                ]),
                html.Br(),
                dbc.Row([dbc.Button('Submit', id='submit-val', n_clicks=0, color="primary")]),
                html.Br(),
                dbc.Row([html.Div(id='prediction output')])
            ], className='mini_container'),

        ], className='pretty-container six columns'),
        # Random Forest - Injury Severity Model
        html.Div([
            dbc.Row([html.H3(children='SECOND MODEL GOES HERE',
                             style={"textAlign": "center"})]),
            html.Div([
                html.P("Describe the model here"),
            ], className='basic-container-column'),
            html.Div([
                html.Div([
                    dbc.Row([
                        dbc.Col(html.Label(children='Hour of the Day:'), width={"order": "first"}),
                        dbc.Col(dcc.Input(value=3, type='number', id='HOUR1'))
                    ]),
                    html.Br(),
                    dbc.Row([
                        dbc.Col(html.Label(children='Day of the Week:'), width={"order": "first"}),
                        dbc.Col(dcc.Input(value=3, type='number', id='WEEKDAY1'))
                    ]),
                    html.Br(),
                    dbc.Row([
                        dbc.Col(html.Label(children='Month:'), width={"order": "first"}),
                        dbc.Col(dcc.Input(value=3, type='number', id='MONTH1'))
                    ]),
                ], className='sidebyside'),

                html.Br(),
                dbc.Row([dbc.Button('Submit', id='submit-val1', n_clicks=0, color="primary")]),
                html.Br(),
                dbc.Row([html.Div(id='prediction output1')]),

            ], className='mini_container'),

        ], className='pretty-container six columns'),

    ], className='basic-container'),

    # feature importance and bar chart
    html.Div([
        html.Div([
            dbc.Row([html.H3(children='Important Risk Factors for Injury Severity',
                             style={"textAlign": "center"})]),
            html.Iframe(id='importance',
                        srcDoc=open(
                            '/Users/joanne/PycharmProjects/DATA606_DCCrash/assets/featureimportance-rf.html',
                            'r').read(),
                        width='100%',
                        height=475, ),
            html.P("This chart display the influence each risk factors had \
                    on the severity of the injuries sustained during traffic accidents."),

        ], className="pretty-container six columns"),

        html.Div([
            dbc.Row([html.H3(children='TITLE PLACEHOLDER',
                             style={"textAlign": "center"})]),
            html.Iframe(id='importance2',
                        srcDoc=open(
                            '/Users/joanne/PycharmProjects/DATA606_DCCrash/assets/featureimportance-xgb.html',
                            'r').read(),
                        width='100%',
                        height=475, ),
            html.P("ADD CAPTION HERE."),
        ], className="pretty-container six columns"),

    ], className='basic-container'),

], className="general")


###############################################################################

@app.callback(
    Output('map-graph', 'figure'),
    [Input('year-dropdown', 'value'),
     Input('month-dropdown', 'value'),
     Input('weekday-dropdown', 'value'),
     Input('hour-dropdown', 'value'),
     Input('choose-ward', 'value')])
def update_map(year, month, weekday, hour, ward):
    dff = df.copy()
    dff['text'] = 'Address: ' + dff['ADDRESS'] \
                  + ' Date: ' + dff['YEAR'].astype(str) \
                  + '-' + dff['MONTH'].astype(str) + ' ' + dff['WARD']

    year_values = create_dropdown_value(year)
    month_values = create_dropdown_value(month)
    weekday_values = create_dropdown_value(weekday)
    hour_values = create_dropdown_value(hour)
    ward_values = create_dropdown_value(ward)

    dff = dff[dff['YEAR'].isin(year_values)]
    dff = dff[dff['MONTH'].isin(month_values)]
    dff = dff[dff['WEEKDAY'].isin(weekday_values)]
    dff = dff[dff['HOUR'].isin(hour_values)]
    dff = dff[dff['WARD'].isin(ward_values)]

    return {
        "data": [
            {"type": "scattermapbox",
             "lat": dff['LATITUDE'],
             "lon": dff['LONGITUDE'],
             "mode": "markers",
             "marker": {"sizemin": 2,
                        "color": "#FF0000",
                        "opacity": 1},
             "text": dff['text']}],
        "layout": dict(
            autosize=True,
            height=500,
            font=dict(color="#485C6E"),
            titlefont=dict(color="#485C6E", size='14'),
            margin=dict(l=35, r=35, b=35, t=45),
            hovermode="closest",
            legend=dict(font=dict(size=10), orientation='h'),
            mapbox=dict(
                accesstoken=mapbox_access_token,
                style="streets",
                center=dict(lon=-77.03722, lat=38.90805),
                zoom=11))}


# Count Based Model
@app.callback(
    Output('prediction output', 'children'),
    Input('submit-val', 'n_clicks'),
    State('HOUR', 'value'),
    State('WEEKDAY', 'value'),
    State('MONTH', 'value')
)
def update_output(n_clicks, HOUR, WEEKDAY, MONTH):
    x = np.array([[HOUR, WEEKDAY, MONTH]])
    prediction = regressor.predict(x)[0]
    return f'The predicted number of car accidents is {prediction}.'


'''
# Injury Severity Model 
@app.callback(
    Output('textarea-example-output', 'children'),
    [Input('weather-dropdown', 'value'),
     Input('precipitation-dropdown', 'value'),
     Input('month-dropdown1', 'value'),
     Input('hour-dropdown1', 'value'),
     Input('weekday-dropdown1', 'value')])
def rf_severity(conditions, precipitation, month, hour, weekday):
    severity_pred = rf.predict(conditions, precipitation, month, hour, weekday)
    if severity_pred == 0:
        severity = 'Major'
    elif severity_pred == 1:
        severity = 'Minor'
    elif severity_pred == 2:
        severity = 'Fatal'
    else:
        severity = 'Unknown'
    return 'Based on the selected conditions, the predicted severity of the accident is {}'.format(severity)
'''

if __name__ == '__main__':
    app.run_server(debug=True)
