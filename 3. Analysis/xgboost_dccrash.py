from model_data import df_features, X_train_res, X_test_res, y_train_res, y_test_res
import pandas as pd
import plotly.express as px
from xgboost import XGBClassifier
import pickle

xgb = XGBClassifier(use_label_encoder=False,
                    learning_rate=0.2,
                    max_depth=6,
                    n_estimators=400,
                    eval_metric='mlogloss',
                    random_state=42)

xgb.fit(X_train_res, y_train_res)
y_pred_xgb2 = xgb.predict(X_test_res)

# Feature Importance
importances_xgb = xgb.feature_importances_

imp2 = pd.DataFrame(importances_xgb)
imp2['Features'] = df_features.columns
imp2.rename(columns={0: 'Importance'}, inplace=True)
imp2 = imp2.sort_values(by='Importance', ascending=False)
imp2 = imp2[['Features', 'Importance']]

fig_xgb = px.bar(imp2, x='Importance', y='Features',
                 color='Features', height=450, width=700,
                 orientation='h')
fig_xgb.write_html("/Users/joanne/PycharmProjects/DATA606_DCCrash/assets/featureimportance-xgb.html")

xgb_pickle = open(r'/Users/joanne/PycharmProjects/DATA606_DCCrash/assets/xgb_severity', 'wb')
pickle.dump(xgb, xgb_pickle)
xgb_pickle.close()
