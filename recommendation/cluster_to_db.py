'''script to put clusters in db
'''

import pandas as pd
import numpy as np
import MySQLdb

for i in range(3):
    cluster_file='cluster'+str(i+1)+'.csv'
    cluster_data = pd.read_csv(cluster_file)
    #del cluster_data['index']
    #del cluster_data['dist']
        
    cluster_id = np.empty(len(cluster_data.index))
    cluster_id.fill(i+1)
    cluster = pd.DataFrame(cluster_id,columns=['cluster_id'])
    
    output= pd.concat([cluster_data,cluster],axis=1)
    

    con = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='mining')
    
    print output.to_sql(con=con, name='clusters_3', if_exists='append', flavor='mysql')    
    

print 'Done'