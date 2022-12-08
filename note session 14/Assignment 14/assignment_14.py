# -*- coding: utf-8 -*-
"""Assignment 14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XG5oTwiKbf5O44lpIY-TgWO65uNCSyeR

import the libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Housing.csv')
dataset.info()

dataset.head()

x = dataset.iloc[:,0:1]
# print(x)
y = dataset.iloc[:,1]
# print(y)

from sklearn.model_selection import train_test_split
xTrain , xTest , yTrain , yTest = train_test_split(x,y,test_size=1/9)

from sklearn.linear_model import LinearRegression
linReg = LinearRegression()
from sklearn.preprocessing import PolynomialFeatures
polyReg = PolynomialFeatures(degree = 4)
#transform بيطبق على الدالة بتعتي
xPoly = polyReg.fit_transform(xTrain)
#في الاخر هتبقى انحدار خطي عادي لانه كله في الاخر عبارة عن ارقام وليست ارقام اصلها اكس اس رقم
linReg2 = LinearRegression()
linReg2.fit(xPoly,yTrain)

plt.scatter(x,y,color = 'red')

plt.scatter(xTrain,yTrain,color = 'red')
plt.plot(x,linReg2.predict(polyReg.fit_transform(x)),color='blue')

plt.scatter(xTest,yTest,color = 'red')
plt.plot(x,linReg2.predict(polyReg.fit_transform(x)),color='blue')

x = dataset.iloc[:,0:1]
xLen = len(x)
xNew = []
yNew = []
for i in range(xLen):
  xLoc = dataset.iloc[i,0:1].values
  xNew.append(xLoc)
  sum = dataset['bedrooms'] + dataset['bathrooms'] + dataset['stories']+ dataset['parking']
  yLoc =  dataset['area'] / sum
  yNew.append(yLoc)

# print(xNew) 
# print(yLoc)
  
plt.scatter(yLoc,xNew,color = 'red')

