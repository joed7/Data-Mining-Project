import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('ggplot')

def plotNoOfPlyaers():
    a_active = pd.read_csv('../data/full_active.csv')
    a_retired=pd.read_csv('../data/full_retired.csv')
    a_hof=pd.read_csv('../data/full_hof.csv')
    
    
    combined=pd.concat([a_active,a_retired,a_hof])
    
    uniq_season_players=pd.DataFrame(combined.groupby(['Season','pname']).groups.keys(),columns=['season','player'])
    
    uniq_season_players['year'] = uniq_season_players['season'].map( lambda x: x[:4])
    
    #print uniq_season_players
    
    
    playercount = pd.DataFrame(uniq_season_players.groupby('year').size(),columns=['no of players'])
    #playercount = pd.DataFrame(uniq_season_players.groupby('season').size().keys(),columns=['season','player'])
    
    
    playercount.plot(xticks=[i for i in range(len(playercount.index)) if not i % 2], grid=True)
    plt.title('No of players in the NBA')
    plt.ylabel('No of players')
    plt.show()

def plotNoTeams():
    a_active = pd.read_csv('../data/full_active.csv')
    a_retired=pd.read_csv('../data/full_retired.csv')
    a_hof=pd.read_csv('../data/full_hof.csv')
    
    
    combined=pd.concat([a_active,a_retired,a_hof])
    combined = combined[ combined['Tm'] != 'TOT' ]
    
    uniq_season_teams=pd.DataFrame(combined.groupby(['Season','Tm']).groups.keys(),columns=['season','teams'])
    
    uniq_season_teams['year'] = uniq_season_teams['season'].map( lambda x: x[:4])
    
    #print uniq_season_players
    
    
    teamcount = pd.DataFrame(uniq_season_teams.groupby('year').size(),columns=['no of teams'])
    
    teamcount.plot(xticks=[i for i in range(len(teamcount.index)) if not i % 2], grid=True)
    plt.title('No of Teams in the NBA')
    plt.ylabel('No of Teams')
    plt.show()
    
plotNoOfPlyaers()
plotNoTeams()
    
'''
t = plotNoTeams()
p = plotNoOfPlyaers()


df = pd.concat([t,p],axis=1)



df.plot(xticks=[i for i in range(len(t.index)) if not i % 2], grid=True)
#plt.title('No of Teams in the NBA')
#plt.ylabel('No of Teams')
plt.show()
'''