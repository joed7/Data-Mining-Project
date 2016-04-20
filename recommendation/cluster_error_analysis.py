import MySQLdb

'''
sg=1
sf=2
pg=3
pf=4
c=5

'''
player_position={}
player_cluster={}

def position_to_cluster(pos):
    if pos =='PF':
        return 3
    elif pos == 'SG':
        return 2
    elif pos == 'PG':
        return 1
    elif pos == 'C':
        return 3
    else:
        return 2
     
def fetchPlayersPosition():
    con = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='mining')
    cursor = con.cursor()
    
    cursor.execute("SELECT pid,pname,Pos FROM player_position") 
    
    result = cursor.fetchall() 
    for r in result:
        pid=int(r[0])
        pname=r[1]
        pos=position_to_cluster(r[2])
        
        player_position[pid]=pos

def fetchClusters():
    con = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='mining')
    cursor = con.cursor()
    
    cursor.execute("SELECT pid,pname,cluster_id FROM clusters_3") 
    
    result = cursor.fetchall() 
    for r in result:
        pid=int(r[0])
        pname=r[1]
        pos=int(r[2])
        
        #print (pid,pname,pos)
        player_cluster[pid]=pos
        

fetchPlayersPosition()  
fetchClusters()      

c=0

for pid,cid1 in player_cluster.items():
    cid2 = player_position[pid]
    
    if cid1 == cid2:
        c=c+1
        
        
print c*1.0/len(player_cluster)

confusion_matrix ={}

for pid,cid1 in player_position.items():
    if pid in player_cluster:
        
        cid2 = player_cluster[pid]
        
        key = (cid1,cid2)
        
        if key in confusion_matrix:
            confusion_matrix[key]=confusion_matrix[key]+1
        else:
            confusion_matrix[key]=1

for k,v in sorted(confusion_matrix.items()):
    print k,v                
    
