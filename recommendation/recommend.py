import numpy as np
import pandas as pd
import sys
import MySQLdb
import scipy.spatial.distance as mod
from operator import itemgetter

name = 'Curry'
max_attr = ''
min_attr=''
players = []

no_of_attrs= 3


def scale(rawpoints, high=100.0, low=0.0):
    rng = max_attr - min_attr
    return (rawpoints - min_attr)*100.0 / rng
    
def fetMixMaxAttr():
    active_player_data = pd.read_csv('../data/active.csv')
    active_player_data = active_player_data[ active_player_data['MP'] > 2500]
    
    input_data = active_player_data[['MP','PTS','TRB','AST']]
    input_data =  input_data.reset_index()
    del input_data['index']
    
    input_data['ppm'] = input_data['PTS']*36/input_data['MP']
    input_data['apm'] = input_data['AST']*36/input_data['MP']
    input_data['rpm'] = input_data['TRB']*36/input_data['MP']
    
    input_data_per_minute = input_data[['ppm','rpm','apm']]
    input_data_per_minute.fillna(0,inplace=True)
    
    global max_attr
    global min_attr
    
    max_attr = np.max(input_data_per_minute.values,axis=0)
    min_attr = np.min(input_data_per_minute.values,axis=0)
    
def getPlayerAttrMatrix(player):
    
    ppm = player[2]
    rpm = player[3]
    apm = player[4]
    mp = player[5]
    
    a=[]
    a.append(ppm)
    a.append(rpm)
    a.append(apm)
    #a.append(mp)
    
    return np.asarray(a)


def fetchClusters(pid,cluster_id):
    con = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='mining')
    cursor = con.cursor()
    
    query = "SELECT pid,pname,ppm,rpm,apm,MP FROM clusters_3 where cluster_id="+str(cluster_id) +" and pid <> "+ str(pid)
    #print query
    
    cursor.execute(query) 
    
    result = cursor.fetchall() 
    for r in result:
        pid=int(r[0])
        pname=r[1]
        ppm=float(r[2])
        rpm=float(r[3])
        apm=float(r[4])
        mp=int(r[5])        
        
        players.append( (pid,pname,ppm,rpm,apm,mp) )
    return players
    
                
def fetchPlayerInfo(name):
    con = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='mining')
    cursor = con.cursor()
    
    name = '%'+str(name)+"%"
    
    query = "SELECT pid,pname,ppm,rpm,apm,MP,cluster_id FROM clusters_3 where pname like '"+name+ "'"
    
    #print query
    
    cursor.execute(query) 
    
    
    result = cursor.fetchall() 
    for r in result:
        pid=int(r[0])
        pname=r[1]
        ppm=float(r[2])
        rpm=float(r[3])
        apm=float(r[4])
        mp=int(r[5])        
        cluster_id=int(r[6])
        
        player = (pid,pname,ppm,rpm,apm,mp) 
        
        #print 'cluster='+str(cluster_id)
        return player,cluster_id

fetMixMaxAttr()

player,cluster_id = fetchPlayerInfo(name)
players_in_clusters = fetchClusters(player[0],cluster_id)

#print players_in_clusters
given_player_matrix = getPlayerAttrMatrix(player)

#print given_player_matrix
scaled_given_player_matrix  = scale(given_player_matrix)


distance_tuples= []

for p in players_in_clusters:
    t_matrix = getPlayerAttrMatrix(p)
    scaled_t_matrix = scale(t_matrix)
    
    m1 = scaled_given_player_matrix.reshape(1,no_of_attrs)
    m2 = scaled_t_matrix.reshape(1,no_of_attrs)
    
    dist = mod.cdist(m1, m2, 'euclidean')
    
    tuple = (p[1],dist[0][0])
    distance_tuples.append(tuple)

    
sorted_distance_tuples = sorted(distance_tuples, key=itemgetter(1),reverse=False)

print 'Similar players to '+name    
for i in sorted_distance_tuples[0:10]:
    print i[0]
