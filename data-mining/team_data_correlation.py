import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.stats.stats import pearsonr


teams = pd.read_csv('../data/teamsstat.csv')
opps = pd.read_csv('../data/oppstats.csv')

'''
[u'Season', u'Lg', u'Tm', u'W', u'L', u'Finish', u'Age', u'Ht.', u'Wt.',
       u'G', u'MP', u'FG', u'FGA', u'FG%', u'3P', u'3PA', u'3P%', u'2P',
       u'2PA', u'2P%', u'FT', u'FTA', u'FT%', u'ORB', u'DRB', u'TRB', u'AST',
       u'STL', u'BLK', u'TOV', u'PF', u'PTS', u'year']
'''

#filtering
teams = teams[ teams['Season'] != '2015-16']
opps = opps[ opps['oSeason'] != '2015-16']

teams['year'] = teams['Season'].map( lambda x: x[:4])
teams['year'] = teams['year'].astype(int)

opps['oyear'] = opps['oSeason'].map( lambda x: x[:4])
opps['oyear'] = opps['oyear'].astype(int)


#filtering years

teams = teams[teams['year'] > 1980]
opps = opps[opps['oyear'] > 1980]


combined = pd.concat([teams,opps],axis=1)

'''
c1 = combined['W']-combined['L']
c2 = combined['oW']-combined['oL']

wlcheck = pd.concat([c1,c2],axis=1)

zerocheck=  wlcheck[0] - wlcheck[1]
'''


#print zerocheck

val= combined[['W','oFG%']].values

print val

print pearsonr(val[:,0],val[:,1])
print '-------------'
