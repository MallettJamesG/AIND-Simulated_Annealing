import numpy as np  # contains helpful math functions like numpy.exp()
import numpy.random as random  # see numpy.random module


test_cities = [('DC', (11, 1)), ('SF', (0, 0)), ('PHX', (2, -3)), ('LA', (0, -4))]

NumCities=len(test_cities)

#
# temp=test_cities[0]
# test_cities[0]=test_cities[1]
# test_cities[1]=temp


AllNeigbs=[]
print("About to enter")
for i in range(NumCities):

    if i+1 not in range(NumCities):
        newlist=test_cities
        newlist[0],newlist[i]=newlist[i],newlist[0]
        AllNeigbs.append(newlist)
        break
    else:
        newlist=test_cities.
        newlist[i],newlist[i+1]=newlist[i+1],newlist[i]
        AllNeigbs.append(newlist)

# print(AllNeigbs)
