
import os
import re
from bs4 import BeautifulSoup

data_path1 = '../urls/backup/active/'
data_path2 = '../urls/backup/retired/'
data_path3 = '../urls/backup/hof/'

write_path1 = '../data/full_advanced_active.csv'
write_path2 = '../data/full_advanced_retired.csv'
write_path3 = '../data/full_advanced_hof.csv'



cups_path = '../data/cups.text'
pattern=r'([0-9]+)'


abs_data_path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), data_path1))
abs_data_path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), data_path2))
abs_data_path3 = os.path.abspath(os.path.join(os.path.dirname(__file__), data_path3))

counter =0
d={}
def write(write_path,output):
    f = open(write_path,'w')
    f.write(output)
    f.close()

def updateDict(player):
    global counter
    d[counter] = player
    counter = counter + 1
    return counter;

def process(abs_data_path,data_path,write_path):
    output= ''

    for f1 in sorted(os.listdir(data_path)):
        print f1
        file_path=os.path.abspath(os.path.join(abs_data_path,f1))
        players = open(file_path)
        
        soup = BeautifulSoup(players,"lxml")
        
        pname = soup.find('h1').text
        
        player_output = ''


        pid = ''+str(updateDict(pname))

        
        
        rows =soup.find(id="advanced").find_all('tr')
        
        iscareer = False
        lastyear =0
        
        for row in rows:
            
            cols = row.find_all('td')
            
            
            
            if len(cols) == 0:
                continue
            
            

            if len(cols) > 0 and cols[0].text == 'Career':
                break
            seaon_output = pid+','+  pname +','
        
                     
            if len(cols) >= 4   and cols[3].text == 'NBA':
                for i,col in enumerate(cols):
                    if i == 0:
                        seaon_output = seaon_output + col.text[0:7] +','
                        continue 
                    seaon_output = seaon_output + col.text +','   
                
                #print seaon_output
                              
                player_output =player_output + seaon_output+"\n"
                                
        #print player_output   
            
        output = output + player_output
        
                
        players.close()
    write(write_path,output)   
        
print 'begin active'         
process(data_path1,abs_data_path1,write_path1)
print 'end active'
process(data_path2,abs_data_path2,write_path2)
print 'end retired'
process(data_path3,abs_data_path3,write_path3)
print 'end hof'