# Importing essential libraries
import numpy as np
import pandas as pd
import pickle

# Loading the dataset
dt = pd.read_csv('houses_to_rent_v2.csv')

#Data after cleaning
scaled_data=dt.loc[(dt["city"]=='São Paulo') & (dt["hoa (R$)"]<8000) & (dt["rooms"]<=4) & (dt["rent amount (R$)"]<22000) & (dt["area"] < 1000)]

#Selecting Features and Target
features=['area', 'rooms', 'bathroom', 'hoa (R$)']
X = scaled_data[features]
y = scaled_data['rent amount (R$)']


# Model Building
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# Creating Random Forest Model
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=200,max_depth=10,random_state=42)
model.fit(X_train, y_train)

# Saving model to disk
pickle.dump(model, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[60, 2, 1,800]])) 