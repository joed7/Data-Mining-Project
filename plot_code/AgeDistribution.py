import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('ggplot')

a_active = pd.read_csv('../data/full_active.csv')
a_retired=pd.read_csv('../data/full_retired.csv')
a_hof=pd.read_csv('../data/full_hof.csv')

combined=pd.concat([a_active,a_retired,a_hof])
combined = combined[ combined['Tm'] != 'TOT' ]

combined['Age'].plot(kind='hist',bins=[18+x for x in range(25)])

plt.ylabel('No of Players')
plt.xlabel('Age')
plt.title('Age distribution Histogram in the nba')
plt.show()