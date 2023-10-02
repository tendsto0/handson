import numpy as np
import random as rnd
import matplotlib.pyplot as plt

neqil = 2500
nitter = 5000                   #monte carlo steps
#T = 2                           #temp in units if j and kb
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
cvlist = []
Xlist = []
Temperature = []
for temp in range(150, 301):
    
    T = temp/100
    avg_e, avg_m = 0, 0
    avg_e_n, avg_m_n = 0, 0
    avg_e_2, avg_m_2 = 0, 0
    
    #evolving the sytem to equilibrium 
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
        if(time >= neqil):
            mag = abs(M)/l*l
            avg_m += mag
            avg_e += E/l*l
            avg_m_2 += M**2
            avg_e_2 += E**2
            avg_m_n += M
            avg_e_n += E
            
    avg_m = avg_m/(nitter - neqil)
    avg_e = avg_e/(nitter - neqil)
    avg_e_2 = avg_m_2/(nitter - neqil)
    avg_m_2 = avg_m_2/(nitter - neqil)
    avg_m_n = avg_m_n/(nitter - neqil)
    avg_e_2 = avg_e_2/(nitter - neqil)
    X = (avg_m_2 - avg_m_n**2)/T
    cv = (avg_e_2 - avg_e_n**2)/T**2
    Xlist.append(X)
    cvlist.append(cv)
    energy.append(avg_e)
    magnetization.append(avg_m)
    Temperature.append(T)
     
fig, ax = plt.subplots(nrows = 2, ncols = 2)   

ax[0, 0].scatter(Temperature, energy, c='red' )
ax[0, 1].scatter(Temperature, cvlist, c='red')
ax[1, 0].scatter(Temperature, magnetization, c='blue')
ax[1, 1].scatter(Temperature, Xlist, c='blue')

ax[0, 0].set_ylabel('Energy per spin <E/N>')
ax[0, 1].set_ylabel('$C_v$')
ax[1, 0].set_ylabel('magnetization <M/N>')
ax[1, 1].set_ylabel('$\chi$')

ax[0, 0].set_xlabel('Temperature')
ax[0, 1].set_xlabel('Temperature')
ax[1, 0].set_xlabel('Temperature')
ax[1, 1].set_xlabel('Temperature')


ax[0, 0].set_title('Energy per spin vs temp.')
ax[0, 1].set_title('$C_v$ vs temp.')
ax[1, 0].set_title('magnetization per spin vs temp.')
ax[1, 1].set_title('Susceptibity vs temp.')
 
plt.show()