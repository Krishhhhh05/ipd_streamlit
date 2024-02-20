import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pickle

# import data
my_df = pd.read_csv("InputData.csv")
# print(my_df)
#independant columns
# Assuming X_train and y_train are your training data
xg_reg = xgb.XGBRegressor()

X_train, X_test, y_train, y_test = train_test_split(my_df.drop(['TrueRiskTol', 'Unnamed: 0'], axis=1), my_df['TrueRiskTol'], test_size=0.2, random_state=42)

xg_reg.fit(X_train, y_train)
pickle.dump(xg_reg,open('xg_reg.pkl','wb'))


# age = 47
# edu = 2
# married = 1
# kids = 0
# lifecl = 2
# occat = 1
# income = 56443.744181
# risk = 3
# wsaved = 1
# spendmor = 5
# networth = 352641.71130

# # Get the column names from X_train excluding 'TrueRiskTol'
# new_columns = [col for col in X_train.columns if col != 'TrueRiskTol' and col != 'Unnamed: 0']


# # Create new DataFrame without 'TrueRiskTol' column
# new_data_values = [[age, edu, married, kids, lifecl, occat, income, risk, wsaved, spendmor, networth]]
# new_data = pd.DataFrame(new_data_values, columns=new_columns)

# # Predict using the new data
# predicted_risk_tolerance = xg_reg.predict(new_data)
# print(predicted_risk_tolerance)