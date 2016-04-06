import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.stats.stats import pearsonr   
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
    
def plotAssist():
    
    a_active = pd.read_csv('../data/full_active.csv')
    a_retired=pd.read_csv('../data/full_retired.csv')
    a_hof=pd.read_csv('../data/full_hof.csv')
    
    combined=pd.concat([a_active,a_retired,a_hof])
    combined = combined[ combined['Tm'] != 'TOT' ]
    
    
#combined['Age'].plot(kind='hist',bins=[18+x for x in range(25)])    
    
    combined['year'] = combined['Season'].map( lambda x: x[:4])
    
    yearassist = pd.DataFrame(combined.groupby('year').aggregate(np.sum)['AST'])
    
    maxgames = pd.DataFrame(combined.groupby('year').aggregate(np.max)['G'])
    
    
    uniq_season_teams=pd.DataFrame(combined.groupby(['year','Tm']).groups.keys(),columns=['year','teams'])
    
    
    teamcount = pd.DataFrame(uniq_season_teams.groupby('year').size(),columns=['nteams'])
    
    totgames=pd.concat([teamcount,maxgames],axis=1)
    games_played = totgames['nteams']*totgames['G']/2
    games_per_season = pd.DataFrame(games_played,columns=['gps'])
    
    ppg = pd.DataFrame( yearassist['AST'] / (2*games_per_season['gps']) , columns=['APG'])
       
    
    last_40_years = ppg[-40:]
    
    last_40_years.plot(xticks=[i for i in range(len(last_40_years.index)) if not i % 2], grid=True)
   
    plt.title('Assists per game per team')
    plt.ylabel('APG')
    plt.show()    

def plotRebounds():
    
    a_active = pd.read_csv('../data/full_active.csv')
    a_retired=pd.read_csv('../data/full_retired.csv')
    a_hof=pd.read_csv('../data/full_hof.csv')
    
    combined=pd.concat([a_active,a_retired,a_hof])
    combined = combined[ combined['Tm'] != 'TOT' ]
    
    combined['year'] = combined['Season'].map( lambda x: x[:4])
    
    yearRBDS = pd.DataFrame(combined.groupby('year').aggregate(np.sum)['ORB'])
    
    maxgames = pd.DataFrame(combined.groupby('year').aggregate(np.max)['G'])
    
    
    uniq_season_teams=pd.DataFrame(combined.groupby(['year','Tm']).groups.keys(),columns=['year','teams'])
    
    
    teamcount = pd.DataFrame(uniq_season_teams.groupby('year').size(),columns=['nteams'])
    
    totgames=pd.concat([teamcount,maxgames],axis=1)
    games_played = totgames['nteams']*totgames['G']/2
    games_per_season = pd.DataFrame(games_played,columns=['gps'])
    
    ppg = pd.DataFrame( yearRBDS['ORB'] / (2*games_per_season['gps']) , columns=['RBG'])
       
    
    last_40_years = ppg[-40:]
    
    last_40_years.plot(xticks=[i for i in range(len(last_40_years.index)) if not i % 2], grid=True)
   
    plt.title('Rebounds per game per team')
    plt.ylabel('RBG')
    plt.show()    

def plotFGP():
    a_active = pd.read_csv('../data/full_active.csv')
    a_retired=pd.read_csv('../data/full_retired.csv')
    a_hof=pd.read_csv('../data/full_hof.csv')
    
    combined=pd.concat([a_active,a_retired,a_hof])
    combined = combined[ combined['Tm'] != 'TOT' ]
    
    combined['year'] = combined['Season'].map( lambda x: x[:4])
    
    yearFG = pd.DataFrame(combined.groupby('year').aggregate(np.sum)['FG'])
    yearFGA = pd.DataFrame(combined.groupby('year').aggregate(np.sum)['FGA'])
    
    yearFGP = pd.DataFrame(yearFG['FG']/yearFGA['FGA'],columns=['fgp'])
    
       
    
    last_40_years = yearFGP[-40:]
    
    last_40_years.plot(xticks=[i for i in range(len(last_40_years.index)) if not i % 2], grid=True)
   
    plt.title('Field Goal %ge')
    plt.ylabel('FG%')
    plt.show()        
    

