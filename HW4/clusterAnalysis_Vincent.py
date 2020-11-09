# Edward Riley & Vincent Venutolo

import sys, os, math
from sklearn import metrics as met
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.metrics.pairwise import euclidean_distances as smetp
import pandas as pd
from pandas import DataFrame
from scipy.io.arff import loadarff
from scipy.spatial import distance
import numpy as np

raw = loadarff(str(sys.argv[1]))
df = pd.DataFrame(raw[0])
data = df.iloc[:,[0,1,2,3]].values
summary = []

# ai
def calculate_Cohesion(intra_cluster):
    totalEuclideanDistance = 0
    # Calculate the cohesive average silhouette coefifficent
    for i in range(1,len(intra_cluster)):
        totalEuclideanDistance += math.sqrt(  (intra_cluster[i][0]-intra_cluster[0][0])**2 + (intra_cluster[i][1]-intra_cluster[0][1])**2 + (intra_cluster[i][2]-intra_cluster[0][2])**2 + (intra_cluster[i][3]-intra_cluster[0][3])**2 )
    return totalEuclideanDistance / (len(intra_cluster) - 1)

# bi
def calculate_Separations(intra_cluster,inter_cluster):
    # Calculate separations
    avg_inter_clusters = []
    
    for i in range(0,len(inter_cluster)):
        cluster_cnt = 0
        totalEuclideanDistance = 0
        for j in range(0,len(inter_cluster[i])):
            totalEuclideanDistance += math.sqrt(  (inter_cluster[i][j][0]-intra_cluster[0][0])**2 + (inter_cluster[i][j][1]-intra_cluster[0][1])**2 + (inter_cluster[i][j][2]-intra_cluster[0][2])**2 + (inter_cluster[i][j][3]-intra_cluster[0][3])**2 )
            cluster_cnt = cluster_cnt + 1
        avg_inter_clusters.append(totalEuclideanDistance / (cluster_cnt - 1))

    # Pick the minimal average silhouette coefifficent out of inter clusters
    res = avg_inter_clusters[0]
    for m in range(1,len(avg_inter_clusters)):
        res = min(res,avg_inter_clusters[m])
    return res

# si
def calculate_Silhouette_Coefficient(ai,bi):
    si = abs(1 - (ai/bi))
    return si;

k_values = [2,3,5,7];
results = []
for i in k_values:
    ai = []
    bi = []
    si = []
    kmeans = KMeans(n_clusters=i, max_iter = 500, random_state=10)
    kmeans.fit(data)
    avg_sil_coe = (met.silhouette_score(data,kmeans.labels_,metric='euclidean'))
    print(' ')
    print('===== ' + str(i) + ' K-VALUE =====')

    # Get the Separations & Cohesions Silhouette Coefficents
    for j in range(0,i):

        comb_inter_clusters = []
        intra_cluster = df[kmeans.labels_==j].iloc[:,[0,1,2,3]].values
        
        for k in range(0,i):
            if (k != j):
                comb_inter_clusters.append(df[kmeans.labels_==k].iloc[:,[0,1,2,3]].values)
        ai.append(calculate_Cohesion(intra_cluster))
        bi.append(calculate_Separations(intra_cluster,comb_inter_clusters))
        si.append(calculate_Silhouette_Coefficient(ai[j],bi[j]))
    print('ai = ', ai)
    print('bi = ', bi)
    print('si = ', si)
    print('Avg Silhouette Coefficients = ', avg_sil_coe)
