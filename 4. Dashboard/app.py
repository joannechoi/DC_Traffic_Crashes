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

with open(r'/Users/joanne/PycharmProjects/DATA606_DCCrash/assets/xgb_regression', 'rb') as f:
    regressor = pickle.load(f)

with open(r'/Users/joanne/PycharmProjects/DATA606_DCCrash/assets/xgb_severity', 'rb') as f2:
    xgb_severity = pickle.load(f2)

# main app
app = dash.Dash()
app.layout = html.Div([
    html.Div([
        # map filters
        html.Div([
            html.Img(id='dc_flag',
                     height='130px',
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
                                     searchable=True,
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
                                     searchable=True,
                                     value=9
                                     )),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col([html.Label("Weekday:", className="control_label")]),
                dbc.Col(dcc.Dropdown(id='weekday-dropdown',
                                     className="dropdown",
                                     style={"flex-grow": "2"},
                                     options=options_weekdays,
                                     multi=True,
                                     searchable=True,
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
                                     searchable=True,
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
                                     searchable=True,
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
        html.Div([
            dbc.Col([html.H2(children='Project Summary',
                             style={"textAlign": "center"})]),

            html.Div([
                dbc.Row([dcc.Markdown('''
                    ### Overview
    
                    - 2/3 of D.C. commuters drive alone (1)
                    - Average D.C. commute is 43 minutes compared to national average of 27 minutes (2)
                    - Most number of car accidents occur during early morning around 5 AM 
                    - Car accidents are highly correlated with precipitation
                    - Major risk factors: 
                      - Weather conditions
                      - Time of day, weekday, month 
    
                    ### Machine Learning  
                    - XGBoost Algorithm was used for both predictive models
                      - [Learn more about XGBoost here!](https://machinelearningmastery.com/gentle-introduction-xgboost-applied-machine-learning/)
                    - Features: Hour of the day, Day of the week, Month, Maximum Temperature, Minimum Temperature, Temperature, Wind Chill, Heat Index, Snow, Snow Depth, Wind Speed, Wind Gust, Visibility
                      - Weather Data Dictionary: [Link](https://www.visualcrossing.com/resources/documentation/weather-data/weather-data-documentation/)
                    - Regression Model 
                      - Independent Variable: Count of accidents aggregated per day
                      - Accuracy: 81% 
                    - Classification Model
                      - Classes: Minor injuries, Major Injuries, Fatal 
                      - Accuracy: 97%   
                    
                    ### Future Updates 
    
                    - Include traffic incidents data from MD and VA
                    - Incorporate traffic volume data
                    - Improve model performance through utilizing stacked models 
                    - Continuous integration of traffic incident data to train models 
                    - 
                    
                    ### References
                    1. National Capital Region Transportation Planning Board. (2019). 2019 STATE OF THE COMMUTE SURVEY Technical Survey Report. [Link](https://www.mwcog.org/file.aspx?&A=1AAuS26tuk0qvTVF52Q7%2BD87l582VWw4yNkHhrI8JrM%3D)
                    2. Berkon, E. (2020). D.C. has some of the longest commutes in the COUNTRY. what help is available? [Link](https://www.npr.org/local/305/2020/01/24/799292338/d-c-has-some-of-the-longest-commutes-in-the-country-what-help-is-available)
                    
                    ### Github
                    Link to the project Github repository - [DC Traffic Crashes](https://github.com/joannechoi/DC_Traffic_Crashes)
                    
                    ### About Us
                    Joanne and Sam are Masters candidates at University of Maryland, Baltimore County for Data Science. 
                    
                    ''', style={"height": '950px'})]),

            ], className='mini_container'),

        ], className='pretty-container six columns'),

        # Count Based Model
        html.Div([
            dbc.Row([html.H2(children='Predict Number of Car Crashes',
                             style={"textAlign": "center"}),
                    dbc.Col(html.H4("This model will predict the number of car accidents that may occur based \
                 on the selected criteria."))]),

            html.Div([
                html.Div([
                    dbc.Row([
                        dbc.Col(html.H5(children='Hour of the Day:', style={'display': 'inline-block', 'margin-right': 20})),
                        dbc.Col(dcc.Dropdown(id='HOUR',
                                             className="dropdown",
                                             style={"width": "150px"},
                                             options=options_hours,
                                             multi=False,
                                             searchable=True,
                                             value=0), style={'display':'inline-block', 'margin-right': 20}),
                    ]),
                    dbc.Row([
                        dbc.Col(html.H5(children='Day of the Week:', style={'display': 'inline-block', 'margin-right': 20})),
                        dbc.Col(dcc.Dropdown(id='WEEKDAY',
                                             className="dropdown",
                                             style={"width": "150px"},
                                             options=options_weekdays,
                                             multi=False,
                                             searchable=True,
                                             value=0), style={'display':'inline-block', 'margin-right': 20}),

                    ]),
                    dbc.Row([
                        dbc.Col(html.H5(children='Month:', style={'display': 'inline-block', 'margin-right': 20})),
                        dbc.Col(dcc.Dropdown(id='MONTH',
                                             className="dropdown",
                                             style={"width": "150px"},
                                             options=options_months,
                                             multi=False,
                                             searchable=True,
                                             value=1
                                             ), style={'display':'inline-block', 'margin-right': 20}),
                    ]),
                ], className='sidebyside'),
                html.Div([
                    dbc.Row([
                        dbc.Col(html.H5(children='Maximum Temperature:')),
                        dbc.Col(dcc.Input(value=3, type='number', min=-100, max=100, id='max_temp'),
                                style={'display':'inline-block', 'margin-right': 20}),
                    ]),
                    dbc.Row([
                        dbc.Col(html.H5(children='Minimum Temperature:')),
                        dbc.Col(dcc.Input(value=3, type='number', min=-100, max=100, id='min_temp'),
                                style={'display':'inline-block', 'margin-right': 20}),
                    ]),
                    dbc.Row([
                        dbc.Col(html.H5(children='Temperature:')),
                        dbc.Col(dcc.Input(value=3, type='number', min=-100, max=100, id='Temperature'),
                                style={'display':'inline-block', 'margin-right': 20}),
                    ]),
                ], className='sidebyside'),
                html.Div([
                    dbc.Row([
                        dbc.Col(html.H5(children='Visibility:')),
                        dbc.Col(dcc.Input(value=3, type='number', min=0, max=10, id='Visibility'),
                                style={'display':'inline-block', 'margin-right': 20}),
                    ]),
                    dbc.Row([
                        dbc.Col(html.H5(children='Heat Index:')),
                        dbc.Col(dcc.Input(value=3, type='number', min=0, max=120, id='heat_index'),
                                style={'display':'inline-block', 'margin-right': 20}),
                    ]),
                ], className='sidebyside'),
                html.Div([
                    dbc.Row([
                        dbc.Col(html.H5(children='Snow:',
                                style={'display': 'inline-block', 'margin-right': 20})),
                        dbc.Col(dcc.Input(value=3, type='number', min=0, max=20, id='Snow'),
                                style={'display':'inline-block', 'margin-right': 20}),
                    ]),
                    dbc.Row([
                        dbc.Col(html.H5(children='Snow Depth:',
                                style={'display': 'inline-block', 'margin-right': 20})),
                        dbc.Col(dcc.Input(value=3, type='number', min=0, max=20, id='snow_depth'),
                                style={'display':'inline-block', 'margin-right': 20}),
                    ]),
                ], className='sidebyside'),
                html.Div([
                    dbc.Row([
                        dbc.Col(html.H5(children='Wind Speed:',
                                style={'display': 'inline-block', 'margin-right': 20})),
                        dbc.Col(dcc.Input(value=3, type='number', min=0, max=50, id='wind_speed'),
                                style={'display':'inline-block', 'margin-right': 20}),
                    ]),
                    dbc.Row([
                        dbc.Col(html.H5(children='Wind Gust:',
                                style={'display': 'inline-block', 'margin-right': 20})),
                        dbc.Col(dcc.Input(value=3, type='number', min=0, max=80, id='wind_gust'),
                                style={'display':'inline-block', 'margin-right': 20}),
                    ]),
                    dbc.Row([
                        dbc.Col(html.H5(children='Wind Chill:',
                                           style={'display': 'inline-block', 'margin-right': 20})),
                        dbc.Col(dcc.Input(value=3, type='number', min=-10, max=50, id='wind_chill'),
                                style={'display':'inline-block', 'margin-right': 20}),
                    ]),
                ], className='sidebyside'),
                html.Br(),
                dbc.Row([dbc.Button('Submit', id='submit-val', n_clicks=0, color="primary")]),
                html.Br(),
                dbc.Row([html.Div(id='prediction output')])

            ], className='mini_container'),

            # Classification Model
            dbc.Row([html.H2(children='Predict the Severity of Accident',
                             style={"textAlign": "center"}),
                     html.H4("This model will predict the severity of the injury that may be sustained \
                                     during an accident based on the selected criteria."),
                     ]),

            html.Div([
                html.Div([
                    dbc.Row([
                        dbc.Col(html.H5("Hour of the Day:", style={'display': 'inline-block', 'margin-right': 20})),
                        dbc.Col(dcc.Dropdown(id='HOUR1',
                                             className="dropdown",
                                             style={"width": "150px"},
                                             options=options_hours,
                                             multi=False,
                                             searchable=True,
                                             value=0), style={'display': 'inline-block', 'margin-right': 20}),
                    ]),
                    dbc.Row([
                        dbc.Col(html.H5(children='Day of the Week:', style={'display': 'inline-block', 'margin-right': 20})),
                        dbc.Col(dcc.Dropdown(id='WEEKDAY1',
                                             className="dropdown",
                                             style={"width": "150px"},
                                             options=options_weekdays,
                                             multi=False,
                                             searchable=True,
                                             value=0), style={'display': 'inline-block', 'margin-right': 20}),

                    ]),
                    dbc.Row([
                        dbc.Col(html.H5(children='Month:', style={'display': 'inline-block', 'margin-right': 20})),
                        dbc.Col(dcc.Dropdown(id='MONTH1',
                                             className="dropdown",
                                             style={"width": "150px"},
                                             options=options_months,
                                             multi=False,
                                             searchable=True,
                                             value=1), style={'display': 'inline-block', 'margin-right': 20}),
                    ]),
                ], className='sidebyside'),
                html.Div([
                    dbc.Row([
                        dbc.Col(html.H5(children='Maximum Temperature:')),
                        dbc.Col(dcc.Input(value=3, type='number', min=-100, max=100, id='max_temp1'))
                    ]),
                    dbc.Row([
                        dbc.Col(html.H5(children='Minimum Temperature:')),
                        dbc.Col(dcc.Input(value=3, type='number', min=-100, max=100, id='min_temp1'))
                    ]),
                    dbc.Row([
                        dbc.Col(html.H5(children='Temperature:')),
                        dbc.Col(dcc.Input(value=3, type='number', min=-100, max=100, id='Temperature1'))
                    ]),
                ], className='sidebyside'),
                html.Div([
                    dbc.Row([
                        dbc.Col(
                            html.H5(children='Visibility:', style={'display': 'inline-block', 'margin-right': 20})),
                        dbc.Col(dcc.Input(value=3, type='number', min=0, max=10, id='Visibility1'),
                                style={'display':'inline-block', 'margin-right': 20})
                    ]),
                    dbc.Row([
                        dbc.Col(html.H5(children='Heat Index:', style={'display': 'inline-block', 'margin-right': 20})),
                        dbc.Col(dcc.Input(value=3, type='number', min=0, max=120, id='heat_index1'),
                                style={'display':'inline-block', 'margin-right': 20})
                    ]),
                ], className='sidebyside'),
                html.Div([
                    dbc.Row([
                        dbc.Col(html.H5(children='Snow:', style={'display': 'inline-block', 'margin-right': 20})),
                        dbc.Col(dcc.Input(value=3, type='number', min=0, max=20, id='Snow1'),
                                style={'display':'inline-block', 'margin-right': 20})
                    ]),
                    dbc.Row([
                        dbc.Col(html.H5(children='Snow Depth:', style={'display': 'inline-block', 'margin-right': 20})),
                        dbc.Col(dcc.Input(value=3, type='number', min=0, max=20, id='snow_depth1'),
                                style={'display':'inline-block', 'margin-right': 20})
                    ]),
                ], className='sidebyside'),
                html.Div([
                    dbc.Row([
                        dbc.Col(html.H5(children='Wind Speed:', style={'display': 'inline-block', 'margin-right': 20})),
                        dbc.Col(dcc.Input(value=3, type='number', min=0, max=50, id='wind_speed1'),
                                style={'display':'inline-block', 'margin-right': 20})
                    ]),
                    dbc.Row([
                        dbc.Col(html.H5(children='Wind Gust:', style={'display': 'inline-block', 'margin-right': 20})),
                        dbc.Col(dcc.Input(value=3, type='number', min=0, max=80, id='wind_gust1'),
                                style={'display':'inline-block', 'margin-right': 20})
                    ]),
                    dbc.Row([
                        dbc.Col(
                            html.H5(children='Wind Chill:', style={'display': 'inline-block', 'margin-right': 20})),
                        dbc.Col(dcc.Input(value=3, type='number', min=-10, max=50, id='wind_chill1'),
                                style={'display':'inline-block', 'margin-right': 20})
                    ]),

                ], className='sidebyside'),
                html.Br(),
                dbc.Row([dbc.Button('Submit', id='submit-val1', n_clicks=0, color="primary")]),
                html.Br(),
                dbc.Row([html.Div(id='prediction output1')])

            ], className='mini_container'),

        ], className='pretty-container six columns'),

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
    State('MONTH', 'value'),
    State('max_temp', 'value'),
    State('min_temp', 'value'),
    State('Temperature', 'value'),
    State('Visibility', 'value'),
    State('heat_index', 'value'),
    State('Snow', 'value'),
    State('snow_depth', 'value'),
    State('wind_speed', 'value'),
    State('wind_gust', 'value'),
    State('wind_chill', 'value')
)
def update_output(n_clicks, HOUR, WEEKDAY, MONTH, max_temp, min_temp, Temperature, Visibility,heat_index, Snow,
                  snow_depth, wind_speed, wind_gust, wind_chill):
    x = np.array([[HOUR, WEEKDAY, MONTH, max_temp, min_temp, Temperature, Visibility, heat_index,
                   Snow, snow_depth, wind_speed, wind_gust, wind_chill]])
    prediction = regressor.predict(x)[0]
    return f'Results: Based on the selected conditions, the predicted number of car accidents is {prediction}.'


@app.callback(
    Output('prediction output1', 'children'),
    Input('submit-val1', 'n_clicks'),
    State('HOUR1', 'value'),
    State('WEEKDAY1', 'value'),
    State('MONTH1', 'value'),
    State('max_temp1', 'value'),
    State('min_temp1', 'value'),
    State('Temperature1', 'value'),
    State('Visibility1', 'value'),
    State('heat_index1', 'value'),
    State('Snow1', 'value'),
    State('snow_depth1', 'value'),
    State('wind_speed1', 'value'),
    State('wind_gust1', 'value'),
    State('wind_chill1', 'value')
)
def update_output(n_clicks, HOUR1, WEEKDAY1, MONTH1, max_temp1, min_temp1, Temperature1, Visibility1, heat_index1,
                  Snow1, snow_depth1, wind_speed1, wind_gust1, wind_chill1):
    x = np.array([[HOUR1, WEEKDAY1, MONTH1, max_temp1, min_temp1, Temperature1, Visibility1, heat_index1, Snow1,
                   snow_depth1, wind_speed1, wind_gust1, wind_chill1]])
    severity_pred = xgb_severity.predict(x)[0]
    print(severity_pred)

    if severity_pred == 0:
        severity_pred = 'Minor'
    elif severity_pred == 1:
        severity_pred = 'Major'
    elif severity_pred == 2:
        severity_pred = 'Fatal'
    else:
        severity_pred = 'Unknown'
    return f'Results: Based on the selected conditions, the predicted severity of the accident is {severity_pred}'


if __name__ == '__main__':
    app.run_server(debug=True)
