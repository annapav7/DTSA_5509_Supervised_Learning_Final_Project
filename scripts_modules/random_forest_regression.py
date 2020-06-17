# -*- coding: utf-8 -*-
"""Random Forest Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zakvRqBbUgcypEy2LMsg6D0Ix3Mb24w1

#Donwload a ImageCollection

## 1._ Install libraries
"""

!pip install earthengine-api

"""## 2._ Establish connection"""

!earthengine authenticate

"""**`Complete End to End Python code for Random Forest Regression:`**"""

# Import necessary Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import rasterio as rio
#from rasterio.plot import show

# Import the data ( CSV formats)
#data = pd.read_csv('name_of_file.csv')
#data.head()

# Store the Data in form of dependent and independent variables separatly
X = data.ilog[:, 0:1].values
y = data.ilog[:, 1].values

# Import the Random Forest Regressor
from sklearn.ensemble import RandomForestRegressor

# Craete a Random Forest Regressor object from Random Forest Regressor Class
RFReg = RandomForestRegressor(n_estimators = 100, random_state = 0)

# Fit the random forest regressor with Training Data represented by X_train and y_train
RFReg.fit(X_train, y_train)

#Predicted Height from test dataset w.r.t Random Forest Regression
y_predict_rfr = RFReg.predict((X_test))

#Model Evaluation using R-Square for Random Forest Regression
from sklearn import metrics
r_square = metrics.r2_score(y_test, y_predict_rfr)
print('R-Square Error associated with Random Forest Regression is:', r_square)

''' Visualise the Random Forest Regression by creating range of values from min value of X_train to max value of X_train  
having a difference of 0.01 between two consecutive values'''
X_val = np.arange(min(X_train), max(X_train), 0.01) 
  
#Reshape the data into a len(X_val)*1 array in order to make a column out of the X_val values 
X_val = X_val.reshape((len(X_val), 1))  
  
#Define a scatter plot for training data 
plt.scatter(X_train, y_train, color = 'blue') 
  
#Plot the predicted data 
plt.plot(X_val, RFReg.predict(X_val), color = 'red')  
  
#Define the title 
plt.title('NO2 prediction using Random Forest Regression')  
  
#Define X axis label 
plt.xlabel('NDVI') 
  
#Define Y axis label 
plt.ylabel('Level of NO2') 

#Set the size of the plot for better clarity
plt.figure(figsize=(1,1))
  
#Draw the plot 
plt.show()

# Predicting Height based on Age using Random Forest Regression 
no2_pred = RFReg.predict([[41]])
print("Predicted NO2t: % d"% no2_pred)

"""**Model Evaluation**"""

#Model Evaluation using Mean Square Error (MSE)
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_predict))

#Model Evaluation using Root Mean Square Error (RMSE)
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_predict)))

#Model Evaluation using Mean Absolute Error (MAE)
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_predict))

#Model Evaluation using R-Square
from sklearn import metrics
r_square = metrics.r2_score(y_test, y_predict)
print('R-Square Error:', r_square)

#For Illustration Purpose Only. 
#Considering Multiple Linear Equation with two Variables : grade = a0 + a1*time_to_study + a2*class_participation
#Model Evaluation using Adjusted R-Square. 
# Here n = no. of observations and p = no. of independent variables

n = 50
p = 2
Adj_r_square = 1-(1-r_square)*(n-1)/(n-p-1)
print('Adjusted R-Square Error:', Adj_r_square)