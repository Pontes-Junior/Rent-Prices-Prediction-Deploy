# Rent-Prices-Prediction-Deploy

## Business Problem

We want to predict the values of rent prices for houses in the city of São Paulo based on  basic features of the place(area,furniture,hoa,etc),solving such a problem would be very useful to identify houses that offer particularly nice characteristics for a good price.

## The Goal

One way to solve the problem above is to train a machine learning algorithm and deploy it as a webapp.In order to do that we use the data available at https://www.kaggle.com/rubenssjr/brasilian-houses-to-rent .We have done basic EDA,cleaning of outliers and comparation of models in a  Jupyter notebook that can be accessed in https://github.com/Pontes-Junior/Rent_Prices_Prediction .We use the Flask library to develop a webapp that deploys the model.

## A Machine Learning Approach

The problem of predicting the value of a continuous feature(House Rent Price) is know in the Data Science\Statistics  literature as a Regression Problem.There are a lot of models that we could compare and just pick the one with best performance.Instead we have limited ourselves to compare the performance of two efficient and interpretable models: 

- Linear Regression and Random Forests.During our investigation the Random Forests algothim showed better performance.

- Then to further improve the model we performed parameter tuning,we remark that the tuning was done in a adhoc manner in the same spirit of this lecture https://www.youtube.com/watch?v=0kns1gXLYg4&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN&index=7 .This already improved our model reasonably but is important to note that better   parameters may be found using Randomized Search techniques.

- Lastly we warn the reader that we are aware that in problems with structured data,such as that we are looking at,gradient algorithms such as LightGBM and XGBOOST perform really well.We doesn`t pursue that line of work because we wanted a focus on fast deploying a reasonably good and simple model. 
