print("Hello!")

import pandas 
from sklearn import linear_model #For prediction
from sklearn.model_selection import KFold #For splitting the data
from sklearn import metrics #To evaluate goodness of fit



from sklearn.ensemble import RandomForestClassifier #under different roof .ensemble, 
#ensemble : component that can disagree with each other - decide by folder 
from sklearn.preprocessing import LabelEncoder

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

# dataset['Distance'] = (((dataset['latitude']-40.7209)**2)+((dataset['longitude']-74.0007)**2))**(1/2)
downtown_lat = 40.7209
downtown_lon = 74.0007
dataset['Distance_downtown'] = numpy.sqrt((dataset['latitude']-40.7209)**2)+((dataset['longitude']-74.0007)**2)

print("Distance to downtown")
# print(dataset)
print(dataset['Distance_downtown'])

#Find minimun distance to downtown:
print("Minimun distance to downtown")
min_dist_downt = min(dataset['Distance_downtown'])
print(min_dist_downt)
#Find what position it is:
print("Index of min distance to downtown")
# print(dataset['Distance_downtown'].index(str(21819.346823416097)))
# linear_min_dist_downt = min_dist_downt*(10000/90)
# print(linear_min_dist_downt) # There is something weird ! Think through

print("Dataset matrix")
for i in range(38821):
	reference_lat = dataset['latitude'].iloc[i]
	reference_long = dataset['longitude'].iloc[i]
	dataset['dist' + str(i)] = numpy.sqrt((dataset['latitude'] - reference_lat)**2 + (dataset['longitude'] - reference_long)**2)
	print(dataset["dist"+ str(i)])
# print(dataset["dist"])
#With this, create a measure of competition:


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


#Analysis:
target = dataset['price'].values     # Call the column by name, 'price' 
print("Target")
print(target)

# le = LabeEncoder()

# data = dataset.iloc[:, ADD COLUMNS HERE ].values
data = [dataset['Distance'].values] # simple 
# print("Data")
# print(data)

# plt.scatter(dataset['latitude'],dataset['longitude'])
# plt.savefig("scatter.png")

kfold_object = KFold(n_splits = 4)
kfold_object.get_n_splits(data)

print(kfold_object) 

i = 0 # We could call i= test_case
for training_index, test_index in kfold_object.split(data):
	print(i)
	i = i + 1
	print("training:", training_index)
	print("test:",test_index)
	data_training = data[training_index]
	data_test = data[test_index]
	target_training = target[training_index]
	target_test = target[test_index]
	machine = RandomForestClassifier(criterion="gini", max_depth=5, n_estimators=11) #copy, paste and adapt from kfold #try different max_depth = 10 , 30, 3
	machine.fit(data_training, target_training)
	new_target = machine.predict(data_test)
	print("Accuracy score:", metrics.accuracy_score(target_test, new_target))# use acc instead of r2
	print("Confusion matrix: \n ", metrics.confusion_matrix(target_test, new_target))# use acc instead of r2	


# Or :

# machine = linear_model.LinearRegression()
# print(machine)
# machine.fit(data, target)


# new_data = [130, 157, 123, 140] # adding 4 new rows of data
# new_target = machine.predict(new_data)
# print(new_target)

# print("R2 score:", metrics.r2_score(new_data, new_target))#we are measuring how well do the target_test 

#

