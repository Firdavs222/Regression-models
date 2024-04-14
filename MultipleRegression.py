
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

#coefficient which shows that if weight increases by 1 kg then how much CO2 increases;
#coefficient which shows that if the volume of motor increases by 1 kg then how much CO2 increases;
#print(regression.coef_)

#creating regression model
def MultiRegression(regression, x):
    X1 = regression.coef_[0]
    X2 = regression.coef_[1]
    mregress = X1*X["Weight"] + X2*X["Volume"] + regression.intercept_
    return mregress
y_predict = MultiRegression(regression, X)

#evaluating R2 score;
#print(regression.score(X,y_true))


