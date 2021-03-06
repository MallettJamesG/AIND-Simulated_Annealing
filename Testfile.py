import json
import copy


import numpy as np  # contains helpful math functions like numpy.exp()
import numpy.random as random  # see numpy.random module
# import random  # alternative to numpy.random module

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#matplotlib inline


map = mpimg.imread("map.png")  # US States & Capitals map

# List of 30 US state capitals and corresponding coordinates on the map
with open('capitals.json', 'r') as capitals_file:
    capitals = json.load(capitals_file)
capitals_list = list(capitals.items())

def show_path(path, starting_city, w=12, h=8):
    """Plot a TSP path overlaid on a map of the US States & their capitals."""
    x, y = list(zip(*path))
    _, (x0, y0) = starting_city
    plt.imshow(map)
    plt.plot(x0, y0, 'y*', markersize=15)  # y* = yellow star for starting point
    plt.plot(x + x[:1], y + y[:1])  # include the starting point at the end of path
    plt.axis("off")
    fig = plt.gcf()
    fig.set_size_inches([w, h])

def simulated_annealing(problem, schedule):
    """The simulated annealing algorithm, a version of stochastic hill climbing
    where some downhill moves are allowed. Downhill moves are accepted readily
    early in the annealing schedule and then less often as time goes on. The
    schedule input determines the value of the temperature T as a function of
    time. [Norvig, AIMA Chapter 3]

    Parameters
    ----------
    problem : Problem
        An optimization problem, already initialized to a random starting state.
        The Problem class interface must implement a callable method
        "successors()" which returns states in the neighborhood of the current
        state, and a callable function "get_value()" which returns a fitness
        score for the state. (See the `TravelingSalesmanProblem` class below
        for details.)

    Returns
    -------
    Problem
        An approximate solution state of the optimization problem

    Notes
    -----
        (1) DO NOT include the MAKE-NODE line from the AIMA pseudocode

        (2) Modify the termination condition to return when the temperature
        falls below some reasonable minimum value (e.g., 1e-10) rather than
        testing for exact equality to zero
    """
    t=1

    while True:
        T=schedule(t)
        print("T",T,"t",t)
        if T<=1e-10:
            # Return the current state

            return 0

        else:
            # print("Problem is ",problem)
            next=random.choice(problem)
            delt_E=next.get_value()-current.get_value()
            if delt_E > 0:
                current=next
            else:
                # Only enters here if delta_E is less than zero, so e^~~ will always be <1
                current=next if random.rand()<np.exp(delta_E/t)

        if t==10:
            break
        t+=1


alpha = 0.95
temperature=1e4

def schedule(time):
    if time==0:
        return temperature
    else:
        return temperature*(alpha**time)

problem=["a","b","c","d","e"]
simulated_annealing(problem, schedule)

# # Failure implies that the initial path of the test case has been changed
# assert(tsp.path == [('DC', (11, 1)), ('SF', (0, 0)), ('PHX', (2, -3)), ('LA', (0, -4))])
# result = simulated_annealing(tsp, schedule)
# print("Initial score: {}\nStarting Path: {!s}".format(tsp.get_value(), tsp.path))
# print("Final score: {}\nFinal Path: {!s}".format(result.get_value(), result.path))
# assert(tsp.path != result.path)
# assert(result.get_value() > tsp.get_value())
