import pandas as pd
from operator import itemgetter
import sys

best_stretch=[]
per_player_best_stretch = {}

def processResult(id,year,arr):
    tot_per = 0
    
    for i in arr:
        tot_per = tot_per + i[2]
    
    
    #over_all stretch
        
    best_stretch.append( (id,year,tot_per) )
    
    #per team stretch
    if id in per_player_best_stretch:
        per_player_best_stretch[id].append( (id,year,tot_per))
    else:
        per_player_best_stretch[id]=[]
        per_player_best_stretch[id].append( (id,year,tot_per))
            

def overlap(tf1,tf2):
    a = tf1.split('-')
    b = tf2.split('-')
    
    s1,e1=a[0],a[1]
    s2,e2=b[0],b[1]
    
    if s1 > e2 or e1 < s2:
        return False
    return True
    
        
                 
a_active = pd.read_csv('../data/full_advanced_active.csv')
a_retired=pd.read_csv('../data/full_advanced_retired.csv')
a_hof=pd.read_csv('../data/full_advanced_hof.csv')

combined=pd.concat([a_active,a_retired,a_hof])
#combined = a_active

combined['year'] = combined['Season'].map( lambda x: int(x[:4]))

#combined =combined [ combined['year'] != 2015 ]
combined = combined [combined['MP'] > 500 ]

data = combined [ ['pid','pname','PER','year','Tm'] ]
data.fillna(0,inplace=True)

stats={}

ids = {}
names={}
for i,row in data.iterrows():
    
    name=row['pname']
    id=row['pid']
    
    names[id]=name
    
    per=row['PER']
    y=row['year']
    tm=row['Tm']
    
    tup = (id,y)
    if not tup in stats:
        stats[tup]=per

pers = []

for t in stats.keys():
    per_tuple = ( t[0],t[1],stats[t])
    pers.append(per_tuple)

#s = sorted(pers, key=itemgetter(0,1))

per_result = {}

for p in pers:
    if p[0] in per_result:
        per_result[p[0]].append(p)
    else:
        per_result[p[0]]=[]
        per_result[p[0]].append(p)



for id in per_result.keys():
    res = per_result[id]

    res = sorted(res, key=itemgetter(1))
    
    for i in range(len(res)):
        j = i+5
        start_year = res[i][1]
        
        if j <= len(res):
            end_year = res[j-1][1]
            
            result_window = res[i:j]
            processResult(id, start_year, result_window)
                        

s = sorted(best_stretch, key=itemgetter(2),reverse=True)

fin_output = []

index = 0

player_stretch={}

while True:
    if index == len(s):
        break
    
    k = s[index]
    id = k[0]
    name = names[k[0]]
    year = k[1]
    per = int(k[2])
    
    index = index+1
    
    
    
    if not id in player_stretch:
        fin_output.append( (name,str(year)+'-'+str(year+4),per) )
        player_stretch[id]=[]
        player_stretch[id].append(str(year)+'-'+str(year+4))
    else:
        cur_peroid = str(year)+'-'+str(year+4)
        
        prev_periods =   player_stretch[id]
        
        is_overlap = False
        
        for pp in prev_periods:
            if overlap(pp, cur_peroid):
                is_overlap = True
                
        if not is_overlap:
            fin_output.append( (name,str(year)+'-'+str(year+4),per) )
            player_stretch[id].append(str(year)+'-'+str(year+4))
            
            
for i in  fin_output[:200]:
    print i               
