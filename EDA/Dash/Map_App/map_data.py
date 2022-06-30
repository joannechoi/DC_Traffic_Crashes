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