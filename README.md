# Washington D.C. Traffic Crashes Dashboard
University of Maryland, Baltimore County 
<br>
Under the advisement of Dr. Tony Diana 

### Authors:
#### Joanne Choi
Masters candidate for Data Science at University of Maryland, Baltimore County. Experienced IT specialist with experience as Software Test Engineer for 7 years. Currently working as Data Quality Specialist at the Smithsonian Institution. As a fellow D.C. commuter, examining and understanding the traffic accidents within the district was informative and intriguing.
#### Sam Clark
Masters candidate for Data Science at the University of Maryland, Baltimore County. Experienced economic consultant focused on analytics for large litigations. Currently working as a Data Scientist at Slalom LLC.

## Background Information
- Washington DC is a major metropolitan area with commuters within D.C. as well as from Maryland and Virignia. 
- The Regional Transportation Planning Board reported that nearly two-thirds of commuters in D.C. drives alone. 
- Compared to the average American commute time of 27 minutes, DC commuters spend an average of 43 minutes getting to and from work. 

## Goals & Objectives
Develop a dashboard that will displays pertinent DC traffic accident information based on machine learning algorithms that will show likelihood of a car crash occurring based on criteria input by the user. To provide a useful tool for the workforce to help make informed decisions regarding their commute to D.C.

## Data
- DC Vehicle Collision Data from opendata.dc.gov
  - Crashes in DC (https://opendata.dc.gov/datasets/70392a096a8e431381f1f692aaa06afd_24)
  - Crash Details Table (https://opendata.dc.gov/datasets/crash-details-table)
- Weather Data from National Weather Service Forecast Office
  - Baltimore/Washington (https://w2.weather.gov/climate/local_data.php?wfo=lwx)

## Methodology & Analysis
Machine Learning Models:
- Count Base Regression
  - Random Forest Regression model
  - XGBoost Regression model
- Injury Severity Classification
    - Required SMOTE create even distribution due to highly imbalanced data among classes.
  - Random Forest Classification model
  - XGBoost Classification model

Analysis:
- XGBoost models performed better for both regression and classification models.
 - Regression Accuracy: 81%   |   Classification Accuracy: 97%
- The hour of the day was the most important features for predicting the count of accidents.
- The days of the week were the most important features for predicting the severity of the accidents.
  
## Implementation
- Dash by Plotly was used to implement the dashboard. 
