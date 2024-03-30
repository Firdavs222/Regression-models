# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 21:32:21 2024

@author: user
"""

import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

dataframe = pd.read_csv("C://Users//user//Downloads//data.csv")
#print(dataframe)

X = dataframe[["Weight","Volume"]]
y_true = dataframe["CO2"]

regression = linear_model.LinearRegression()
regression.fit(X, y_true)

#predicting future values;
predicted_co2 = regression.predict([[1100,980]])
print(predicted_co2)

#koeffitsiyent - og'irlik 1 kg oshsa qancha CO2 ko'payishi;
#koefffitsiyent - hajm 1000 cm3 oshsa qancha CO2 ko'payishi;
#print(regression.coef_)

#regression model tuzamiz
def MultiRegression(regression, x):
    X1 = regression.coef_[0]
    X2 = regression.coef_[1]
    mregress = X1*X["Weight"] + X2*X["Volume"] + regression.intercept_
    return mregress
y_predict = MultiRegression(regression, X)

#determinatsiya koeffitsiyentini hisoblash;
#print(regression.score(X,y_true))


