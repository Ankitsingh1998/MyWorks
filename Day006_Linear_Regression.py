#Day006 - Linear Regression
"""
Machine learning, a subset of data science, is the scientific study of 
computational algorithms and statistical models to perform specific tasks t
hrough patterns and inference instead of explicit instructions. 
Machine learning can be described as a set of tools to build models on data. 
Data scientists explore data, select and build models (machine), tune 
parameters such that a model fits observations (learning), then use the model 
to predict and understand aspects of new unseen data.
Machine learning is a set of tools used to build models on data. Building 
models to understand data and make predictions is an important part of a data 
scientist's job.
"""
"""
Supervised Learning:
    known past data also called as labels.
    for eg. predicting what price a house will sale for?
    Linear Regression
    Classification
    
Unsupervised Learning:
    unknown past data.
    for eg. determining the topics discussed in restaurant reviews?
    Clustering
"""
"""
scikit-learn :
    import-->instantiate-->fit-->predict
    It itself provides some datasets to work on. such as, Boston house-prices 
    datasets, iris dataset for classification task
"""
"""
Linear Regression:
    y = m*x + c
    m --> slope, c --> intercept, x --> feature, y --> label
    m and c are to be found such that the errors are minimized.
"""
#EDA (Exploratory Data Analysis):
from sklearn.datasets import load_boston
boston_house_data = load_boston()
import pandas as pd
df = pd.DataFrame(boston_house_data.data, columns=boston_house_data.feature_names)
df['MEDV'] = boston_house_data.target #MEDV --> Median home price values in $1000
df.shape
df.columns.tolist()
df.iloc[:,[0,1,2,3,4,-1]].head(10)
df.iloc[:,[0,1,2,3,4,-1]].tail(10)
description = df.describe(include='all')

import matplotlib.pyplot as plt
df.hist(column='CHAS')
plt.show()

df.hist(column='RM', bins = 20)
plt.show()

#correlation matrix - measures linear relationship between variables
"""
each element raqnges from -1 to 1.
near 1 represents strong positive correlation between variables and similarly
near -1 represents strong negative correlation between variables.
"""
"""
corr_matrix analysis:
The last row or column is used to identify features that are most correlated 
with the target MEDV (median value of owner-occupied homes in $1000’s).
LSTAT (percentage of lower status of the population) is most negatively 
correlated with the target (-0.74) which means that as the percentage of 
lower status drops, the median house values increases; while RM (the average 
number of rooms per dwelling) is most positively correlated with MEDV (0.70) 
which means that the house value increases as the number of rooms increases.

Feature Selection:
    Feature selection is used for several reasons, including simplification 
    of models to make them easier to interpret, shorter training time, 
    reducing overfitting, etc.
"""
corr_matrix = df.corr().round(2)

#RM and MEDV are well correlated, so let's plot their scatter
plt.style.use('classic')
plt.scatter(df['RM'], df['MEDV'], marker='*', color='c',)
plt.legend('scatter')
plt.xlabel('RM')
plt.ylabel('MEDV')
plt.xlim(5,8)
plt.ylim(5,25)
plt.title('RM and MEDV are strongly positively correlated')
plt.show()

corr_desciption = corr_matrix.describe()

#(DIS vs NOX) and (MEDV vs LSTAT) are strongly neagtively correlated, so let's plot them as well
plt.style.use('classic')
plt.scatter(df['NOX'], df['DIS'], marker='.', color='k',)
plt.legend('scatter')
plt.xlabel('NOX')
plt.ylabel('DIS')
plt.xlim(0.35,0.8)
plt.ylim(0.5,9)
plt.title('NOX and DIS are strongly negatively correlated')
plt.show()

plt.style.use('classic')
plt.scatter(df['LSTAT'], df['MEDV'], marker='^', color='g',)
plt.legend('scatter')
plt.xlabel('LSTAT')
plt.ylabel('MEDV')
plt.xlim(1,34)
plt.ylim(3,50)
plt.title('MEDV and LSTAT are strongly negatively correlated')
plt.show()

df.plot(kind='scatter', x='RM', y='MEDV', figsize=(8,6))

