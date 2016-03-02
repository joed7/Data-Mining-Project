import os
import re
from bs4 import BeautifulSoup

teams = ['TOR', 'SAC', 'NYK', 'MEM', 'OKC', 'GSW', 'HOU', 'CHA',
       'MIL', 'MIN', 'DET', 'DEN', 'ORL', 'POR', 'DAL', 'NOP', 'PHI',
       'LAC', 'SAS', 'IND', 'BOS','UTA', 'PHO', 'CHI', 'CLE',
       'BRK',  'MIA', 'ATL', 'LAL', 'WAS']



def generateUrls():
    f  = open('../urls/opp_stats.txt','w')
    
    url='http://www.basketball-reference.com/teams/?/opp_stats_totals.html'
    
    for t in teams:
        u= url.replace('?', t)
        f.write(u+"\n")
        
    f.flush()    

generateUrls()        