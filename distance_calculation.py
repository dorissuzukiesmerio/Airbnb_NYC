print("Hello!")

import pandas 
from sklearn import linear_model #For prediction
from sklearn.model_selection import KFold #For splitting the data
from sklearn import metrics #To evaluate goodness of fit
import numpy
from matplotlib import pyplot #for plotting graphs


dataset = pandas.read_csv("AB_NYC_2019.csv")
print(dataset)

#Detecting missing data
print(dataset.isnull().sum()) 

# name                                 16
# host_name                            21
# last_review                       10052
# reviews_per_month                 10052

#replacing all NaN values in 'reviews_per_month' with 0
dataset.fillna({'reviews_per_month':0}, inplace=True)
#examing changes
dataset.reviews_per_month.isnull().sum()

dataset.dropna(inplace=True)	                 # Drop observations with missing data
print(dataset)

# dataset['Distance'] = dataset.apply(lambda row: ((((latitude-40.7209)**2)+((longitude-74.0007)**2))**(1/2), axis == 1)
dataset['Distance'] = (((dataset['latitude']-40.7209)**2)+((dataset['longitude']-74.0007)**2))**(1/2)

print("Distance")
print(dataset)