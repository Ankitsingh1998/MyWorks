#Day008 - Fitting a multivariate Linear Regression
"""
Multivariate Regression:
    multiple features
    y = (m1*x1) + (m2*x2) + c
    x1 = RM, x2 = LSTAT, y = MEDV
"""
from sklearn.datasets import load_boston
boston_house_data = load_boston()
import pandas as pd
df = pd.DataFrame(boston_house_data.data, columns=boston_house_data.feature_names)
df['MEDV'] = boston_house_data.target

X = df[['RM', 'LSTAT']]
Y = df['MEDV']

from sklearn.linear_model import LinearRegression
multivariate_regression = LinearRegression()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

multivariate_regression.fit(x_train, y_train)

c = multivariate_regression.intercept_
m1, m2 = multivariate_regression.coef_

#prediction
x1 = 5.5
x2 = 20
y = (m1*x1) + (m2*x2) + c
 
y_test_prediction = multivariate_regression.predict(x_test)
pd.DataFrame(y_test_prediction, y_test)

from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_test_prediction).round(2)
#Low MSE means better model - In univariate it was high so this model is better suited

#sololearn code challenge
"""
input:
    2 2
    1 0
    0 2
    2 3
"""
n, p = [int(x) for x in input('Enter 1 X 2 matrix: ').split()]
X = []
for i in range(n):
    X.append([float(x) for x in input('Enter a matrix of 2 X 2: ').split()])

y = [float(x) for x in input('Enter a matrix of 1 X 2: ').split()]

import numpy as np
X=np.array(X).reshape(n,p)
y=np.array(y)
b=np.linalg.pinv(X) @ y.transpose() 
print(np.around(b,decimals=2))


