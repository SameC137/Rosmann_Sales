import pickle
import sklearn

import sys, os

from scripts.CustomMaxImputer import CustomMaxImputer
import pandas as pd
from sklearn.metrics import mean_squared_error

try:
    file = open("./models/model2.pkl",'rb')
    model = pickle.load(file)
except:
    print("Error Loading Model")

try:
    data=pd.read_csv("./data/val.csv")
except:
    print("Csv File Could not be read")


print(data.columns)

y=data["Sales"]
x=data.drop(["Sales","Customers","Date","Store","Unnamed: 0"], axis=1,inplace=False)
prediction = model.predict(x)
error=mean_squared_error(y,prediction)

with open("metrics.txt", 'w') as outfile:
        outfile.write("MeanSquaredError: " + str(error) + "\n")
