
import os
import re
from bs4 import BeautifulSoup

data_path1 = '../urls/active/'
data_path2 = '../urls/retired/'
data_path3 = '../urls/hof/'

write_path1 = '../data/active.csv'
write_path2 = '../data/retired.csv'
write_path3 = '../data/hof.csv'


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
#f = open(data_path)

def processHOF(data_path):
    output= ''
    for f1 in sorted(os.listdir(data_path)):
        file_path=os.path.abspath(os.path.join(abs_data_path3,f1))
        players = open(file_path)

                
        soup = BeautifulSoup(players)
        
        pname = soup.find('h1').text

        player_output = ''+str(updateDict(pname))
        player_output = player_output+ ','+ pname +','
        
        rows =soup.find('table',id,'totals').find_all('tr')
        
        iscareer = False
        lastyear =0
        
        for row in rows:
            
            cols = row.find_all('td')
    
            if len(cols) > 0 and cols[0].text == 'Career':
                iscareer =  True
                     
            if iscareer and len(cols) > 0  and cols[3].text == 'NBA':
                
                for col in cols[5:]:
                    player_output = player_output + col.text +','             
                break
        print player_output   
        output = output + player_output +'\n'
        players.close()
        
    write(write_path3,output)        
def processActive(data_path):
    output= ''

    for f1 in sorted(os.listdir(data_path)):
        file_path=os.path.abspath(os.path.join(abs_data_path1,f1))
        players = open(file_path)
        
        soup = BeautifulSoup(players)
        
        pname = soup.find('h1').text
        
        player_output = ''


        player_output = ''+str(updateDict(pname))
        player_output = player_output+','+  pname +','

        
        rows =soup.find('table',id,'totals').find_all('tr')
        
        iscareer = False
        lastyear =0
        
        for row in rows:
            
            cols = row.find_all('td')
    
            if len(cols) > 0 and cols[0].text == 'Career':
                iscareer =  True
                     
            if iscareer and len(cols) > 0  and cols[3].text == 'NBA':
                
                for col in cols[5:]:
                    player_output = player_output + col.text +','             
                                
                break
        print player_output   
            
        output = output + player_output +'\n'
                
        players.close()

    write(write_path1,output)    
def processretired(data_path):
    
    output =""
    for f1 in sorted(os.listdir(data_path)):
        try:
            
            file_path=os.path.abspath(os.path.join(abs_data_path2,f1))
            players = open(file_path)
            print f1
            soup = BeautifulSoup(players)
            
            pname = soup.find('h1').text
            
            player_output = ''+str(updateDict(pname))
            player_output = player_output + ','+pname +','
          
            rows =soup.find('table',id,'totals').find_all('tr')
            
            iscareer = False
            lastyear =0
            
            for row in rows:
                
                cols = row.find_all('td')
        
                if len(cols) > 0 and cols[0].text == 'Career':
                    iscareer =  True
                elif len(cols) > 0 and cols[0].text.find('-') != -1:
                    lastyear = cols[0].text
                         
                if iscareer and len(cols) > 0  and cols[3].text == 'NBA':
                    
                    for col in cols[5:]:
                        #print col.text,        
                        player_output = player_output + col.text +','             
                               
                    break
            #print lastyear
            #print player_output +','+lastyear   
            lyear = lastyear[0:lastyear.find('-')]
            
            output = output + player_output +','+lyear      + '\n'        
            players.close()
    
            write(write_path2,output)   
        except :
            print 'error for '+str(f1)    

print 'begin active'         
processActive(data_path1)
print 'end active'
processretired(data_path2)
print 'end retired'
processHOF(data_path3)
print 'end hof'