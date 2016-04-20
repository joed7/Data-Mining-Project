import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.stats.stats import pearsonr
from sklearn import cluster
from scipy.cluster.vq import kmeans
import pandas as pd

from sklearn.preprocessing import normalize
import sys
import scipy.spatial.distance as mod


def scale(rawpoints, high=100.0, low=0.0):
    mins = np.min(rawpoints, axis=0)
    maxs = np.max(rawpoints, axis=0)
    
    rng = maxs - mins
    return (rawpoints - mins)*100.0 / rng

def descale(rawpoints,scaled_points, high=100.0, low=0.0):
    
    mins = np.min(rawpoints, axis=0)
    maxs = np.max(rawpoints, axis=0)
    
    rng = maxs - mins
    
    return (scaled_points * rng/100) + mins 
    

active_player_data = pd.read_csv('../data/active.csv')

active_player_data = active_player_data[ active_player_data['MP'] > 2500]

input_data = active_player_data[['MP','PTS','TRB','AST','FG%','BLK','3P%','pname','pid']]
input_data =  input_data.reset_index()
del input_data['index']

input_data['ppm'] = input_data['PTS']*36/input_data['MP']
input_data['apm'] = input_data['AST']*36/input_data['MP']
input_data['rpm'] = input_data['TRB']*36/input_data['MP']
input_data['bpm'] = input_data['BLK']*36/input_data['MP']

input_data_per_minute = input_data[['pid','pname','ppm','rpm','apm','bpm','FG%','3P%','MP']]

input_data_per_minute.fillna(0,inplace=True)


print 'training'


input_mat = input_data_per_minute.values[:,2:5]
scaled_input_mat = scale(input_mat)
k_means = cluster.KMeans(n_clusters=3)

print 'training start'
k_means.fit(scaled_input_mat)
print 'training over'
out = k_means.cluster_centers_

print descale(input_mat,k_means.cluster_centers_)


pd.DataFrame(descale(input_mat,k_means.cluster_centers_)).to_csv('cluster_centroid')

print 'cluster 1 size =' + str(len(input_data[k_means.labels_ == 0]))

cluster1 = input_data_per_minute[k_means.labels_ == 0]
cluster1.sort('MP',ascending=False)[['pid','pname','ppm','rpm','apm','MP']].to_csv('cluster1.csv')


print 'cluster 2 size =' + str(len(input_data[k_means.labels_ == 1]))

cluster2 = input_data_per_minute[k_means.labels_ == 1]
cluster2.sort('MP',ascending=False)[['pid','pname','ppm','rpm','apm','MP']].to_csv('cluster2.csv')


print 'cluster 3 size =' + str(len(input_data[k_means.labels_ == 2]))

cluster3 = input_data_per_minute[k_means.labels_ == 2]
cluster3.sort('MP',ascending=False)[['pid','pname','ppm','rpm','apm','MP']].to_csv('cluster3.csv')


