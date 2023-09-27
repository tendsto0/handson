import numpy as np
import random as rnd
import matplotlib.pyplot as plt


nitter = 10000                  #monte carlo steps
T = 2                           #temp in units if j and kb
j_ising = 1                     #j in hamiltonian of ising model
E , M = 0, 0
l = 20                          #lattice length
spin = np.ones((l, l))          #2d lattice

#randomize the lattice

for i in range(l):
    for j in range(l):
        if rnd.uniform(0,1) < 0.5:
            spin[i][j] = -1
            
#claculating initial energy and magnetizaton of lattice
for i in range(l):
        for j in range(l):
            
            a, b, c, d = i + 1, i - 1, j + 1, j - 1                     #identifying neighbours
            if (i == l - 1): a = 0                                      #-----------------------
            if (i == 0): b = l - 1                                      #periodic boundry condition
            if (j == l - 1): c = 0
            if (j == 0): d = l - 1                                      #-----------------------
            
            
            E = E - j_ising*(spin[i][j] * (spin[a][j] + spin[b][j] + spin[i][c] + spin[i][d]))
            M = M + spin[i][j]


E = E/2                                                 #energy (divided by two because counted spin pairs twice)
mag = M/(l*l)                                           #magnetization per spin

print(f"initial    energy = {E}    magnetization = {mag}    M = {M}")

#evolving the sytem to equilibrium   
magnetization = []
energy = []
for  time in range(nitter):
    for itter1 in range(l):
         for itter2 in range(l):
            i = int(rnd.uniform(0,1)*l) 
            j = int(rnd.uniform(0,1)*l)
            
            a, b, c, d = i + 1, i - 1, j + 1, j - 1                     #identifying neighbours
            if (i == l - 1): a = 0                                      #-----------------------
            if (i == 0): b = l - 1                                      #periodic boundry condition
            if (j == l - 1): c = 0
            if (j == 0): d = l - 1                                      #-----------------------
            
            #energy before flip
            Ei = (-j_ising)*(spin[i][j] * (spin[a][j] + spin[b][j] + spin[i][c] + spin[i][d]))
            
            spin[i][j] = -spin[i][j]                                    #trial flip
            
            #energy after flip
            Ef = (-j_ising)*(spin[i][j] * (spin[a][j] + spin[b][j] + spin[i][c] + spin[i][d]))

            #Metropolis Algorithm
            if(Ef - Ei <= 0):
                E += (Ef - Ei)
                M += 2*spin[i][j]
            else:
                h = rnd.uniform(0,1)
                if(h < np.exp(-(Ef - Ei)/T)):
                    E += (Ef - Ei)
                    M += 2*spin[i][j]
                else:
                    spin[i][j] = -spin[i][j]
    
    
            magnetization.append(M/(400)) 
            #energy.append(E) 
    
plt.plot(magnetization, label= "mag")   
#print(magnetization)
#plt.legend()
plt.show()
                
                
            
            
            
       
    







