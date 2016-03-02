import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.stats.stats import pearsonr
from sklearn import cluster
from scipy.cluster.vq import kmeans


hof_data = pd.read_csv('../data/hof.csv')

input_data = hof_data[['PTS','TRB','AST','FG%']]


input_mat = input_data.values

k_means = cluster.KMeans(n_clusters=4)

#print input_mat

print 'training start'
k_means.fit(input_mat)
print 'training over'

out = k_means.cluster_centers_


print k_means.cluster_centers_


print 'cluster 0 size =' + str(len(hof_data[k_means.labels_ == 0]))
print hof_data[k_means.labels_ == 0][['pname','PTS','TRB','AST','FG%','MP']]

print 'cluster 1='+str(len(hof_data[k_means.labels_ == 1]))
print hof_data[k_means.labels_ == 1][['pname','PTS','TRB','AST','FG%','MP']]

print 'cluster 2 size = '+str(len(hof_data[k_means.labels_ == 2]))
print hof_data[k_means.labels_ == 2][['pname','PTS','TRB','AST','FG%','MP']]

print 'cluster 4 size = '+str(len(hof_data[k_means.labels_ == 3]))
print hof_data[k_means.labels_ == 3][['pname','PTS','TRB','AST','FG%','MP']]




