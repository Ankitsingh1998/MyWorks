#Day010 - KNN Classification
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
#0 --> setosa, 1 --> versicolor, 2-->virginca
df_iris = load_iris()
df = pd.DataFrame(df_iris.data, columns=['sep_len','sep_wid','pet_len','pet_wid'])
df['species'] = df_iris.target

dict1 = {0:'iris-setosa', 1:'iris-versicolor',2:'iris-virginica'}
df['species'] = [dict1[item] for item in df['species']]

X = df[['pet_len','pet_wid']]
Y = df['species']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0, stratify=Y)

y_train.value_counts()
y_test.value_counts()
#stratify applied on Y to distribute species types equally in both train and test

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5,p=2)
#On scikit-learn:
#https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html

knn.fit(x_train, y_train)

y_test_prediction = knn.predict(x_test)

#predict_proba --> predicts probability for a particular label to appear as a prediction
y_predicted_prob = knn.predict_proba(x_test)

#Accuracy - Method 1
(y_test_prediction==y_test.values).sum()/y_test.size

#Accuracy - Method 2
knn.score(x_test, y_test)

#Accuracy - Method 3
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_test_prediction)

#Confusion matrix: It is a summary of the counts of correct and incorrect prdictions, broken down by each class.
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_test_prediction, labels=['iris-setosa','iris-versicolor','iris-virginica'])

#visualizing the confusion matrix
import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix
plot_confusion_matrix(knn, x_test, y_test, cmap=plt.cm.Blues)
#dir(plt.cm)

#K-fold cross validation
"""
Previously we made train-test split before fitting the model so that we can 
report the model performance on the test data. This is a simple kind of cross 
validation technique, also known as the holdout method. However, the split is 
random, as a result, model performance can be sensitive to how the data is 
split. To overcome this, we introduce k-fold cross validation.
In k fold cross validation, the data is divided into k subsets. Then the 
holdout method is repeated k times, such that each time, one of the k subsets 
is used as the test set and the other k-1 subsets are combined to train the 
model. Then the accuracy is averaged over k trials to provide total 
effectiveness of the model. In this way, all data points are used; and there 
are more metrics so we don’t rely on one test data for model performance 
evaluation.
"""
from sklearn.model_selection import cross_val_score
knn_cv = KNeighborsClassifier(n_neighbors=3)
cv_scores = cross_val_score(knn_cv, X, Y, cv=10)
print(cv_scores)
cv_scores.mean()
"""
As a general rule, 5-fold or 10-fold cross validation is preferred; but there 
is no formal rule. As k gets larger, the difference in size between the 
training set and the resampling subsets gets smaller. As this difference 
decreases, the bias of the technique becomes smaller.
"""

#Grid Search:
"""
When we built our first knn model, we set the hyperparameter k to 5, and then 
to 3 later in k-fold cross validation; random choices really. What is the best 
k? Finding the optimal k is called tuning the hyperparameter. A handy tool is 
grid search. In scikit-learn, we use GridSearchCV, which trains our model 
multiple times on a range of values specified with the param_grid parameter 
and computes cross validation score, so that we can check which of our values 
for the tested hyperparameter performed the best.
"""
from sklearn.model_selection import GridSearchCV
knn2 = KNeighborsClassifier()
neighbor_values = [3,5,7,9]
param_grid = {'n_neighbors':neighbor_values}
knn_gs_cv = GridSearchCV(knn2, param_grid, cv=5)
knn_gs_cv.fit(X, Y) #will fit for every n_neighbors
knn_gs_cv.best_params_ #will show which k value has best prediction - returns a dictionary
knn_gs_cv.best_score_ #will show accuracy for best k value fit

#Now, final modeling:
knn_final = KNeighborsClassifier(n_neighbors=knn_gs_cv.best_params_['n_neighbors'])
knn_final.fit(X, Y)
y_prediction = knn_final.predict(X)
knn_final.score(X, Y)

y_prediction = pd.DataFrame(y_prediction, columns=['species'])
y_prediction.value_counts()

#predict for new data:
data = np.array([[3.76, 1.20]])
knn_final.predict(data)

data2 = np.array([[5.03,2.25]])
knn_final.predict(data2)

new_data = np.array([[3.76,1.2],[5.25,1.2],[1.58,1.2]])
knn_final.predict(new_data)
knn_final.predict_proba(new_data)

#sololearn code challenge - Binary Disorder
y_true = [int(x) for x in input('Enter 1st sequence of binary digits: ').split()]
y_pred =  [int(x) for x in input('Enter 2nd sequence of binary digits: ').split()]

import numpy as np

y_true = np.array(y_true )
y_true = y_true.astype(str) 

y_pred = np.array(y_pred )
y_pred = y_pred.astype(str) 
#y_true = y_true.reshape(-1, 1)
#y_pred = y_pred.reshape(-1, 1)
#print(y_true.shape)

from sklearn.metrics import confusion_matrix

print((confusion_matrix(y_pred, y_true, labels=['1', '0']))/1)

