import string
from bs4 import BeautifulSoup
import requests

f1='../urls/hof.txt'
f2='../urls/retired.txt'
f3='../urls/active.txt'

o1 = open(f1,'w')
o2 = open(f2,'w')
o3 = open(f3,'w')

isactive = False
ishof = False

for char in string.ascii_lowercase:
    url= 'http://www.basketball-reference.com/players/'+char+''
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)
    players= soup.find('table',id,'players') 
    
    if players == None:
        continue
    
    rows= players.find_all('tr')

    
    for (i,row) in enumerate(rows):
        if i == 0:
            continue
        col = row.find_all('td')
        
        if len(col[0].find_all('strong')) == 0:
            isactive = False
        else:
            isactive = True
            
        val = str(col[0]).find('*')
        
        
        if val  != -1:
            ishof = True
        else:
            ishof=False    
        
        #print col[0]     
        u = col[0].find_all('a')[0].get('href')
        #if ishof:
            #o1.write(u+"\n")
            
        print u
            
        if isactive:
            o3.write(u+"\n") 
        else:
            if ishof:
                o1.write(u+"\n")
            else:
                o2.write(u+"\n")
                    
                   
        #print 

print 'done'