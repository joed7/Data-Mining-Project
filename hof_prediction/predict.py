import pickle
import pandas as pd
import numpy as np
import sys
from inspect import getmembers
from sklearn import tree
from sklearn.svm import SVC

def descale(rawpoints,scaled_points, high=100.0, low=0.0):
    
    mins = np.min(rawpoints, axis=0)
    maxs = np.max(rawpoints, axis=0)
    
    rng = maxs - mins
    
    return (scaled_points * rng/100) + mins 

features =[]    

def getDescaled(val,index):
 
 
    mins=np.array([ 4.66378148 ,1.89001565 ,0.5262438 ])
    maxs = np.array([ 28.3463461 ,19.11113294 ,11.91307261])

    rng = maxs - mins
    
       
    v = features[index]
    
    if v == 'points':
        rng_va = rng[0]
        min_v = mins[0]
        return (val * rng_va/100) + min_v
    elif v == 'rebounds':
        rng_va = rng[1]
        min_v = mins[1]
        return (val * rng_va/100) + min_v
    else:
        rng_va = rng[2]
        min_v = mins[2]
        return (val * rng_va/100) + min_v        
        
def print_decision_tree(tree, feature_names=None, offset_unit='    '):
    '''Plots textual representation of rules of a decision tree
    tree: scikit-learn representation of tree
    feature_names: list of feature names. They are set to f1,f2,f3,... if not specified
    offset_unit: a string of offset of the conditional block'''

    global features
    
    left      = tree.tree_.children_left
    right     = tree.tree_.children_right
    threshold = tree.tree_.threshold
    value = tree.tree_.value
    if feature_names is None:
        features  = ['f%d'%i for i in tree.tree_.feature]
    else:
        features  = [feature_names[i] for i in tree.tree_.feature]        
    
    print features
    
    def recurse(left, right, threshold, features, node, depth=0):
            offset = offset_unit*depth
            if (threshold[node] != -2):
                    print(offset+"if ( " + features[node] + " <= " + str(getDescaled(threshold[node],node)) + " ) {")
                    if left[node] != -1:
                            recurse (left, right, threshold, features,left[node],depth+1)
                    print(offset+"} else {")
                    if right[node] != -1:
                            recurse (left, right, threshold, features,right[node],depth+1)
                    print(offset+"}")
            else:
                    print(offset+"return " + str(value[node]))

    recurse(left, right, threshold, features, 0,0)
            
fileObject = open('hof_prob.pkl','r')  
model = pickle.load(fileObject)  
fileObject.close()


tree.export_graphviz(model,out_file='tree.dot')
print_decision_tree(model,['points','rebounds','assists'])



analomy = pd.read_csv('../data/retired.csv')
analomy = analomy[analomy['MP'] > 10000]

def scale2(rawpoints, high=100.0, low=0.0):
    mins=np.array([ 4.66378148 ,1.89001565 ,0.5262438 ])
    maxs = np.array([ 28.3463461 ,19.11113294 ,11.91307261])
    
    rng = maxs - mins
    return (rawpoints - mins)*100.0 / rng

    
    
        

hof_anamoly={}
analomy = analomy.sort(columns=['PTS'],ascending=False)

for index, row in analomy.iterrows():
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
    
    print hof_input_data['pname'],
    print v1,
    print model.predict(data) == 1   
