import pandas as pd

df = pd.read_csv('/Users/joanne/Documents/School/DATA606/Data/crash_weather_2015-2019.csv', low_memory=False)
df = df[df['TOTAL_VEHICLES'] > 0]

# cleanse data
df = df[['DATE', 'TIME', 'ADDRESS', 'LATITUDE', 'LONGITUDE', 'WARD']]
df.dropna(inplace=True)
df['DATE'] = pd.to_datetime(df['DATE'])
df['YEAR'] = pd.DatetimeIndex(df['DATE']).year
df['MONTH'] = pd.DatetimeIndex(df['DATE']).month
df.to_csv('map_data')


def df_ward(df, ward):

    if ward == "Ward 1":
        df = df[df["WARD"] == "Ward 1"]
        color = "#91BCCE" # blue
    elif ward == "Ward 2":
        df = df[df["WARD"] == "Ward 2"]
        color = "#ff7f0e" # orange
    elif ward == "Ward 3":
        df = df[df["WARD"] == "Ward 3"]
        color = "#DE97A5" # pink
    elif ward == "Ward 4":
        df = df[df["WARD"] == "Ward 4"]
        color = "#E6E26A" # yellow
    elif ward == "Ward 5":
        df = df[df["WARD"] == "Ward 5"]
        color = "#8BE66A" # green
    elif ward == "Ward 6":
        df = df[df["WARD"] == "Ward 6"]
        color = 'A58DEB' # purple
    elif ward == "Ward 7":
        df = df[df["WARD"] == "Ward 7"]
        color = 'FFBE0D' # darker yellow
    elif ward == "Ward 8":
        df = df[df["WARD"] == "Ward 8"]
        color = "E66A6A"
    else:
        color = "#535E7A"
    return df, color