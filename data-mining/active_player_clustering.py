import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.stats.stats import pearsonr
from sklearn import cluster
from scipy.cluster.vq import kmeans

from sklearn.preprocessing import normalize
import sys
import scipy.spatial.distance as mod


def scale_linear_bycolumn(rawpoints, high=100.0, low=0.0):
    mins = np.min(rawpoints, axis=0)
    maxs = np.max(rawpoints, axis=0)
    rng = maxs - mins
    return high - (((high - low) * (maxs - rawpoints)) / rng)


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

#print input_data_per_minute.sort('ppm',ascending=False)

input_data_per_minute.fillna(0,inplace=True)





print 'training'


input_mat = input_data_per_minute.values[:,2:5]

#print input_mat

scaled_input_mat = scale2(input_mat)

#print descale(input_mat, scaled_input_mat)


k_means = cluster.KMeans(n_clusters=5)

#print input_mat

print 'training start'
k_means.fit(scaled_input_mat)
print 'training over'

out = k_means.cluster_centers_

'''
compute distance
'''
dist1 = mod.cdist(scaled_input_mat, out[0,:].reshape(1,3), 'euclidean')
dist2 = mod.cdist(scaled_input_mat, out[1,:].reshape(1,3), 'euclidean')
dist3 = mod.cdist(scaled_input_mat, out[2,:].reshape(1,3), 'euclidean')
dist4 = mod.cdist(scaled_input_mat, out[3,:].reshape(1,3), 'euclidean')
dist5 = mod.cdist(scaled_input_mat, out[4,:].reshape(1,3), 'euclidean')


distdf1 = pd.DataFrame(dist1,columns=['dist'])
distdf2 = pd.DataFrame(dist2,columns=['dist'])
distdf3 = pd.DataFrame(dist3,columns=['dist'])
distdf4 = pd.DataFrame(dist4,columns=['dist'])
distdf5 = pd.DataFrame(dist5,columns=['dist'])

print descale(input_mat,k_means.cluster_centers_)

'''
print 'cluster 0 size =' + str(len(input_data[k_means.labels_ == 0]))
print input_data[k_means.labels_ == 0].sort('MP',ascending=False)[['pname','PTS','TRB','AST','FG%','MP']]

print 'cluster 1='+str(len(input_data[k_means.labels_ == 1]))
print input_data[k_means.labels_ == 1].sort('MP',ascending=False)[['pname','PTS','TRB','AST','FG%','MP']]

print 'cluster 2 size = '+str(len(input_data[k_means.labels_ == 2]))
print input_data[k_means.labels_ == 2].sort('MP',ascending=False)[['pname','PTS','TRB','AST','FG%','MP']]

print 'cluster 4 size = '+str(len(input_data[k_means.labels_ == 3]))
print input_data[k_means.labels_ == 3].sort('MP',ascending=False)[['pname','PTS','TRB','AST','FG%','MP']]

print 'cluster 5 size = '+str(len(input_data[k_means.labels_ == 4]))
print input_data[k_means.labels_ == 4].sort('MP',ascending=False)[['pname','PTS','TRB','AST','FG%','MP']]

'''



print 'cluster 1 size =' + str(len(input_data[k_means.labels_ == 0]))

distcluster1 = distdf1[k_means.labels_ == 0]
cluster1 = input_data_per_minute[k_means.labels_ == 0]
print pd.concat([cluster1,distcluster1],axis=1).sort('dist')[['pid','pname','ppm','rpm','apm','MP']]
pd.concat([cluster1,distcluster1],axis=1).sort('MP',ascending=False)[['pid','pname','ppm','rpm','apm','MP','dist']].to_csv('cluster1.csv')


print 'cluster 2 size =' + str(len(input_data[k_means.labels_ == 1]))

distcluster2 = distdf1[k_means.labels_ == 1]
cluster2 = input_data_per_minute[k_means.labels_ == 1]
print pd.concat([cluster2,distcluster2],axis=1).sort('dist')[['pid','pname','ppm','rpm','apm','MP']]
pd.concat([cluster2,distcluster2],axis=1).sort('MP',ascending=False)[['pid','pname','ppm','rpm','apm','MP','dist']].to_csv('cluster2.csv')


