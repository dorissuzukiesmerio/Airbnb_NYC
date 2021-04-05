# Airbnb_NYC
Prediction of Airbnb prices in NYC

File : distance_calculation

Thursday April 1, 2021
9:44pm - 10:20pm (46 min) 
- Found info coordinates for downtown : 40.7209° N, 74.0007° W
- Calculation of distance
- Checking for errors
Created distance column !

Next steps: 
1. include that new column in analysis
2. google how to calculate the distance that takes into account the spherical shape of the earth (great circle distance)
3. Delete unnecessary files from this repository
______________________________________________________
Friday April 2, 2021
4:24pm - 4:56pm (32min) 

- Deleted unnecessary files from this repository
- Included additional commands to do analysis

Need to :
1. Calculate distance from each other - to see concentration and competition
2. Calculate great circle distance
_____
6:33pm- 7:14pm (41 min)
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

Or: build a matrix where the columnns 

2. Great circle distance ( Googling how to code 6:49-7:14pm)

from math import radians, degrees, sin, cos, asin, acos, sqrt
def great_circle(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    return 6371 * (
        acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))
    )
If miles, use 3958.756 
If km use 6371
Now... how to do a loop ?

Useful link: https://codereview.stackexchange.com/questions/217557/aggregate-pandas-columns-on-geospacial-distance 

- Did a scatter, and looked some previous codes to try to understand how to correctly write the syntax. 

_____________________________________________
Monday April 5, 2021

6:10pm - 6: 46pm (36 min) 

Goals: 
- try to finish analysis with the column I have
- then, try to correctly write the syntax of the idea for the distance loop.

n = 1
for i in (1,38821):
  n = n + 1
  dataset.Distance[i] = (((dataset.latitude[i]-dataset.latitude[n])**2)+((dataset.longitude[i]-dataset.latitude[n])**2))**(1/2)
  
I realized I was thinking 38820 should be the number, but I should actually use 38821

__ERRORS:
1. In the loop for distance between each point
2. In including Distance to Downtown in prediction
ValueError: Expected 2D array, got 1D array instead:
array=[147.84747 147.93526 147.89322 ... 147.91153 148.08002 147.93648].
Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.

______________________________________________________

TOTAL : 155 min ( 2h35min) 

Questions for Prof.Tom:

1. Sytax of 


n = 1
for i in (1,38821):
  n = n + 1
  dataset.Distance[i] = (((dataset.latitude[i]-dataset.latitude[n])**2)+((dataset.longitude[i]-dataset.latitude[n])**2))**(1/2)
  
2. Errors in prediction

3. Hint for writing loop for great circle distance

4. It looks like sometimes I am doing something wrong when I try to update the files on git hub 

This is what I have put:
git remote add origin https://github.com/dorissuzukiesmerio/Airbnb_NYC.git
git branch -M main
git push -u origin main![image](https://user-images.githubusercontent.com/78039852/113636280-408d2f80-9640-11eb-94e5-b1edb7668ce3.png)

And this is the message in yellow that I get:

 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/dorissuzukiesmerio/Airbnb_NYC.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
