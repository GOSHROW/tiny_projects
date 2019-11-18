'''
By:                 Swapnil Ghosh
                    BTECH/10281/18
                    BIT Mesra
For:                Basics of Intelligent Computing
                    Assignment #8
Date of Creation:   18th November, 2019, evidenced by commit to GitHub
GitHub:             https://github.com/GOSHROW/tiny_projects/Genetic_Algorithm
'''

# Importing neccessary libraries for future uses 
import random
import secrets
from numpy.random import choice
import pandas
import matplotlib.pyplot as plt

#  Initializing Random Population

def Initialize(pop_size, no_of_chromosomes):
    
    population = []                                         #population to be initialized and returned

    for i in range(pop_size):

        individual = secrets.randbits(no_of_chromosomes)    #Generate pseudo-CRNG for each individual

        individual = str(bin(individual))[2:]               #Convert to binary string
        individual = individual.zfill(no_of_chromosomes)    #Makes sure that all strings are of equal length
        population.append(individual)
    
    return population
	
#  function to MAXIMIZE: (x**2 - 2*x) ie (x^2 - 2x)
#  any custom function may be taken by changing parameter fitness_fn of Parents()
#  returns fit Parents for a Population by Roulette-wheel

def Parents(population, fitness_fn = "x**2 - 2*x"):                        #change fitness_fn at call for custom fitness function
    
    fitness_val = []

    for i in range(len(population)):

        individual = int(population[i], 2)                                 #convert all strings to native integer for Roulette-Wheel
        fitness = eval(fitness_fn.replace('x', 'individual'))              #evaluates and assigns fitness value for individuals
        fitness_val.append(fitness)
    
    fitness_sum = sum(fitness_val)
    probability = [x/fitness_sum for x in fitness_val]                     #provides probability to have weighted draw
    
    draw = choice(population, size = 64 , replace = True, p = probability) #implements weighted choice of Parents
    random.shuffle(list(draw))                                             #so that each pair is randomly taken
    parents = draw
    
    return (parents, probability, fitness_val)                             #returns a relevant tuple
	
#  Finds Next Generation for given parents, by Single-Point CrossOver 
#  Mutation has not been done, since it was not specified in the assignement: it may be added accordingly

def NextGeneration(parents):
    
    next_gen = []

    for i in range(len(parents)//2):                         #Provides pair of parenst

        crossover_point = secrets.randbelow(10)              #pseudo-CRNG pont for the Single CrossOver

        p1, p2 = parents[2*i], parents[2*i + 1]              #Provides pair of parents
        child1 = p1[:crossover_point] + p2[crossover_point:] #Provides Child1 by CrossOver
        child2 = p2[:crossover_point] + p1[crossover_point:] #Provides Child2 by CrossOver

        next_gen.append(child1)
        next_gen.append(child2)
    
    return next_gen
	


#  Main function
#  The variables defined hereon maybe and could be customized as per need
#  The values given for each variable is only suggestive and is irrelevant to the algorithm of the program

epochs = 100
pop_size = 64
no_of_chromosomes  = 16
plot_avg_fit =[]

population = Initialize(pop_size, no_of_chromosomes)

for i in range(epochs):                             #ALL epochs are covered and the fitness and population of each epoch affects the next         

    (parents, probability, fitness_val) = Parents(population)
    
    print("\nEpochs: " + str(i))
    avg_fitness = sum(fitness_val)/len(fitness_val) #Average Fitness of Population at each Epoch
    plot_avg_fit.append(avg_fitness)                
    print("Fitness Average: "+ str(avg_fitness))
    
    if i in [0, epochs-1]:                          #For comparative Study of the first and the final population through dataframes
        print(pandas.DataFrame(list(zip(population, fitness_val, probability)), index = list(range(1, pop_size + 1)), columns = ['Population', 'Fitness Value', 'Probability']))

    next_gen = NextGeneration(parents)              
    population = next_gen                           #Each poulation except the initial is generated as child of the previous one
	
plt.plot(plot_avg_fit)                          #Plots the average Fitness of each Epoch
plt.ylabel("Average Fitness of the Population")
plt.xlabel("No. of Epochs")
plt.show()                                      #The General trend for the function taken seems to increase until it attains a Plateau
print("Max. Epoch shown at:{}".format(plot_avg_fit.index(max(plot_avg_fit))))