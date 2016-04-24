import pandas as pd
import numpy as np
import pickle

from sklearn import tree
from sklearn.ensemble      import RandomForestClassifier
from sklearn.svm import SVC

def createPickle(name,dict):
    fileObject = open(name,'wb') 
    pickle.dump(dict,fileObject)   
    fileObject.close() 
    
def scale2(rawpoints, high=100.0, low=0.0):
    mins = np.min(rawpoints, axis=0)
    maxs = np.max(rawpoints, axis=0)
    
    print mins
    print maxs
    
    rng = maxs - mins
    return (rawpoints - mins)*100.0 / rng

labels=[]

analomy = pd.read_csv('../anamoly/anamoly_cluster_2.csv')

hof_anamoly={}

for index, row in analomy.iterrows():
     hof_anamoly[row['pname']]=1
                 
                 

hof_data = pd.read_csv('../data/hof.csv')
            
hof_players = []                 
for index, row in hof_data.iterrows():
     if not row['pname'] in hof_anamoly:
         hof_players.append(row)
         labels.append(0)
         
         
hof_input_data = pd.DataFrame.from_records(hof_players)[['pid','pname','MP','PTS','TRB','AST']]       
      
hof_input_data['ppm'] = hof_input_data['PTS']*36/hof_input_data['MP']
hof_input_data['apm'] = hof_input_data['AST']*36/hof_input_data['MP']
hof_input_data['rpm'] = hof_input_data['TRB']*36/hof_input_data['MP']

hof_input_data_per_minute = hof_input_data[['ppm','rpm','apm']]
                          

hof_input_mat = hof_input_data_per_minute.values

#read retired not hof data

retired = pd.read_csv('../data/retired.csv')
filtered_retired = retired[ retired['lyear'] < 2007][retired['MP'] > 25000][retired['lyear'] > 1980][['pid','pname','MP','PTS','TRB','AST']]
    
filtered_retired['ppm'] = filtered_retired['PTS']*36/filtered_retired['MP']
filtered_retired['apm'] = filtered_retired['AST']*36/filtered_retired['MP']
filtered_retired['rpm'] = filtered_retired['TRB']*36/filtered_retired['MP']    

retired_per_minute = filtered_retired[['ppm','rpm','apm']]
retired_per_minute.fillna(0,inplace=True)

retired = retired_per_minute.values


labelsone= np.ones(85)
labesszero = np.zeros(93)

labels= np.concatenate((labelsone,labesszero))


data= np.concatenate((hof_input_mat,retired))


data = scale2(data)

#clf = RandomForestClassifier()
#clf = tree.DecisionTreeRegressor()
clf = tree.DecisionTreeClassifier()
#clf = SVC(kernel='linear')
print 'training start'
clf.fit(data,labels)
print 'training end'

#print clf1.coef_
createPickle('hof_prob.pkl', clf)