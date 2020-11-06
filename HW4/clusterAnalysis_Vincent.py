# Edward Riley & Vincent Venutolo

import sys, os, math
from sklearn import metrics as met
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances as smetp
import pandas as pd
from pandas import DataFrame
from scipy.io.arff import loadarff
from scipy.spatial import distance
import numpy as np

raw = loadarff(str(sys.argv[1]))
df = pd.DataFrame(raw[0])
data = df.iloc[:,[0,1,2,3]].values
sse_rds = []
kmean_rds = []
km_center_rds = []
cohesion = []
avg_silcoe_rds = []
# print(data)

def calculateEulideanDistance(ctrd,data):
    totalEuclideanDistance = 0
    for i in range(0,len(data)):
        totalEuclideanDistance += math.sqrt(  (data[i][0]-ctrd[0])**2 + (data[i][1]-ctrd[1])**2 + (data[i][2]-ctrd[2])**2 + (data[i][3]-ctrd[3])**2 )
    return totalEuclideanDistance

for i in range(3,7):
    kmeans = KMeans(n_clusters=i, n_init = 10, max_iter = 500, random_state=10)
    kmeans.fit(data)
    print(' ')
    print('===== ' + str(i) + ' K-VALUE =====')
    ctrd = kmeans.cluster_centers_
    km_center_rds.append(ctrd)

    # Get the cohesion data of each k cluster
    for j in range(0,i):
        k = df[kmeans.labels_==j].iloc[:,[0,1,2,3]].values
        cohesion.append(calculateEulideanDistance(ctrd[j],k))
    # SSE
    print('SSE: ' + str(kmeans.inertia_))
    sse_rds.append(kmeans.inertia_)
    sil_coe = met.silhouette_score(data,kmeans.labels_, metric='sqeuclidean')
    print('Silhouette Score: ' + str(sil_coe))
    avg_silcoe_rds.append(sil_coe)


print('\nEuaclidean Distance to centroid Records: ')
for i in range(0,len(cohesion)):
    print('Cluster #' + str(i) + ': ' + str(cohesion[i]))
#print('\nFinal Cluster Centroids: ')
#print(km_center_rds)
