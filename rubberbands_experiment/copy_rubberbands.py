# import libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# import dataset
dataset = pd.read_csv("rubberbands_experiment/copy_rubberbands.csv")
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

X_max = max(100, X.max())
X_grid = np.arange(min(X), X_max, 0.1).reshape(-1, 1)

print(lin_reg.coef_)
print(lin_reg.intercept_)

plt.scatter(X, y, color="red", s=5)
plt.plot(X_grid, lin_reg.predict(poly_reg.transform(X_grid)), color="blue")

plt.title("Polynomial Regression")
plt.xlabel("Angle (deg)")
plt.xticks(np.arange(0, X_max, 10))
plt.ylabel("Horizontal Distance (m")

plt.show()