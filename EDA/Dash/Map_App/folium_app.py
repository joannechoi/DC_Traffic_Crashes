import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from user_input import options_years, options_wards, options_months

# load data
df = pd.read_csv('/Users/joanne/PycharmProjects/DATA606_DCCrash/map_data')
mapbox_access_token = 'pk.eyJ1IjoiaGNob2k0IiwiYSI6ImNsNHUybndoYjFyYTQzY3BhenRhNXB2djEifQ.XG8Jl_2gapRFufmepYe1mw'

df_2015 = df[df["YEAR"] == 2015]
df_2016 = df[df["YEAR"] == 2016]
df_2017 = df[df["YEAR"] == 2017]
df_2018 = df[df["YEAR"] == 2018]
df_2019 = df[df["YEAR"] == 2019]

# main app
app = dash.Dash()
app.layout = html.Div([

    # First Row
    html.Div([

        # Map
        html.Div([
            dcc.Graph(id='map-graph'),

            html.Div([
                dcc.Dropdown(id='month-dropdown',
                             className="input-line",
                             style={"flex-grow": "2"},
                             options=options_months,
                             searchable=False,
                             value=1),
                dcc.Dropdown(id='choose_year_map',
                             className="input-line",
                             style={"flex-grow": "2"},
                             options=options_years,
                             searchable=False,
                             value=2015),
                dcc.Dropdown(id='choose-ward',
                             className="input-line",
                             style={"flex-grow": "2"},
                             options=options_wards,
                             searchable=False,
                             value="Ward 1"),

            ], className="sidebyside"),

        ], className="map_container"),

], className="general")])

###############################################################################

@app.callback(
    Output('map-graph', 'figure'),
    [Input('month-dropdown', 'value'),
     Input('choose_year_map', 'value'),
     Input('choose-ward', 'value')])

def update_map(month, year, ward, df=df):
    if year == 2015:
        df2 = df_2015[(df_2015['WARD'] == ward) & (df_2015['MONTH'] == month)]
    elif year == 2016:
        df2 = df_2016[(df_2016['WARD'] == ward) & (df_2016['MONTH'] == month)]
    elif year == 2017:
        df2 = df_2017[(df_2017['WARD'] == ward) & (df_2017['MONTH'] == month)]
    elif year == 2018:
        df2 = df_2018[(df_2018['WARD'] == ward) & (df_2018['MONTH'] == month)]
    elif year == 2019:
        df2 = df_2019[(df_2019['WARD'] == ward) & (df_2019['MONTH'] == month)]

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
                zoom=11))
    }

if __name__ == '__main__':
    app.run_server(debug=True)