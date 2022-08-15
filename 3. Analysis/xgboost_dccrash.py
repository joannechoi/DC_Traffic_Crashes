from xgboost import XGBClassifier
import pickle
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
df['MONTH'] = df['REPORTDATE'].dt.month
df['HOUR'] = df['REPORTDATE'].dt.hour
df['WEEKDAY'] = df['REPORTDATE'].dt.dayofweek

print(df['WEEKDAY'])

# select targets and feature variables
targets = ['MINORINJURIES_DRIVER', 'MAJORINJURIES_DRIVER', 'FATAL_DRIVER']
features = ["HOUR", "WEEKDAY", "MONTH", "Maximum Temperature", "Minimum Temperature", "Temperature",
            "Visibility", "Heat Index", "Snow", "Snow Depth", "Wind Speed", "Wind Gust", "Wind Chill",]

df1 = df[(df['MINORINJURIES_DRIVER'] > 0) | (df['MAJORINJURIES_DRIVER'] > 0) | (df['FATAL_DRIVER'] > 0)]
label_df = df1[['MINORINJURIES_DRIVER', 'MAJORINJURIES_DRIVER', 'FATAL_DRIVER']]

label_df.loc[label_df['MINORINJURIES_DRIVER'] > 0, ['Severity']] = 0
label_df.loc[label_df['MAJORINJURIES_DRIVER'] > 0, ['Severity']] = 1
label_df.loc[label_df['FATAL_DRIVER'] > 0, ['Severity']] = 2

df_features=df1[features].copy()
df_features['Wind Chill'] = df_features['Wind Chill'].fillna(0)
df_features['Heat Index'] = df_features['Heat Index'].fillna(0)
df_features['Wind Gust'] = df_features['Wind Gust'].fillna(0)

# set and split train/test data
y = label_df['Severity']
X = df_features

# fix the imbalance in data
sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X, y)

# rerun random forest with best parameters
X_train_res, X_test_res, y_train_res, y_test_res = train_test_split(X_res, y_res, test_size=0.3, random_state=42)

xgb = XGBClassifier(use_label_encoder=False,
                    learning_rate=0.2,
                    max_depth=6,
                    n_estimators=400,
                    eval_metric='mlogloss',
                    random_state=42)

xgb.fit(X_train_res, y_train_res)

xgb_pickle = open(r'/Users/joanne/PycharmProjects/DATA606_DCCrash/assets/xgb_severity', 'wb')
pickle.dump(xgb, xgb_pickle)
xgb_pickle.close()
