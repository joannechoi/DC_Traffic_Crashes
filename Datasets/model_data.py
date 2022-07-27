import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

# import data
df = pd.read_csv('/Users/joanne/PycharmProjects/DATA606_DCCrash/data/crash_weather_2015-2019.csv',
                 low_memory=False)

# filter out accidents with vehicles
df = df[df['TOTAL_VEHICLES'] > 0]

# transform date data
df['REPORTDATE'] = pd.to_datetime(df['REPORTDATE'], errors='coerce')
df = df.loc[(df['REPORTDATE'].dt.year > 2015) & (df['REPORTDATE'].dt.year < 2020)]
# Extract year, month, day, hour and weekday
df['YEAR'] = df['REPORTDATE'].dt.year
df['MONTH'] = df['REPORTDATE'].dt.strftime('%b')
df['HOUR'] = df['REPORTDATE'].dt.hour
df['WEEKDAY'] = df['REPORTDATE'].dt.strftime('%a')

# select targets and feature variables
targets = ['MINORINJURIES_DRIVER', 'MAJORINJURIES_DRIVER', 'FATAL_DRIVER']
features = ['Temperature', 'Visibility', 'Cloud Cover', 'Wind Speed',
            'Precipitation', 'Conditions', 'MONTH', 'HOUR', 'WEEKDAY']

df1 = df[(df['MINORINJURIES_DRIVER'] > 0) | (df['MAJORINJURIES_DRIVER'] > 0) | (df['FATAL_DRIVER'] > 0)]
label_df = df1[['MINORINJURIES_DRIVER', 'MAJORINJURIES_DRIVER', 'FATAL_DRIVER']]

label_df.loc[label_df['MINORINJURIES_DRIVER'] > 0, ['Severity']] = 0
label_df.loc[label_df['MAJORINJURIES_DRIVER'] > 0, ['Severity']] = 1
label_df.loc[label_df['FATAL_DRIVER'] > 0, ['Severity']] = 2

df_features = df1[features].copy()
df_features = pd.get_dummies(df_features)

hour_dummy = pd.get_dummies(df_features['HOUR'])
hour_dummy.columns = ['Hour_0', 'Hour_1', 'Hour_2', 'Hour_3', 'Hour_4', 'Hour_5', 'Hour_6', 'Hour_7', 'Hour_8',
                      'Hour_9', 'Hour_10', 'Hour_11', 'Hour_12', 'Hour_13', 'Hour_14', 'Hour_15', 'Hour_16', 'Hour_17',
                      'Hour_18', 'Hour_19', 'Hour_20', 'Hour_21', 'Hour_22', 'Hour_23']
df_features = pd.concat([df_features, hour_dummy], axis=1)
df_features.drop(columns='HOUR', inplace=True)

# set and split train/test data
y = label_df['Severity']
X = df_features
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# fix the imbalance in data
sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X, y)

# rerun random forest with best parameters
X_train_res, X_test_res, y_train_res, y_test_res = train_test_split(X_res, y_res, test_size=0.3, random_state=42)