print 'cluster 3 size =' + str(len(input_data[k_means.labels_ == 2]))

distcluster3 = distdf1[k_means.labels_ == 2]
cluster3 = input_data_per_minute[k_means.labels_ == 2]
print pd.concat([cluster3,distcluster3],axis=1).sort('dist')[['pid','pname','ppm','rpm','apm','MP']]
pd.concat([cluster3,distcluster3],axis=1).sort('MP',ascending=False)[['pid','pname','ppm','rpm','apm','MP','dist']].to_csv('cluster3.csv')



print 'cluster 4 size =' + str(len(input_data[k_means.labels_ == 3]))

distcluster4 = distdf1[k_means.labels_ == 3]
cluster4 = input_data_per_minute[k_means.labels_ == 3]
print pd.concat([cluster4,distcluster4],axis=1).sort('dist')[['pid','pname','ppm','rpm','apm','MP']]
pd.concat([cluster4,distcluster4],axis=1).sort('MP',ascending=False)[['pid','pname','ppm','rpm','apm','MP','dist']].to_csv('cluster4.csv')

print 'cluster 5 size =' + str(len(input_data[k_means.labels_ == 4]))

distcluster5 = distdf1[k_means.labels_ == 4]
cluster5 = input_data_per_minute[k_means.labels_ == 4]
print pd.concat([cluster5,distcluster5],axis=1).sort('dist')[['pid','pname','ppm','rpm','apm','MP']]
pd.concat([cluster5,distcluster5],axis=1).sort('MP',ascending=False)[['pid','pname','ppm','rpm','apm','MP','dist']].to_csv('cluster5.csv')

'''

#input_data_per_minute[k_means.labels_ == 0].sort('MP',ascending=False)[['pid','pname','ppm','rpm','apm','MP']].to_csv('cluster1.csv')

print 'cluster 1='+str(len(input_data[k_means.labels_ == 1]))
#print input_data_per_minute[k_means.labels_ == 1].sort('MP',ascending=False)[['pid','pname','ppm','rpm','apm','MP']]
print len(distdf1[k_means.labels_ == 1])

input_data_per_minute[k_means.labels_ == 1].sort('MP',ascending=False)[['pid','pname','ppm','rpm','apm','MP']].to_csv('cluster2.csv')

print 'cluster 2 size = '+str(len(input_data[k_means.labels_ == 2]))
#print input_data_per_minute[k_means.labels_ == 2].sort('MP',ascending=False)[['pid','pname','ppm','rpm','apm','MP']]
print len(distdf1[k_means.labels_ == 2])

input_data_per_minute[k_means.labels_ == 2].sort('MP',ascending=False)[['pid','pname','ppm','rpm','apm','MP']].to_csv('cluster3.csv')

print 'cluster 3 size = '+str(len(input_data[k_means.labels_ == 3]))
#print input_data_per_minute[k_means.labels_ == 3].sort('MP',ascending=False)[['pid','pname','ppm','rpm','apm','MP']]
print len(distdf1[k_means.labels_ == 3])

input_data_per_minute[k_means.labels_ == 3].sort('MP',ascending=False)[['pid','pname','ppm','rpm','apm','MP']].to_csv('cluster4.csv')


print 'cluster 4 size = '+str(len(input_data[k_means.labels_ == 4]))
#print input_data_per_minute[k_means.labels_ == 4].sort('MP',ascending=False)[['pid','pname','ppm','rpm','apm','MP']]
print len(distdf1[k_means.labels_ == 4])

input_data_per_minute[k_means.labels_ == 4].sort('MP',ascending=False)[['pid','pname','ppm','rpm','apm','MP']].to_csv('cluster5.csv')


print 'cluster 5 size = '+str(len(input_data[k_means.labels_ == 5]))
print input_data_per_minute[k_means.labels_ == 5].sort('MP',ascending=False)[['pid','pname','ppm','rpm','apm','MP']]

input_data_per_minute[k_means.labels_ == 5].sort('MP',ascending=False)[['pid','pname','ppm','rpm','apm','MP']].to_csv('cluster6.csv')
'''