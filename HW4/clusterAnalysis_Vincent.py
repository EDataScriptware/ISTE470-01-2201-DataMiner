# Edward Riley & Vincent Venutolo

import sys, os, math
from sklearn import metrics as met
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances as smetp
import pandas as pd
from pandas import DataFrame
from scipy.io.arff import loadarff
from scipy.spatial import distance

raw = loadarff(str(sys.argv[1]))
df = pd.DataFrame(raw[0])
data = df.iloc[:,[0,1,2,3]].values
sse_rds = []
kmean_rds = []
km_center_rds = []
cohesion = []
avg_silcoe_rds = []
# print(data)

for i in range(3,4):
    kmeans = KMeans(n_clusters=i, n_init = 10, max_iter = 500, random_state=10)
    kmeans.fit(data)
    print(' ')
    print('----- ' + str(i) + ' K-VALUE -----')
    km = kmeans.cluster_centers_
    # print(km)
    km_center_rds.append(km)

    # Get the cohesion data of each k cluster
    for j in range(0,i):
        k = df[kmeans.labels_==j].iloc[:,[0,1,2,3]].values
        print(k.inertia_)
        cohesion.append(distance.euclidean(k))

    print('---- SSE: ' + str(kmeans.inertia_) + ' ----')
    sse_rds.append(kmeans.inertia_)
    # print(kmeans.labels_)
    sil_coe = met.silhouette_score(data,kmeans.labels_, metric='sqeuclidean')
    print('---- Score: ' + str(sil_coe) + ' ----')
    avg_silcoe_rds.append(sil_coe)


print('------ COHESION RECORD ------')
print(cohesion)
# k1 = df[kmeans.labels_==0].iloc[:,[0,1,2,3]].values
# k2 = df[kmeans.labels_==1]
# k3 = df[kmeans.labels_==2]
# met.silhouette_score(kmean_rds[0].tolist(),kmeans.labels_,metric='sqeclidean')
print('------ SSE RECORDS ------')
print(sse_rds)
#print('------ KMEANS RECORDS ------')
#print(kmean_rds)
print('------ AVG SILHOUETTE COE RECORDS ------')
print(avg_silcoe_rds)

