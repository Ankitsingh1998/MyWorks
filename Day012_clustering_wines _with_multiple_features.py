#Day012 - clustering wines with multiple features
import numpy as np
import pandas as pd
from sklearn.datasets import load_wine
df_wine = load_wine()

df = pd.DataFrame(df_wine.data, columns=df_wine.feature_names)

import matplotlib.pyplot as plt

X = df

from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

scale.fit(X)

scale.mean_
scale.scale_

x_scaled = scale.transform(X)

x_scaled.mean(axis=0)
x_scaled.std(axis=0)

from sklearn.cluster import KMeans

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

kmeans = KMeans(3)
kmeans.fit(x_scaled)
kmeans.inertia_

y_prediction = kmeans.predict(x_scaled)
centroids = kmeans.cluster_centers_

data = np.array([[14, 1.8, 2.58, 16, 128, 3, 3, 0.3, 2.3, 6, 1.2, 4, 1100]])
data_scaled = scale.transform(data)
kmeans.predict(data_scaled)

#sololearn code challenge - pandas pandas pandas
"""
3
1 0
0 .5
4 0
"""
import numpy as np

first = np.array([[0., 0.]])
second = np.array([[2., 2.]])
n = int(input('Enter the number of clusters: '))

data = []

for i in range(n):
   data.append([float(i) for i in input('Enter three centroids: ').split()])
  
    
data = np.array(data).reshape((-1,2))

for i in range(n):
   dist1 = np.sqrt(((data[i]-first[0])**2).sum())
 
   dist2 = np.sqrt(((data[i]-second[0])**2).sum())
   
   if (dist1) <= (dist2):
      first = np.vstack((first,data[i]))
       
   else:
      second = np.vstack((second,data[i]))
       
if first.size > 2:
   mean1 = np.mean(first[1:], axis=0)
   print(np.around(mean1, decimals=2))
else:
   print(None)
