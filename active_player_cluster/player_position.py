'''Script to extract player id, player name and thier position
'''

import pandas as pd
import numpy as np
import MySQLdb

active_player_data = pd.read_csv('../data/full_advanced_active.csv')

input_data = active_player_data[['pid','pname','Pos']]

player_position=pd.DataFrame(input_data.groupby(['pid','pname','Pos']).size().reset_index(name='count'))

output =  player_position.loc[player_position.groupby(['pid','pname'])['count'].idxmax(), ['pid','pname','Pos'] ]

con = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='mining')

print output.to_sql(con=con, name='player_position', if_exists='replace', flavor='mysql')