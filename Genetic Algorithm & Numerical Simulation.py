#important packages to install to help run code.
#import sys
#!{sys.executable} -m pip install --upgrade pip
#!{sys.executable} -m pip install PyHamcrest
#!{sys.executable} -m pip install mlrose   #provides functionality for implementing some of the most popular randomization and search algorithms.

# Create a program in python to complete this optimization process.
# import important libraries for problem
import numpy as np
import matplotlib.pyplot as plt
import mlrose as mse
import random


def genetic_alg():
    # Create array containing coordinates of city(x and y can be in the range of 0-100 inclusive) feel free to edit the coordinates to represent a scaled representation of earth or for fun
    city_coordinates = []  # initializing a list to store coordinates of all cities
    for i in range(15):
        city_coordinates.append((random.sample(range(101),
                                               2)))  # random class has accessor method sample which takes any non-repeated 2 values from 0-100 and appends as a tuple in city-coordinates list.
    print("Unordered city coordinates:", city_coordinates)

    # Initialize Objective function to accept nodes as parameters
    fit_coordinates = mse.TravellingSales(
        coords=city_coordinates)  # access the TSP class in mlrose package which manually defines fitness function to take point coordinates as parameter and calculates all possible total lenghts

    # Set-up the Optimization problem using TravelSalesPerson Optimization Class in the opt_probs library.
    vaccine_spread = mse.TSPOpt(length=15, fitness_fn=fit_coordinates,
                                maximize=False)  # creating an instance of the TSP Optimization problem with parameters length referring to number of cities, fitness function taking suitable coordinates and setting maximize to False because our general objective function is to minimize total distance.

    # Choose Randomized Optimization Algorithm
    arranged_cities, shortest_distance = mse.genetic_alg(vaccine_spread, mutation_prob=0.2, max_attempts=100,
                                                         random_state=2)  # we select the genetic algorithm class to process our fitness functions with mutation probability of 0.2.
    # Our max_attempts sets maximum number of attempts to find a better neighbor at each step. The use of a random seed is simply to allow for results to be as (close to) reproducible as possible.

    print()
    print('The best city arrangement is: ', arranged_cities,
          " ")  # Array containing arranged genes that optimizes the fitness function.

    print()
    print('The shortest distance between optimally arranged city is: ', shortest_distance,
          "units.")  # Value of fitness function at optimal state.

    # visualization graph
    arranged_coordinates = []  # list for coordinates in arranged order
    for i in arranged_cities:
        arranged_coordinates.append(
            city_coordinates[i])  # adds city coordinates to list in order of arrangement of postions in optimal pathway
    print()
    print("\nArranged coordinates of cities:", arranged_coordinates)

    plt.rcParams["figure.figsize"] = [10, 7]
    xcord, ycord = [x[0] for x in arranged_coordinates], [y[1] for y in
                                                          arranged_coordinates]  # separates tuples in arranged coordinates to x and y coordinates for graphing
    plt.plot(xcord, ycord, marker="o", label="Cities")
    j = 0
    for i in arranged_cities:
        plt.text(xcord[j], ycord[j], str(i))  # for labeling each city for easy identification and path follow up.
        j += 1
    plt.plot(xcord[0], ycord[0], marker="o", color="red", label="Start City")
    plt.plot(xcord[-1], ycord[-1], marker="o", color="green", label="End City")

    xends = [xcord[0], xcord[-1]]
    yends = [ycord[0], ycord[-1]]
    plt.plot(xends, yends)  # a line to show return to start point

    plt.grid()
    plt.legend()

    plt.show()


genetic_alg()

