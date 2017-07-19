# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 08:46:12 2017

@author: BALASUBRAMANIAM
"""

import numpy as np
import pandas as pd
df= pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2010_alcohol_consumption_by_country.csv")
print(df.keys())
pdata=df[0:10]
print(pdata)
meanValue=np.mean(pdata['alcohol'])
print("Mean Value of Alcohol Consumers %r" %(meanValue))
stdValue=np.std(pdata['alcohol'])
print("STD Value of Alcohol Consumers %r" %(stdValue))
scores = [15, 20, 35, 40, 50]
perc =  np.percentile(scores,80)
print(perc)



