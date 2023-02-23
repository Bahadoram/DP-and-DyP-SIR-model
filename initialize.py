import numpy as np
import random

def initial_conf(N, initial_infected, d):
    if d==1:
        initial_lattice = np.zeros(N)
        indeces = random.sample([i for i in range(len(initial_lattice))], initial_infected)
        initial_lattice[indeces] = 1
        return(initial_lattice)
    elif d==2:
        initial_lattice = np.zeros((N, N))
        index_x = random.sample([i for i in range(len(initial_lattice[0]))], initial_infected)
        index_y = random.sample([i for i in range(len(initial_lattice[1]))], initial_infected)
        for pair in list(zip(index_x, index_y)):
            initial_lattice[pair]=1
        return(initial_lattice)