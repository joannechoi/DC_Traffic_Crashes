import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from user_input import options_years, options_wards, options_months, options_weekdays_1, options_hours
from randomforest_dccrash import fig

# load data
df = pd.read_csv('/map_data1')
mapbox_access_token = 'pk.eyJ1IjoiaGNob2k0IiwiYSI6ImNsNHUybndoYjFyYTQzY3BhenRhNXB2djEifQ.XG8Jl_2gapRFufmepYe1mw'

df_2016 = df[df["YEAR"] == 2016]
df_2017 = df[df["YEAR"] == 2017]
df_2018 = df[df["YEAR"] == 2018]
df_2019 = df[df["YEAR"] == 2019]

# main app
app = dash.Dash()
app.layout = html.Div([

    html.Div([

        html.Div([
            html.H1('Washington D.C. Car Accident Dashboard',
                    style={"textAlign": "center",
                           "display": "flex",
                           "alignItems": "center",
                           "justifyContent": "center"})
        ], className="pretty-container"),

        html.Div([
            dcc.Graph(id='map-graph', style={'padding-top': '20px',
                                             'padding-bottom': '20px'})],
            className="pretty-container"),

        html.Div([
            html.Div([
                html.H3("Filter by:",
                        className="filter"),

                html.H4("Year:",
                        className="control_label"),

                dcc.Dropdown(id='year-dropdown',
                             className="input-line",
                             style={"flex-grow": "2"},
                             options=options_years,
                             value=2016),

                html.H4("Month:",
                        className="control_label"),

                dcc.Dropdown(id='month-dropdown',
                             className="input-line",
                             style={"flex-grow": "2"},
                             options=options_months,
                             value=1),

                html.H4("Weekday:",
                        className="control_label"),

                dcc.Dropdown(id='weekday-dropdown',
                             className="input-line",
                             style={"flex-grow": "2"},
                             options=options_weekdays_1,
                             value=6),

                html.H4("Hour:",
                        className="control_label"),

                dcc.Dropdown(id='hour-dropdown',
                             className="input-line",
                             style={"flex-grow": "2"},
                             options=options_hours,
                             value=0),

                html.H4("Ward:",
                        className="control_label"),

                dcc.Dropdown(id='choose-ward',
                             className="input-line",
                             style={"flex-grow": "2"},
                             options=options_wards,
                             searchable=False,
                             value="Ward 1"),

            ], className="basic-container-column twelve columns"),

            html.Div(
                children=[
                    html.Iframe(
                        src="/Users/joanne/PycharmProjects/DATA606_DCCrash/venv/assets/featureimportance-bar.html",
                        style={"height": "1067px", "width": "100%"},)
            ], className="pretty-container"),

        ], className="pretty-container three columns"),

    ], className="basic-container")

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
    if year == 2016:
        df2 = df_2016[(df_2016['WARD'] == ward)
                      & (df_2016['MONTH'] == month)
                      & (df_2016['WEEKDAY'] == weekday)
                      & (df_2016['HOUR'] == hour)]
    elif year == 2017:
        df2 = df_2017[(df_2017['WARD'] == ward)
                      & (df_2017['MONTH'] == month)
                      & (df_2017['WEEKDAY'] == weekday)
                      & (df_2017['HOUR'] == hour)]
    elif year == 2018:
        df2 = df_2018[(df_2018['WARD'] == ward)
                      & (df_2018['MONTH'] == month)
                      & (df_2018['WEEKDAY'] == weekday)
                      & (df_2018['HOUR'] == hour)]
    elif year == 2019:
        df2 = df_2019[(df_2019['WARD'] == ward)
                      & (df_2019['MONTH'] == month)
                      & (df_2019['WEEKDAY'] == weekday)
                      & (df_2019['HOUR'] == hour)]

    return {
        "data": [
            {"type": "scattermapbox",
             "lat": df2['LATITUDE'],
             "lon": df2['LONGITUDE'],
             "mode": "markers",
             "marker": {"sizemin": 2,
                        "color": "#FF0000",
                        "opacity": 1},
             "text": df2['ADDRESS']}],
        "layout": dict(
            autosize=True,
            height=500,
            font=dict(color="#485C6E"),
            titlefont=dict(color="#485C6E", size='14'),
            margin=dict(l=35, r=35, b=35, t=45),
            hovermode="closest",
            title=f"Car Accidents in Washington D.C.",
            legend=dict(font=dict(size=10), orientation='h'),
            mapbox=dict(
                accesstoken=mapbox_access_token,
                style="streets",
                center=dict(lon=-77.03722, lat=38.90805),
                zoom=11))}

if __name__ == '__main__':
    app.run_server(debug=True)
