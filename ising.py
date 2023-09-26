import numpy as np
import random as rnd
import matplotlib.pyplot as plt

T = 2 #temp in units if j and kb
j_ising = 1 # j in hamiltonian 

l = 50 #lattice length
lattice = np.ones((l, l))  #2d lattice

#randomize the lattice
for i in range(l):
    for j in range(l):
        if rnd.random() < 0.5:
            lattice[i][j] = -1
            
    
plt.pcolormesh(lattice)    
plt.show()
print (lattice)