def plot3P():
    a_active = pd.read_csv('../data/full_active.csv')
    a_retired=pd.read_csv('../data/full_retired.csv')
    a_hof=pd.read_csv('../data/full_hof.csv')
    
    combined=pd.concat([a_active,a_retired,a_hof])
    combined = combined[ combined['Tm'] != 'TOT' ]
    
    combined['year'] = combined['Season'].map( lambda x: x[:4])
    
    yearFG = pd.DataFrame(combined.groupby('year').aggregate(np.sum)['3P'])
    yearFGA = pd.DataFrame(combined.groupby('year').aggregate(np.sum)['3PA'])
    
    yearFGP = pd.DataFrame(yearFG['3P']/yearFGA['3PA'],columns=['3fgp'])
    

    
    last_40_years = yearFGP[-40:]
    
    last_40_years.plot(xticks=[i for i in range(len(last_40_years.index)) if not i % 2], grid=True)
   
    plt.title('3 Point percentage by season')
    plt.ylabel('3 point%')
    plt.show()        
            

def plot2P():
    a_active = pd.read_csv('../data/full_active.csv')
    a_retired=pd.read_csv('../data/full_retired.csv')
    a_hof=pd.read_csv('../data/full_hof.csv')
    
    combined=pd.concat([a_active,a_retired,a_hof])
    combined = combined[ combined['Tm'] != 'TOT' ]
    
    combined['year'] = combined['Season'].map( lambda x: x[:4])
    
    yearFG = pd.DataFrame(combined.groupby('year').aggregate(np.sum)['2P'])
    yearFGA = pd.DataFrame(combined.groupby('year').aggregate(np.sum)['2PA'])
    
    yearFGP = pd.DataFrame(yearFG['2P']/yearFGA['2PA'],columns=['2FGP'])
    

    
    last_40_years = yearFGP[-40:]
    
    last_40_years.plot(xticks=[i for i in range(len(last_40_years.index)) if not i % 2], grid=True)
   
    plt.title('2 Point percentage by season')
    plt.ylabel('2 point%')
    plt.show()        

def plotFGA():
    a_active = pd.read_csv('../data/full_active.csv')
    a_retired=pd.read_csv('../data/full_retired.csv')
    a_hof=pd.read_csv('../data/full_hof.csv')
    
    combined=pd.concat([a_active,a_retired,a_hof])
    combined = combined[ combined['Tm'] != 'TOT' ]
    
    combined['year'] = combined['Season'].map( lambda x: x[:4])
    
    yearFGA = pd.DataFrame(combined.groupby('year').aggregate(np.sum)['FGA'])
    
    maxgames = pd.DataFrame(combined.groupby('year').aggregate(np.max)['G'])
    
    
    uniq_season_teams=pd.DataFrame(combined.groupby(['year','Tm']).groups.keys(),columns=['year','teams'])
    teamcount = pd.DataFrame(uniq_season_teams.groupby('year').size(),columns=['nteams'])
    totgames=pd.concat([teamcount,maxgames],axis=1)
    games_played = totgames['nteams']*totgames['G']/2
    games_per_season = pd.DataFrame(games_played,columns=['gps'])
    
    FGpreGame = pd.DataFrame( yearFGA['FGA'] / (2* games_per_season['gps']) , columns=['fga'])
       

    
    last_40_years = FGpreGame[-40:]
    
    last_40_years.plot(xticks=[i for i in range(len(last_40_years.index)) if not i % 2], grid=True)
   
    plt.title('Field Goals Attempted Per Team Per Game')
    plt.ylabel('FGA')
    plt.show()       

def plot2PA():
    a_active = pd.read_csv('../data/full_active.csv')
    a_retired=pd.read_csv('../data/full_retired.csv')
    a_hof=pd.read_csv('../data/full_hof.csv')
    
    combined=pd.concat([a_active,a_retired,a_hof])
    combined = combined[ combined['Tm'] != 'TOT' ]
    
    combined['year'] = combined['Season'].map( lambda x: x[:4])
    
    yearFGA = pd.DataFrame(combined.groupby('year').aggregate(np.sum)['2PA'])
    
    maxgames = pd.DataFrame(combined.groupby('year').aggregate(np.max)['G'])
    
    
    uniq_season_teams=pd.DataFrame(combined.groupby(['year','Tm']).groups.keys(),columns=['year','teams'])
    teamcount = pd.DataFrame(uniq_season_teams.groupby('year').size(),columns=['nteams'])
    totgames=pd.concat([teamcount,maxgames],axis=1)
    games_played = totgames['nteams']*totgames['G']/2
    games_per_season = pd.DataFrame(games_played,columns=['gps'])
    
    FGpreGame = pd.DataFrame( yearFGA['2PA'] / (2* games_per_season['gps']) , columns=['2PA'])
       

    
    last_40_years = FGpreGame[-40:]
    
    last_40_years.plot(xticks=[i for i in range(len(last_40_years.index)) if not i % 2], grid=True)
   
    plt.title('2 Points Attempted Per Team Per Game')
    plt.ylabel('2PA')
    plt.show()       
            
