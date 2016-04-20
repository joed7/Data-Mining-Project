import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.stats.stats import pearsonr
from sklearn import cluster
from scipy.cluster.vq import kmeans



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
    


hof_data = pd.read_csv('../data/hof.csv')

input_data = hof_data[['PTS','TRB','AST']]
input_data.fillna(0,inplace=True)


input_mat = input_data.values

k_means = cluster.KMeans(n_clusters=4)

#scale the features
scaled_input_mat = scale2(input_mat)

#print input_mat


print 'training start'
k_means.fit(scaled_input_mat)
print 'training over'

out = k_means.cluster_centers_


print descale(input_mat,k_means.cluster_centers_)



print 'cluster 0 size =' + str(len(hof_data[k_means.labels_ == 0]))
print hof_data[k_means.labels_ == 0][['pname','PTS','TRB','AST','FG%','MP']]
hof_data[k_means.labels_ == 0][['pname','PTS','TRB','AST','FG%','MP']].to_csv('anamoly_cluster_1.csv')

print 'cluster 1='+str(len(hof_data[k_means.labels_ == 1]))
print hof_data[k_means.labels_ == 1][['pname','PTS','TRB','AST','FG%','MP']]
hof_data[k_means.labels_ == 1][['pname','PTS','TRB','AST','FG%','MP']].to_csv('anamoly_cluster_2.csv')

print 'cluster 2 size = '+str(len(hof_data[k_means.labels_ == 2]))
print hof_data[k_means.labels_ == 2][['pname','PTS','TRB','AST','FG%','MP']]
hof_data[k_means.labels_ == 2][['pname','PTS','TRB','AST','FG%','MP']].to_csv('anamoly_cluster_3.csv')

print 'cluster 4 size = '+str(len(hof_data[k_means.labels_ == 3]))
hof_data[k_means.labels_ == 3][['pname','PTS','TRB','AST','FG%','MP']].to_csv('anamoly_cluster_4.csv')
print hof_data[k_means.labels_ == 3][['pname','PTS','TRB','AST','FG%','MP']]


