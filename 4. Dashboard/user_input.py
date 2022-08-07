import pandas as pd

options_months = [
    {'label': 'January', 'value': 1},
    {'label': 'February', 'value': 2},
    {'label': 'March', 'value': 3},
    {'label': 'April', 'value': 4},
    {'label': 'May', 'value': 5},
    {'label': 'June', 'value': 6},
    {'label': 'July', 'value': 7},
    {'label': 'August', 'value': 8},
    {'label': 'September', 'value': 9},
    {'label': 'October', 'value': 10},
    {'label': 'November', 'value': 11},
    {'label': 'December', 'value': 12}]

options_years = [
    {"label": "2016", "value": 2016},
    {"label": "2017", "value": 2017},
    {"label": "2018", "value": 2018},
    {"label": "2019", "value": 2019}
]

options_wards = [
    {"label": "Ward 1", "value": "Ward 1"},
    {"label": "Ward 2", "value": "Ward 2"},
    {"label": "Ward 3", "value": "Ward 3"},
    {"label": "Ward 4", "value": "Ward 4"},
    {"label": "Ward 5", "value": "Ward 5"},
    {"label": "Ward 6", "value": "Ward 6"},
    {"label": "Ward 7", "value": "Ward 7"},
    {"label": "Ward 8", "value": "Ward 8"}
]

options_weekdays = [
    {"label": "Sunday", "value": 6},
    {"label": "Monday", "value": 0},
    {"label": "Tuesday", "value": 1},
    {"label": "Wednesday", "value": 2},
    {"label": "Thursday", "value": 3},
    {"label": "Friday", "value": 4},
    {"label": "Saturday", "value": 5}
]

options_hours = [
    {"label": "12AM", "value": 0},
    {"label": "1AM", "value": 1},
    {"label": "2AM", "value": 2},
    {"label": "3AM", "value": 3},
    {"label": "4AM", "value": 4},
    {"label": "5AM", "value": 5},
    {"label": "6AM", "value": 6},
    {"label": "7AM", "value": 7},
    {"label": "8AM", "value": 8},
    {"label": "9AM", "value": 9},
    {"label": "10AM", "value": 10},
    {"label": "11AM", "value": 11},
    {"label": "12PM", "value": 12},
    {"label": "1PM", "value": 13},
    {"label": "2PM", "value": 14},
    {"label": "3PM", "value": 15},
    {"label": "4PM", "value": 16},
    {"label": "5PM", "value": 17},
    {"label": "6PM", "value": 18},
    {"label": "7PM", "value": 19},
    {"label": "8PM", "value": 20},
    {"label": "9PM", "value": 21},
    {"label": "10PM", "value": 22},
    {"label": "11PM", "value": 23},
]

options_conditions = [
    {'label': 'Clear', 'value': 'Conditions_Clear'},
    {'label': 'Overcast', 'value': 'Conditions_Overcast'},
    {'label': 'Partially Cloudy', 'value': 'Conditions_Partially cloudy'},
    {'label': 'Rain', 'value': 'Conditions_Rain'},
    {'label': 'Rain - Overcast', 'value': 'Conditions_Rain, Overcast'},
    {'label': 'Rain - Partially Cloudy', 'value': 'Conditions_Rain, Partially cloudy'},
    {'label': 'Snow', 'value': 'Conditions_Snow'},
    {'label': 'Snow - Overcast', 'value': 'Conditions_Snow, Overcast'},
    {'label': 'Snow - Partially Cloudy', 'value': 'Conditions_Snow, Partially cloudy'}
]

options_precipitation = [
    {'label': 'Yes', 'value': 0},
    {'label': 'No', 'value': 1}
]

def create_dropdown_value(input):
    series = pd.Series(input)
    value = series.sort_values().unique().tolist()
    return value
