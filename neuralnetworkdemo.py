# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 19:57:13 2017

@author: BALASUBRAMANIAM
"""

import pandas as pd
#cultivator does labelling. Three class labels 1,2 and 3
wine = pd.read_csv('wine_data.csv', names = ["Cultivator", "Alchol", "Malic_Acid", "Ash", "Alcalinity_of_Ash", "Magnesium", "Total_phenols", "Falvanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue", "OD280", "Proline"])

#takes first 5 rows
print(wine.head())

print(wine.describe().transpose())
print(wine.shape)
from sklearn.model_selection import train_test_split
X = wine.drop('Cultivator',axis=1)
y = wine['Cultivator']
X_train, X_test, y_train, y_test = train_test_split(X, y)

#data normalization
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
#fit the training data
scaler.fit(X_train)
StandardScaler(copy=True, with_mean=True, with_std=True)
# Now apply the transformations to the data:
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neural_network import MLPClassifier
#Multi layer perceptron created with 3 hidden layer and each hidden layer has
#13 neurons and 500 iterations
mlp = MLPClassifier(hidden_layer_sizes=(13,13,13),max_iter=500)
#view the model generated
print(mlp.fit(X_train,y_train))
predictions = mlp.predict(X_test)
from sklearn.metrics import classification_report,confusion_matrix
#confudion matrix gives result for each class 
#Diagonal elements shows the number of correct classifications
#off diagonal gives number of misclassified data

print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))
print(len(mlp.coefs_))
print(len(mlp.coefs_[0]))
print(len(mlp.intercepts_[0]))
