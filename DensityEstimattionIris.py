# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 20:28:44 2017

@author: BALASUBRAMANIAM
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
import seaborn as sns;
mean, cov = [0, 2], [(1, .5), (.5, 1)]
#x, y = np.random.multivariate_normal(mean, cov, size=50).T
#ax = sns.kdeplot(x)
iris = sns.load_dataset("iris")
my_data_frame = pd.DataFrame(iris)
print(my_data_frame.head())


#p=plt.hist(my_data_frame.sepal_length)
sns.set(style="ticks", color_codes=True) # change style
'''
g = sns.pairplot(iris, hue="species")

g = sns.pairplot(iris, kind="reg", hue="species")
'''
setosa = iris.loc[iris.species == "setosa"]
virginica = iris.loc[iris.species == "virginica"]
ax = sns.kdeplot(setosa.sepal_width, setosa.sepal_length,
                  cmap="Reds", shade=True, shade_lowest=False)

ax = sns.kdeplot(virginica.sepal_width, virginica.sepal_length,
                  cmap="Blues", shade=True, shade_lowest=False)
