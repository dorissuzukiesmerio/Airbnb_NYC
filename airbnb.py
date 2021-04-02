print("Hello!")

import pandas 
from sklearn import linear_model #For prediction
from sklearn.model_selection import KFold #For splitting the data
from sklearn import metrics #To evaluate goodness of fit
import numpy

dataset = pandas.read_csv("AB_NYC_2019.csv")
print(dataset)

#Detecting missing data
print(dataset.isnull().sum()) 
#not relevant missing data. Just remember:
# name                                 16
# host_name                            21
# last_review                       10052
# reviews_per_month                 10052
#This is the missing data - do not use these columns, in order to avoid problems. Also, they do not seem too important to predict price
#(If I wanted to be very precise, I could try to impute last_review and reviews_per_month)
#(alternatively, I could have dropped the observations with missing data)

dataset.dropna(inplace=True)	                 # Drop observations with missing data
print(dataset)


# print(dataset.groupby('neighbourhood_group').count())



dataset['Bronx'] = numpy.where(dataset['neighbourhood_group']=='Bronx',1,0)
dataset['Brooklyn'] = numpy.where(dataset['neighbourhood_group']=='Brooklyn',1,0)
dataset['Manhattan'] = numpy.where(dataset['neighbourhood_group']=='Manhattan',1,0)
dataset['Queens'] = numpy.where(dataset['neighbourhood_group']=='Queens',1,0)
dataset['Staten Island'] = numpy.where( dataset['neighbourhood_group']=='Staten Island',1,0)


target = dataset.iloc[:,9].values #Price is the 9th column
print(target)

#What I tried but got error: KeyError: 'neighborhood'
# neighborhood_dummies = pandas.get_dummies(dataset['neighborhood'], dummy_na=True)
# neighborhood_group_dummies = pandas.get_dummies(dataset['neighborhood_group'])
# room_type_dummies = pandas.get_dummies(dataset['room_type'])

# data = pandas.concat([dataset[['ability','age','female','education','exp']]region_dummies, occ_dummies], axis = 1).values
target = dataset.iloc[:,1].values


#Selecting a subset of the Data:
data = dataset.iloc[:,[4,8]].values
# data = dataset.iloc[:,[4,8]].values
# data = dataset.iloc[:,[4,8]].values
# data = dataset.iloc[:,[4,8]].values
# data = dataset.iloc[:,[4,8]].values

print(data)


machine = linear_model.LinearRegression() # target is continuous variable (price)
print(machine)
machine.fit(data, target)


dataset.sample(frac=1).reset_index(drop=True)
#We want to mix the data randomly
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
	machine = linear_model.LinearRegression()
	machine.fit(data_training, target_training)
	new_target = machine.predict(data_test)#instead of new_data
	#We run pretending we don't know the predicted. But it is target_ .
	print("R2 score:", metrics.r2_score(target_test, new_target))#we are measuring how well do the target_test 
	print("Accuracy score:", metrics.accuracy_score(target_test, new_target))#How much of the predicted value is equal to the real. 
	# Accuracy_score is percentage of predicted score
	print("Confusion matrix: /n", metrics.confusion_matrix(target_test, new_target))


