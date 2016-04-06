import os
import re
from bs4 import BeautifulSoup

data_path1 = '../urls/teamstats'
abs_data_path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), data_path1))


def process():
    output= ''

    c=0
    for f1 in sorted(os.listdir(data_path1)):
        c = c+1
        file_path=os.path.abspath(os.path.join(abs_data_path1,f1))
        players = open(file_path)
        
        soup = BeautifulSoup(players,"lxml")
        
        stats =  soup.find('table',id,'team_stats_totals')
        rows = stats.find_all('tr')

        out = ''
        
        for row in rows:
            cols = row.find_all('td')
            
            if len(cols) > 0:
                if cols[1].text != 'NBA':
                    continue
                
                for i,col in enumerate(cols):
                    out = out  +col.text+","
                    if i == 2:
                        print str(c)+','+col.text
                
                out = out + str(c) + '\n'  
        output = output + out
        #print out
                    
    f = open('../data/teamsstat_id.csv','w')
    f.write(output)
    
process()        