#Day007 - Fitting a univariate Linear Regression
from sklearn.datasets import load_boston
boston_house_data = load_boston()
import pandas as pd
df = pd.DataFrame(boston_house_data.data, columns=boston_house_data.feature_names)
df['MEDV'] = boston_house_data.target
"""
scikit-learn:
    To perform Linear Regression on RM and MEDV.
    MEDV = m*(RM) + c
    model requires --> a 2D feature matrix(X, 2D array or a pandas dataframe)
    and a 1D target array(Y).
"""
X = df[['RM']] #pandas DataFrame --> since features requires 2D array
X.shape
Y = df['MEDV'] #pandas Series --> labels can be 1D array
Y.shape

from sklearn.linear_model import LinearRegression #importing the class
regression_model = LinearRegression() #creating an instance of the class

from sklearn.model_selection import train_test_split
#training and testing our model to ensure its performance
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

#Now, fitting the model
regression_model.fit(x_train, y_train)
m = regression_model.coef_
c = regression_model.intercept_

import numpy as np
RM_data = np.array([[6.5]])
RM_data.shape
regression_model.predict(RM_data) #Method 1

x = 6.5
y = m*x + c
print(y[0].round(2)) #Method 2

#predicting the y_test data and comparing
y_test_prediction = regression_model.predict(x_test)
y_test_prediction.shape
type(y_test_prediction)
y_test.shape

#Evaluating the model
#Residual
#Residual for tested dataset
import matplotlib.pyplot as plt
plt.scatter(x_test, y_test, label='Testing data')
plt.plot(x_test, y_test_prediction, label='Predicted line', linewidth=2)
plt.xlabel('RM')
plt.ylabel('MEDV')
plt.legend(loc='lower right')
plt.title('model comparison by tested dataset')
plt.suptitle('RM vs MEDV')
plt.show()

residual_tested = y_test - y_test_prediction
plt.scatter(x_test, residual_tested, label='Tested data')
plt.hlines(y=0, xmin=x_test.min(), xmax=x_test.max(), linestyle='--', label='y = 0')
plt.xlabel('RM')
plt.ylabel('residual for tested datset')
plt.title('residual for tested dataset')
plt.legend(loc='lower left')
plt.show()

#Residual for trained dataset
y_train_prediction = regression_model.predict(x_train)
plt.scatter(x_train, y_train, label='Trained data')
plt.plot(x_train, y_train_prediction, label='Predicted trained data', linewidth=2)
plt.xlabel('RM')
plt.ylabel('MEDV')
plt.legend(loc='lower right')
plt.title('model comparison by trained dataset')
plt.suptitle('RM vs MEDV')
plt.show()

residual_trained = y_train - y_train_prediction
plt.scatter(x_train, residual_trained, label='Trained data')
plt.hlines(y=0, xmin=x_train.min(), xmax=x_train.max(), linestyle='-', label='y = 0')
plt.xlabel('RM')
plt.ylabel('residual for trained datset')
plt.legend(loc='lower left')
plt.title('residual for trained dataset')
plt.show()

"""
Residuals are scattered around the horizontal line, y = 0, with no particular 
pattern. This seemingly random distribution is a sign that the model is 
working. Ideally the residuals should be symmetrically and randomly spaced 
around the horizontal axis; if the residual plot shows some pattern, linear 
or nonlinear, that’s an indication that our model has room for improvement.
Residual plots can reveal bias from the model and statistical measures 
indicate goodness-of-fit.
Residual close to 0 indicates that our model is a good fit.
"""

#Mean squared error (MSE)
residual_tested[:5] #can be done by head or tail too
residual_tested.mean()
(residual_tested**2).mean() #MSE - Method 1

#MSE - Method 2
from sklearn.metrics import mean_squared_error
MSE_test_data = mean_squared_error(y_test, y_test_prediction).round(2)
Var = y_test.var()
#comparing Var and MSE we observe that MSE is lower indicating our model is not that bad.
#RMSE- square root of MSE

#R-scored: Method 1
regression_model.score(x_test,y_test)
regression_model.score(x_test,y_test_prediction)

#The total variation is calculated as the sum of squares of the difference between the response and the mean of response
total_variation = ((y_test - y_test.mean())**2).sum()

#The variation that the model fails to capture is computed as the sum of squares of residuals
variation = (residual_tested**2).sum()

#proportion of total variation from the data - R-scored Method 2
proportion_total_variation = 1-(variation/total_variation)

#Evaluating R-squared values in conjunction with residual plots quantifies model performance.

