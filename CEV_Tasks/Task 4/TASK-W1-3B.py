import numpy as np
import pandas as pd 

data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])

x = heights.max()
y = heights.min()

state1 = np.array(data['height(cm)'] == x)
state2 = np.array(data['height(cm)'] == y)

s1 = data.loc[state1]
s2 = data.loc[state2]

display(pd.concat([s1, s2]))