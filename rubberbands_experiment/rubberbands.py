# import libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# import dataset
dataset = pd.read_csv("rubberbands_experiment/rubberbands.csv")
X = dataset.iloc[:, 0].values.reshape(-1, 1)
y = dataset.iloc[:, 1].values

# create polynomial regression model
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(X)

# create linear regression model
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_poly, y)

test_dataset = pd.read_csv("rubberbands_experiment/test_set.csv")
X_test = test_dataset.iloc[:, 0].values.reshape(-1, 1)
y_test = test_dataset.iloc[:, 1].values * 100

from sklearn.metrics import r2_score
print(r2_score(y_test, lin_reg.predict(poly_reg.fit_transform(X_test))))