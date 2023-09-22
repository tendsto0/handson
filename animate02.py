import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation 

x = []
y = []

fig, ax = plt.subplots()

ax.scatter(x,y)

def animate(i):
   
    x.append(i*0.1)
    y.append(np.sin(i*0.1))
    
    plt.cla()   
    plt.scatter(x,y)
              
anim = FuncAnimation(fig, animate, frames = 2000, interval = 10)      

plt.show()      