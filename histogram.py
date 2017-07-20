# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 05:30:32 2017

@author: BALASUBRAMANIAM
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(size = 5000)
plt.hist(x, normed=True, bins=50)
plt.ylabel('Probability');
#cumulative histogram 
plt.hist(x, 
         bins=100, 
         normed=True,
         stacked=True,
         cumulative=True)
plt.show()
plt.hist(x, 
         bins=100, 
         normed=True, 
         stacked=True, 
         edgecolor="#6A9662",
         color="#DDFFDD")
plt.show()