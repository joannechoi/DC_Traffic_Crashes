from model_data import df_features, X_train_res, X_test_res, y_train_res, y_test_res
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
import pickle

rf = RandomForestClassifier(n_estimators=400,
                            criterion='entropy',
                            max_depth=8,
                            max_features='log2',
                            random_state=42)

rf.fit(X_train_res, y_train_res)
y_pred_res = rf.predict(X_test_res)

# Feature Importance
importances = rf.feature_importances_

imp = pd.DataFrame(importances)
imp['Features'] = df_features.columns
imp.rename(columns={0: 'Importance'}, inplace=True)
imp = imp.sort_values(by='Importance', ascending=False)
imp = imp[['Features', 'Importance']]

fig = px.bar(imp, x='Importance', y='Features',
             color='Features', height=450, width=700,
             orientation='h')
fig.write_html("/Users/joanne/PycharmProjects/DATA606_DCCrash/assets/featureimportance-rf.html")

rf_pickle = open(r'/Users/joanne/PycharmProjects/DATA606_DCCrash/assets/rf_severity', 'wb')
pickle.dump(rf, rf_pickle)
rf_pickle.close()
