import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.stats.stats import pearsonr
from sklearn import cluster

from sklearn.preprocessing import normalize
import sys
import scipy.spatial.distance as mod

ncluser = 15

def scale2(rawpoints, high=100.0, low=0.0):
    mins = np.min(rawpoints, axis=0)
    maxs = np.max(rawpoints, axis=0)
    
    
    rng = maxs - mins
    return (rawpoints - mins)*100.0 / rng

def descale(rawpoints,scaled_points, high=100.0, low=0.0):
    
    mins = np.min(rawpoints, axis=0)
    maxs = np.max(rawpoints, axis=0)
    
    rng = maxs - mins
    
    return (scaled_points * rng/100) + mins 
    
def scatterPlot(ds1,ds2,v1,v2):

    plt.scatter(ds1,ds2)
    plt.xlabel(v1)

    plt.ylabel(v2)
    plt.grid(True)
    plt.show()
    
    
dist=[]

def clustering(n):
    d=0
    k_means = cluster.KMeans(n_clusters=n)
    
    
    k_means.fit(scaled_input_mat)
    
    out = k_means.cluster_centers_
    
    
    for i in range(n):
        disti = mod.cdist(scaled_input_mat, out[i,:].reshape(1,3), 'euclidean')
        distdfi = pd.DataFrame(disti,columns=['dist'])
        distclusteri = distdfi[k_means.labels_ == i]
        
        d = d + np.sum(distclusteri.values)
    dist.append(d)    
    



hof_data = pd.read_csv('../data/hof.csv')

input_data = hof_data[['PTS','TRB','AST']]
input_data.fillna(0,inplace=True)
input_mat = input_data.values
scaled_input_mat = scale2(input_mat)


cluster_number = []

for i in range(ncluser):
    clustering(i+1)    
    cluster_number.append(i+1)    
print dist

diff_dist = []

for i in range(len(dist)):
    if i == len(dist)-1:
        continue
    diff_dist.append( (dist[i] - dist[i+1]))
    
arr1 = np.array(cluster_number)
arr2 = np.array(dist)

scatterPlot(arr1, arr2, 'cluster_number', 'distance')

cluster_number.pop(0)
arr1 = np.array(cluster_number)
arr2 = np.array(diff_dist)

scatterPlot(arr1, arr2, 'cluster_number', 'distance-gained')