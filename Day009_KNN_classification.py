#Day009 - KNN Classification
"""
classification - to predict a discrete value
Discrete data are only able to have certain values, while continuous data 
can take on any value.
Examples:
    whether a breast cancer is benign or malignant given a set of features.
    to classify an image as containing cats, dogs or horses.
    to predict whether an email is spam or not from the email address.
In each of the above examples, the labels comes in categorical form and 
represent a finite number of classes.
Discrete data values can be numeric, like the number of students in a class
or it can be categorical like a color, red, blue or green.
"""
"""
Types of classification:
    Binary:
        If there are two classes to predict. for eg, a benign or malignant 
        tumor.
    Multi-class:
        If there are more than two classes. for eg, classifying the species 
        of iris, which can be versicolor, virqinica, or setosa, based on 
        their sepal and petal characteristics.
"""
"""
Logistic Regression
KNN (K-nearest neighbors)
decision trees
naive bayes
SVM (Support vector machines)
Neural Networks
"""
#KNN to classify iris species
#input variable(x) --> mapping --> output variable(y)
#output --> continuous in Linear Regression and categorical in classification

import pandas as pd
from sklearn.datasets import load_iris
#0 --> setosa, 1 --> versicolor, 2-->virginca
df_iris = load_iris()
df = pd.DataFrame(df_iris.data, columns=['sep_len','sep_wid','pet_len','pet_wid'])
df['species'] = df_iris.target

df.shape
df.head()
df.describe()

#Importance of feature scaling - https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html
"""
The ranges of attributes are still of similar magnitude, thus we will skip 
standardization. However, standardizing attributes such that each has a mean 
of zero and a standard deviation of one, can be an important preprocessing 
step for many machine learning algorithms. This is also called feature scaling.
"""

df.groupby('species').size()
df['species'].value_counts()

"""
An imbalanced dataset is one where the classes within the data are not 
equally represented.
An example of an imbalanced dataset is fraud. Generally only a small 
percentage of the total number of transactions is actual fraud, about 1 in 
1000. And when the dataset is imbalanced, a slightly different analysis will
be used. Therefore, it is important to understand whether the data is balanced
or imbalanced.
Link for imbalanced dataset:
https://machinelearningmastery.com/tactics-to-combat-imbalanced-classes-in-your-machine-learning-dataset/
"""
import matplotlib.pyplot as plt
df[['sep_len','sep_wid','pet_len','pet_wid']].hist()
plt.show()

#plt.style.available
plt.style.use('classic')

flower_names = ['iris-setosa', 'iris-versicolor', 'iris-viginica']
f_name = [name for name in flower_names]
colors = [num for num in df['species']]
scatter = plt.scatter(df['sep_len'], df['sep_wid'], c = colors)
plt.xlabel('sepal length, (cm)')
plt.ylabel('sepal width, (cm)')
plt.legend(handles=scatter.legend_elements()[0],labels = f_name)
plt.suptitle('sepal length vs sepal width')
plt.title('iris classification')
plt.show()

scatter = plt.scatter(df['pet_len'], df['pet_wid'], c = colors)
plt.xlabel('petal length, (cm)')
plt.ylabel('petal width, (cm)')
plt.legend(handles= scatter.legend_elements()[0],labels = f_name)
plt.suptitle('petal length vs petal width')
plt.title('iris classification')
plt.show()
"""
Using sepal_length and sepal_width features, we can distinguish iris-setosa 
from others; separating iris-versicolor from iris-virginica is harder because 
of the overlap as seen by the green and brown datapoints.
Interestingly, the length and width of the petal are highly correlated, and 
these two features are very useful to identify various iris species. It is 
notable that the boundary between iris-versicolor and iris-virginica remains 
a bit fuzzy, indicating the difficulties for some classifiers. It is worth 
keeping in mind when training to decide which features we should use.
"""
#plot for every feature
pd.plotting.scatter_matrix(df.iloc[:,0:4])

"""
KNN:
    It is a supervised machine learning model that takes a data point, looks 
    at its 'k' closest labeled data points, and assigns the label by a 
    majority vote.
k --> hyperparameter
K nearest neighbors can also be used for regression problems. The difference 
lies in prediction. Instead of a majority vote, knn for regression makes a 
prediction using the mean labels of the k closest data points.
"""
