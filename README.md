# Airbnb_NYC
Prediction of Airbnb prices in NYC

File : distance_calculation

9:44pm - 10:20pm (46 min) Thursday April 1, 2021
- Found info coordinates for downtown : 40.7209° N, 74.0007° W
- Calculation of distance
- Checking for errors
Created distance column !

Next steps: 
1. include that new column in analysis
2. google how to calculate the distance that takes into account the spherical shape of the earth (great circle distance)
3. Delete unnecessary files from this repository

4:24pm - 4:56pm (32min) Friday April 2, 2021

- Deleted unnecessary files from this repository
- Included additional commands to do analysis

Need to :
1. Calculate distance from each other - to see concentration and competition
2. Calculate great circle distance

6:33pm- 
1. Calculate distance from each other - to see concentration and competition

i) brainstorming: what would be the idea? (6:33pm to 6:49pm - 16 min)
Having 38820 observations (38821rows -1 for heading), I would need to create 38819 additional columns. Distance to observation 1, 2, ..... 38820
It would be a matrix where the main diagonal is 0. 

This piece of information would allow me to later implement other commands to gather, for each column :
the max and min distance, the average, the number of obs within a certain distance.

Adapt same formula:
dataset['Distance'] = (((dataset['latitude']-40.7209)**2)+((dataset['longitude']-74.0007)**2))**(1/2)

But, now:
for i in (1,38820):
  dataset['Distance_i'] = (((dataset['latitude_i']-distance['latitude'])**2)+((dataset['longitude_i']-distance['latitude'])**2))**(1/2)

Check syntax
