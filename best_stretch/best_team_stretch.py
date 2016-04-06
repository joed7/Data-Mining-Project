import pandas as pd
import numpy as np

from pandas.io import sql
import MySQLdb
from operator import itemgetter

def insert_team_data():
    stats = pd.read_csv('../data/teamsstat_id.csv')
    
    stats['year'] = stats['Season'].map( lambda x: int(x[:4]))
    stats = stats[ stats['year'] > 1980 ]

    stats['tot'] = stats['W'] + stats['L']
    
    data = stats[['id','year','W','tot']]
    
    con = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='mining')
    
    print data.to_sql(con=con, name='team_stats', if_exists='replace', flavor='mysql')
    con.close()

def insert_team_ids():
    stats = pd.read_csv('../data/team_ids.csv')
    
    print stats
    
    con = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='mining')
    
    print stats.to_sql(con=con, name='team_id', if_exists='replace', flavor='mysql')

    
teams = {}   
results = {}
best_stretch=[]
per_team_best_stretch = {}

def fetchAllTeams():
    con = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='mining')
    cursor = con.cursor()
    
    cursor.execute("SELECT * FROM team_id") 
    
    result = cursor.fetchall() 
    for r in result:
        teams[int(r[1])]= r[2]

def fetchTeamRecord(id):
    con = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='mining')
    cursor = con.cursor()
    
    cursor.execute("SELECT year,W,tot FROM team_stats where year != 2015 and id="+str(id)+" order by year") 
    
    result = cursor.fetchall() 
    
    t_result = []
    for r in result:
        t_result.append(r)    
        
    results[id]=t_result
    
    con.close()
    



def processResult(id,year,arr):
    tot_w = 0
    tot_gm = 0
    
    for i in arr:
        tot_w = tot_w + i[1]
        tot_gm = tot_gm + i[2]
    
    wp =    tot_w *100.0/ tot_gm 
    
    #over_all stretch
    best_stretch.append( (id,year,wp) )
    
    #per team stretch
    if id in per_team_best_stretch:
        per_team_best_stretch[id].append( (id,year,wp))
    else:
        per_team_best_stretch[id]=[]
        per_team_best_stretch[id].append( (id,year,wp))
            
def get_worst_stretch(best_stretch):
    s = sorted(best_stretch, key=itemgetter(2))
    return s

        
def get_best_stretch(best_stretch):
    s = sorted(best_stretch, key=itemgetter(2),reverse=True)
    return s

        
def printTopX(rec,num):
    for b in rec[0:num]:
        y = b[1]
        id = b[0]
        wp = b[2]
        team = teams[id]
        
        tuple = (team,str(y)+'-'+str(y+4),wp)
        print tuple       
     
       
fetchAllTeams()
#fetchTeamRecord(1)


for  id in teams.keys():
    fetchTeamRecord(id)
    
for id in results.keys():
    res = results[id]
    
    for i in range(len(res)):
        j = i+5
        start_year = res[i][0]
        
        if j <= len(res):
            end_year = res[j-1][0]
            
            result_window = res[i:j]
            processResult(id, start_year, result_window)
            
'''
r = get_worst_stretch(best_stretch)
printTopX(r,50)
'''
            
for t_id in per_team_best_stretch:
    s = get_worst_stretch(per_team_best_stretch[t_id])
    printTopX(s,1)
        
