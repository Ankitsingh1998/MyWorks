#Day011 - Clustering wines
"""
Clustering is a type of unsupervised learning that allows us to find groups 
of similar objects, objects that are more related to each other than to the 
objects in other groups. This is often used when we don’t have access to the 
ground truth, in other words, the labels are missing.

Examples of business use cases include the grouping of documents, music, and 
movies based on their contents, or finding customer segments based on purchase 
behavior as a basis for recommendation engines.
"""
"""
The goal of clustering is to separate the data into groups, or clusters, with 
more similar traits to each other than to the data in the other clusters.
"""
"""
There are more than 100 clustering algorithms known, 12 of them have been 
implemented in scikit-learn, but few gained popularity.

In general, there are four types:
--> Centroid based models - each cluster is represented by a single mean 
    vector (e.g., k-means),
--> Connectivity based models - built based on distance connectivity (e.g., 
    hierarchical clustering)
--> Distribution based models - built using statistical distributions (e.g., 
    Gaussian mixtures)
--> Density based models - clusters are defined as dense areas (e.g., DBSCAN)

In this module, we will explore the simple and widely-used clustering 
algorithm, k-means, to reveal subgroups of wines based on the chemical 
analysis reports.
"""
#More on clustering wines:
#https://scikit-learn.org/stable/modules/clustering.html#overview-of-clustering-methods

"""
k-means clustering algoritm:
    Assuming there are n data points.
    Step 1:initialization - pick k random points as cluster centers, called 
    centroids.
    Step 2:cluster assignment - assign each data point to its nearest centroid 
    based on its distance to each centroid, and that forms k clusters.
    Step 3:centroid updating - for each new cluster, calculate its centroid by 
    taking the average of all the points assigned to the cluster.
    Step 4:repeat steps 2 and 3 until none of cluster assignments change, or 
    it reaches the maximum number of iterations.
"""
"""
The algorithm has gained great popularity because it is easy to implement and 
scales well to large datasets. However, it is difficult to predict the number 
of clusters, it can get stuck in local optimums, and it can perform poorly 
when the clusters are of varying sizes and density.
"""
import numpy as np
x = np.array([5,3])
y = np.array([3,7])
np.sqrt(((x - y)**2).sum())

import pandas as pd
from sklearn.datasets import load_wine
df_wine = load_wine()

df = pd.DataFrame(df_wine.data, columns=df_wine.feature_names)
df.describe()
df.info()
df.isnull().any(axis=0)

"""
df['class'] = df_wine.target
dict1 = {0:'class_0',1:'class_1',2:'class_2'}
df['class'] = [dict1[num] for num in df['class']]
"""

import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
scatter_matrix(df.iloc[:,[0,5]]) #histogram + scatterplot
plt.show()

"""
Always perform EDA before diving into the modeling part, whether for the 
supervised or unsupervised learning problem.
"""

#Standardization - z = (x - mean)/std
X = df[['alcohol','total_phenols']]

from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

scale.fit(X)

scale.mean_
scale.scale_

x_scaled = scale.transform(X)

x_scaled.mean(axis=0)
x_scaled.std(axis=0)

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)
kmeans.fit(x_scaled)
y_prediction = kmeans.predict(x_scaled)

y_pred = pd.DataFrame(y_prediction, columns=['class'])
y_pred.value_counts()

centroids = kmeans.cluster_centers_ #To inspect the coordinates of the centroids/clusters

#plotting the scaled data
plt.scatter(x_scaled[:,0], x_scaled[:,1], c=y_prediction)
#identifying the centroids
plt.scatter(centroids[:,0], centroids[:,1], marker='*', s=200, c=[0,1,2], edgecolors='k')
plt.xlabel('alcohol')
plt.ylabel('total phenols')
plt.title('k-means, k = 3')
plt.show()

data = np.array([[13, 2.5]])
data_scaled = scale.transform(data)
kmeans.predict(data_scaled)

"""
Intuitively, k-means problem partitions n data points into k tight sets such 
that the data points are closer to each other than to the data points in the 
other clusters. And the tightness can be measured as the sum of squares of the 
distance from data point to its nearest centroid, or inertia.
"""
kmeans2 = KMeans(n_clusters = 2)
kmeans2.fit(x_scaled)
kmeans2.inertia_

kmeans3 = KMeans(n_clusters = 3)
kmeans3.fit(x_scaled)
kmeans3.inertia_

#plot inertia for different values of k
inertia = []
cluster_range = np.arange(1,11)
for i in cluster_range:
    km = KMeans(n_clusters = i)
    km.fit(x_scaled)
    inertia.append(km.inertia_)
plt.style.use('classic')
plt.plot(cluster_range, inertia, marker='o', color='r')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia corresponding to each clusters')
plt.show()

"""
k=3 seems to be optimal, as we increase the number of clusters from 3 to 4, 
the decrease in inertia slows down significantly, compared to that from 
2 to 3. This approach is called elbow method.
It is a useful graphical tool to estimate the optimal k in k-means.
"""
"""
The inertia decreases as the number of clusters increases. The optimal k 
should be where the inertia no longer decreases as rapidly.
One single inertia alone is not suitable to determine the optimal k because 
the larger k is, the lower the inertia will be.
"""

#In practice, the features are often chosen by the collaboration between data scientists and domain knowledge experts.
