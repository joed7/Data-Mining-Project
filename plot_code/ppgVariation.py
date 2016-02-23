import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('ggplot')

def plotPPG():
    
    a_active = pd.read_csv('../data/full_active.csv')
    a_retired=pd.read_csv('../data/full_retired.csv')
    a_hof=pd.read_csv('../data/full_hof.csv')
    
    combined=pd.concat([a_active,a_retired,a_hof])
    combined = combined[ combined['Tm'] != 'TOT' ]
    
    combined['year'] = combined['Season'].map( lambda x: x[:4])
    
    yearpts = pd.DataFrame(combined.groupby('year').aggregate(np.sum)['PTS'])
    
    maxgames = pd.DataFrame(combined.groupby('year').aggregate(np.max)['G'])
    
    
    uniq_season_teams=pd.DataFrame(combined.groupby(['year','Tm']).groups.keys(),columns=['year','teams'])
    
    
    teamcount = pd.DataFrame(uniq_season_teams.groupby('year').size(),columns=['nteams'])
    
    totgames=pd.concat([teamcount,maxgames],axis=1)
    games_played = totgames['nteams']*totgames['G']/2
    games_per_season = pd.DataFrame(games_played,columns=['gps'])
    
    ppg = pd.DataFrame( yearpts['PTS'] / (2*games_per_season['gps']) , columns=['ppg'])
       
    
    last_40_years = ppg[-40:]
    
    last_40_years.plot(xticks=[i for i in range(len(last_40_years.index)) if not i % 2], grid=True)
   
    plt.title('Point per game per team')
    plt.ylabel('PPG')
    plt.show()