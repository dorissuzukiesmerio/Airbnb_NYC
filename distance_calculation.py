print("Hello!")

import pandas 
from sklearn import linear_model #For prediction
from sklearn.model_selection import KFold #For splitting the data
from sklearn import metrics #To evaluate goodness of fit

import numpy
from matplotlib import pyplot as plt #for plotting graphs


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


#It is also important to drop the observations with price = 0
dataset = dataset.drop(dataset[dataset['price'] == 0].index)


# dataset['Distance'] = dataset.apply(lambda row: ((((latitude-40.7209)**2)+((longitude-74.0007)**2))**(1/2), axis == 1)
dataset['Distance'] = (((dataset['latitude']-40.7209)**2)+((dataset['longitude']-74.0007)**2))**(1/2)

print("Distance")
print(dataset)


#shuffles dataset
dataset = dataset.sample(frac=1).reset_index(drop=True)

#Transforming the categorical/string variables into dummies/numerical values:
neighbourhood_group_dummies = pandas.get_dummies(dataset['neighbourhood_group'])
neighbourhood_dummies = pandas.get_dummies(dataset['neighbourhood'])
room_type_dummies = pandas.get_dummies(dataset['room_type'])


#Merge new created variables as an entire csv file 
#dataset = dataset.merge(neighbourhood_group_dummies, left_index = True, right_index = True)
#dataset = dataset.merge(neighbourhood_dummies, left_index = True, right_index = True)
#dataset = dataset.merge(room_type_dummies, left_index = True, right_index = True)
#dataset.to_csv("dataset_dummies.csv")

#Distance between points
# for i in (1,38820):
#   dataset['Distance_i'] = (((dataset['latitude_i']-distance['latitude'])**2)+((dataset['longitude_i']-distance['latitude'])**2))**(1/2)


#Analysis:
target = dataset['price'].values     # Call the column by name, 'price' 
print("Target")
print(target)

# data = dataset.iloc[:, ADD COLUMNS HERE ].values
# print("Data")
# print(data)

plt.scatter(dataset['latitude'],dataset['longitude'])
plt.savefig("scatter.png")