# NUMERICAL SIMULATION USING EULER'S METHOD TO MODEL MALARIA DYNAMICS IN FLORIDA

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def Euler_sim():
    t0 = 0 # start time represented in days
    t_end = 50 # end time represented in days

    h = .01 # step size
    steps = int((t_end - t0)/h + 1) # number of steps, the +1 means we are also considering counting the full t_end year as part.

    t = np.linspace(t0, t_end, steps) # storing t values
    S = np.zeros(steps) # for storing S values over time but all values initialized to zero at first
    I = np.zeros(steps) # for storing I values over time but all values initialized to zero at first
    R = np.zeros(steps) # for storing R values over time but all values initialized to zero at first
    V = np.zeros(steps) # for storing V values over time but all values initialized to zero at first

    b = 0.001 # infection rate parameter for malaria
    k = 0.9   # recovery rate paramenter for malaria
    y = 1/10  # mean time for immunity = 10 years: insects are known to evolve about every decade.
    i = 0.6  # vaccination rate

    def dSdt(t,S,I): # dS/dt function which represents the susceptible differential equation that takes S and I as variables and b as parameter
        return -b*S*I # we have -b to show decrease in our susceptible solution over the years. Also our susceptible population depend on amount of susceptible and infected individuals

    def dIdt(t,S,I): # dI/dt function which represents the infected differential equation that takes S and I as variables and b and k as parameter
        return I*(b*S - k) #Infected popluation depend on amount of susceptible and infected minus those removed from the population

    def dRdt(t,I): # dR/dt function which represents the removed differential equation that takes and I as variable and k as parameter
        return k*I # Removed population depend on amount of Infected population

    def dVdt(t,S): # dV/dt function which represents vaccinated differential equation that takes S as variable and i as parameter
        return i*S # vaccinated population depends on amount of susceptible population only. NB: once you're infected you are cured not vaccined in this context.

    # initial condition
    S[0] = 750 # number of susceptible people at start of simulation to 80 i.e at t0=0
    I[0] = 250 # number of infected people at start of simulation to 20 i.e at t0=0
    R[0] = 0  # number of recovered people at start of simulation due to death or vaccine so can no longer be infected to 0 i.e. at t0=0
    V[0] = 0  # number of vaccinated people before start of simulation set to 0.

    #Optional Super Challenge included: vaccination and resistant malaria
    #over time, recovered people lose immunity due to evolution of resistant malaria.
    #This allows people in recovered population to leak back to susceptible population.
    #Also we assume some fraction of susceptible were vaccinated and continued as we were deploying our drug over the 15 cities.
    #over time, vaccinated population is expected to increase decreasing susceptible population by change in vaccinated population over time.

    for n in range(steps-1): # for loop to start numerical simulation. steps-1 because range begins at index 0.
        S[n+1] = S[n] + h*dSdt(t[n],S[n], I[n]) + (h*y*R[n]) - (h*dVdt(t[n],S[n])) # susceptible population at any time will approximately be equal to susceptible population for previous year + change in susceptible population plus change in leaked recovered populaiton from previous year due to resistant/evolved malaria minus change in vaccinated population.
        I[n+1] = I[n] + h*dIdt(t[n],S[n],I[n]) # infected population at any time will be approx. equal to infected population from previous year and change in infected population
        R[n+1] = R[n] + h*dRdt(t[n],I[n]) - (h*y*R[n]) # recovered population at any time approx. equals recovered population from previous year and change in recovered population minus leaked recovered population from previous year due to resistant malaria.
        V[n+1] = V[n] + h*dVdt(t[n],S[n]) # vaccinated population at any time approx. equals vaccinated population from previous year and change in vaccination population

    #visualization of model

    #%matplotlib inline
    plt.rcParams.update({'font.size': 15})
    plt.rcParams["figure.figsize"] = [13,8] #for adjusting size of graph
    sns.regplot(x=t, y=S, fit_reg=False, color="blue") #plot actual dots, fit_reg is set to False because regression lines are not needed.
    sns.regplot(x=t, y=I, fit_reg=False, color="orange")
    sns.regplot(x=t, y=R, fit_reg=False, color="green")
    sns.regplot(x=t, y=V, fit_reg=False, color="red")
    plt.plot(t,S,linewidth=2,label='Susceptible(t)') #lineplots for different variables, with set thickness of lines.
    plt.plot(t,I,linewidth=2,label='Infected(t)')
    plt.plot(t,R,linewidth=2,label='Recovered(t)')
    plt.plot(t,V,linewidth=2,label='Vaccinated(t)')
    plt.xlabel('t (years)')
    plt.ylabel('S,  I,  R,  V (people)')
    plt.legend(loc='upper right') #sets the legend on the upper right on the graph
    plt.grid() #sets gridlines
    plt.show()

Euler_sim()