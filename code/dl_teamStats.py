import os
import re
from bs4 import BeautifulSoup

teams = ['TOR', 'SAC', 'NYK', 'MEM', 'OKC', 'GSW', 'HOU', 'CHA',
       'MIL', 'MIN', 'DET', 'DEN', 'ORL', 'POR', 'DAL', 'NOP', 'PHI',
       'LAC', 'SAS', 'IND', 'BOS', 'NOH', 'UTA', 'PHO', 'CHI', 'CLE',
       'BRK', 'NOK', 'MIA', 'NJN', 'ATL', 'LAL', 'WAS', 'CHO', 'SEA']



def generateUrls():
    f  = open('../urls/team_stats.txt','w')
    
    url='http://www.basketball-reference.com/teams/?/stats_totals.html'
    
    for t in teams:
        u= url.replace('?', t)
        f.write(u+"\n")
        
    f.flush()    

generateUrls()        