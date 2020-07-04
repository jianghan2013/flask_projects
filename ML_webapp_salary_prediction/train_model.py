import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import requests
import json


batch_data_path = "Salary_Data.csv"
model_path = 'model.pkl'

dataset = pd.read_csv(batch_data_path)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)


regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

pickle.dump(regressor, open(model_path,'wb'))