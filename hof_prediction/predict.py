import pickle
import pandas as pd
import numpy as np


fileObject = open('hof_prob.pkl','r')  
model = pickle.load(fileObject)  
fileObject.close()


analomy = pd.read_csv('../data/hof.csv')

def scale2(rawpoints, high=100.0, low=0.0):
    mins=np.array([ 4.66378148 ,1.89001565 ,0.5262438 ])
    maxs = np.array([ 28.3463461 ,19.11113294 ,11.91307261])
    
    rng = maxs - mins
    return (rawpoints - mins)*100.0 / rng

    
    
        
        
hof_anamoly={}

for index, row in analomy.iterrows():
    hof_input_data = row[['pid','pname','MP','PTS','TRB','AST']]       
    
    hof_input_data['ppm'] = hof_input_data['PTS']*36/hof_input_data['MP']
    hof_input_data['apm'] = hof_input_data['AST']*36/hof_input_data['MP']
    hof_input_data['rpm'] = hof_input_data['TRB']*36/hof_input_data['MP']
    hof_input_data.fillna(0,inplace=True)
    v= hof_input_data[['ppm','rpm','apm']].values
    
    data = scale2(v)
    
    
    if model.predict(data) != 1:
        print hof_input_data['pname'],
        print v
                      