# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 10:25:19 2017

@author: BALASUBRAMANIAM
"""

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import random
df = pd.DataFrame(columns=('Time', 'Distance'))
print(df)
start_date=dt.datetime(2017,1,13)
end_date=dt.datetime(2017,1,27)
daterange = pd.date_range(start_date, end_date)
#print(daterange)
for single_date in daterange:
    
    row = dict(zip(['Time', 'Distance'],
     [single_date,
     int(50*np.random.randint(1,100))]))
    #print(row)
    row_s = pd.Series(row)
    row_s.name = single_date.strftime('%b %d')
    df = df.append(row_s)

print(df)

str_startDate=start_date.strftime("%m %d")
str_endDate=end_date.strftime("%m %d")
df.ix['Jan 13':'Jan 27', ['Time', 'Distance']].plot()
plt.ylim(0, 10000)
plt.xlabel('Time')
plt.ylabel('Distance')
plt.title('Plotting Time vs Distance')
plt.show()