def plot3PA():
    a_active = pd.read_csv('../data/full_active.csv')
    a_retired=pd.read_csv('../data/full_retired.csv')
    a_hof=pd.read_csv('../data/full_hof.csv')
    
    combined=pd.concat([a_active,a_retired,a_hof])
    combined = combined[ combined['Tm'] != 'TOT' ]
    
    combined['year'] = combined['Season'].map( lambda x: x[:4])
    
    yearFGA = pd.DataFrame(combined.groupby('year').aggregate(np.sum)['3PA'])
    
    maxgames = pd.DataFrame(combined.groupby('year').aggregate(np.max)['G'])
    
    
    uniq_season_teams=pd.DataFrame(combined.groupby(['year','Tm']).groups.keys(),columns=['year','teams'])
    teamcount = pd.DataFrame(uniq_season_teams.groupby('year').size(),columns=['nteams'])
    totgames=pd.concat([teamcount,maxgames],axis=1)
    games_played = totgames['nteams']*totgames['G']/2
    games_per_season = pd.DataFrame(games_played,columns=['gps'])
    
    FGpreGame = pd.DataFrame( yearFGA['3PA'] / (2* games_per_season['gps']) , columns=['3PA'])
       

    
    last_40_years = FGpreGame[-40:]
    
    last_40_years.plot(xticks=[i for i in range(len(last_40_years.index)) if not i % 2], grid=True)
   
    plt.title('3 Points Attempted Per Team Per Game')
    plt.ylabel('3PA')
    plt.show()       
                                    
def plotAge():
    
    a_active = pd.read_csv('../data/full_active.csv')
    a_retired=pd.read_csv('../data/full_retired.csv')
    a_hof=pd.read_csv('../data/full_hof.csv')
    
    combined=pd.concat([a_active,a_retired,a_hof])
    
    combined['year'] = combined['Season'].map( lambda x: x[:4])
    
    
    combined = combined[ (combined['Tm'] != 'TOT') & (combined['MP'] >= 1200) & (combined['year'] != '2011') & (combined['year'] != '2015')] 
    
    
    #yearage = pd.DataFrame();
    
    yearage = pd.DataFrame( combined.groupby(['year','pid','Age']).groups.keys(),
                            columns=['year','pid','Age'] )[['year','Age']]    
                            
    year_age_mean = yearage.groupby('year').agg(np.mean)
    
    
    
    #year_age_mean.plot(xticks=[i for i in range(len(year_age_mean.index)) if not i % 2], grid=True)
    year_age_mean.plot()
    plt.title('Avg age of NBA teams')
    plt.ylabel('Avg Age')
    plt.show()   

def plotAge():
    
    a_active = pd.read_csv('../data/full_active.csv')
    a_retired=pd.read_csv('../data/full_retired.csv')
    a_hof=pd.read_csv('../data/full_hof.csv')
    
    combined=pd.concat([a_active,a_retired,a_hof])
    
    combined['year'] = combined['Season'].map( lambda x: x[:4])
    
    
    combined = combined[ (combined['Tm'] != 'TOT') & (combined['MP'] >= 1000)] 
    
    agepts = combined[['Age','PTS']]
    
    
    #yearage = pd.DataFrame();
    
    yearage = pd.DataFrame( agepts.groupby(['Age']).aggregate(np.mean) )  
                            
    year_age_mean = yearage.groupby(['year','Tm']).size()
    
    
    
    #year_age_mean.plot(xticks=[i for i in range(len(year_age_mean.index)) if not i % 2], grid=True)
    year_age_mean.plot()
    plt.title('Avg age of NBA teams')
    plt.ylabel('Avg Age')
    plt.show()          


plot3PA()