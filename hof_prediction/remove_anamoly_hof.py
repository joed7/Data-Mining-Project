import pandas as pd
import numpy as np
import pickle

analomy = pd.read_csv('../anamoly/anamoly_cluster_2.csv')

hof_anamoly={}

for index, row in analomy.iterrows():
     hof_anamoly[row['pname']]=1
                 
                 

hof_data = pd.read_csv('../data/hof.csv')
            
hof_players = []                 
for index, row in hof_data.iterrows():
     if not row['pname'] in hof_anamoly:
         hof_players.append(row)
         
hof_without_anomoly =  pd.DataFrame(hof_players)         


hof_without_anomoly.to_csv('hof_without_anomoly.csv',index = False)



