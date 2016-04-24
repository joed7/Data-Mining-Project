import pickle
import pandas as pd
import numpy as np
import sys
from inspect import getmembers
from sklearn import tree
from sklearn.svm import SVC


features =[]    

            
fileObject = open('hof_prob.pkl','r')  
model = pickle.load(fileObject)  
fileObject.close()

#tree.export_graphviz(model,out_file='tree.dot')
#print_decision_tree(model,['points','rebounds','assists'])


def scale2(rawpoints, high=100.0, low=0.0):
    mins=np.array([ 4.66378148 ,1.89001565 ,0.5262438 ])
    maxs = np.array([ 28.3463461 ,19.11113294 ,11.91307261])
    
    rng = maxs - mins
    return (rawpoints - mins)*100.0 / rng

    
    
hof_wo_outlier = pd.read_csv('hof_without_anomoly.csv')

tp=0
fn=0

for index, row in hof_wo_outlier.iterrows():
    each_row = row[['pid','pname','MP','PTS','TRB','AST']]       
    
    each_row['ppm'] = each_row['PTS']*36.0/each_row['MP']
    each_row['apm'] = each_row['AST']*36.0/each_row['MP']
    each_row['rpm'] = each_row['TRB']*36.0/each_row['MP']

    each_row['ippm'] = each_row['PTS']*36/each_row['MP']
    each_row['iapm'] = each_row['AST']*36/each_row['MP']
    each_row['irpm'] = each_row['TRB']*36/each_row['MP']

    
    each_row.fillna(0,inplace=True)
    v= each_row[['ppm','rpm','apm']].values
    v1= each_row[['ippm','irpm','iapm']].values
    
    data = scale2(v)
    
    '''
    if model.predict(data) == 1:
        print each_row['pname'],
        print v1

    
    print each_row['pname'],
    print v1,
    print model.predict(data) == 1   
    '''
    
    if model.predict(data) == 1:
        tp=tp+1
    else:
        fn=fn+1



retired = pd.read_csv('../data/retired.csv')
filtered_retired = retired[ retired['lyear'] < 2007][retired['MP'] > 25000][retired['lyear'] > 1980][['pid','pname','MP','PTS','TRB','AST']]
filtered_retired.fillna(0,inplace=True)

tn=0
fp=0


for index, row in filtered_retired.iterrows():
    each_row = row[['pid','pname','MP','PTS','TRB','AST']]       
    
    each_row['ppm'] = each_row['PTS']*36.0/each_row['MP']
    each_row['apm'] = each_row['AST']*36.0/each_row['MP']
    each_row['rpm'] = each_row['TRB']*36.0/each_row['MP']

    each_row['ippm'] = each_row['PTS']*36/each_row['MP']
    each_row['iapm'] = each_row['AST']*36/each_row['MP']
    each_row['irpm'] = each_row['TRB']*36/each_row['MP']

    
    each_row.fillna(0,inplace=True)
    v= each_row[['ppm','rpm','apm']].values
    v1= each_row[['ippm','irpm','iapm']].values
    
    data = scale2(v)
    
    '''
    if model.predict(data) == 1:
        print each_row['pname'],
        print v1
    
    
    print each_row['pname'],
    print v1,
    print model.predict(data) == 1   
    '''
    if model.predict(data) == 1:
        fp=fp+1
        #print each_row['pname'],
        #print v1,
        #print model.predict(data) == 1          
    else:
        tn=tn+1
    
                        
print '---------final result------------'

print "True positive:" + str(tp)
print "False negative:" + str(fn)               
print "True negative:" + str(tn)
print "False positive:" + str(fp)               
        

print '----------Active Player HOF prediction-----'

active_players = pd.read_csv('../data/active.csv')
active_players = active_players[active_players['MP'] > 10000]

active_players = active_players.sort(columns=['PTS'],ascending=False)

actve_hof=[]

for index, row in active_players.iterrows():
    hof_input_data = row[['pid','pname','MP','PTS','TRB','AST']]       
    
    hof_input_data['ppm'] = hof_input_data['PTS']*36.0/hof_input_data['MP']
    hof_input_data['apm'] = hof_input_data['AST']*36.0/hof_input_data['MP']
    hof_input_data['rpm'] = hof_input_data['TRB']*36.0/hof_input_data['MP']

    hof_input_data['ippm'] = hof_input_data['PTS']*36/hof_input_data['MP']
    hof_input_data['iapm'] = hof_input_data['AST']*36/hof_input_data['MP']
    hof_input_data['irpm'] = hof_input_data['TRB']*36/hof_input_data['MP']

    
    hof_input_data.fillna(0,inplace=True)
    v= hof_input_data[['ppm','rpm','apm']].values
    v1= hof_input_data[['ippm','irpm','iapm']].values
    
    data = scale2(v)
    
    '''
    if model.predict(data) == 1:
        print hof_input_data['pname'],
        print v1
    '''
    
    if model.predict(data) == 1 :
        print hof_input_data['pname'],
        print v1
        actve_hof.append(v)

print '------------------average stats---------'
final_array = np.array(actve_hof)

print np.average(final_array,axis=0)

print '--------------------total selection------------'

print len(final_array)