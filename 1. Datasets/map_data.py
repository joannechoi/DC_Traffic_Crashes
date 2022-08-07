import pandas as pd

df = pd.read_csv('/Users/joanne/PycharmProjects/DATA606_DCCrash/data/crash_weather_2015-2019.csv', low_memory=False)
df = df[df['TOTAL_VEHICLES'] > 0]

# cleanse data
df = df[['REPORTDATE', 'TIME', 'ADDRESS', 'LATITUDE', 'LONGITUDE', 'WARD']]
df.dropna(inplace=True)
df['DATE'] = pd.to_datetime(df['REPORTDATE'])
df = df.loc[(df['DATE'].dt.year > 2015) & (df['DATE'].dt.year < 2020)]
df['YEAR'] = pd.DatetimeIndex(df['DATE']).year
df['MONTH'] = pd.DatetimeIndex(df['DATE']).month
df['HOUR'] = pd.DatetimeIndex(df['DATE']).hour
df['WEEKDAY'] = pd.DatetimeIndex(df['DATE']).weekday

print(df['HOUR'].value_counts())
print(df.columns)
print(type(df['text']))
df.to_csv('map_data')
