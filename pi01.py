from random import random
from math import sqrt
count = 0
n = 0
while(True):
    x = random()*2 - 1
    y = random()*2 - 1
    d = sqrt(x**2 + y**2)
    if d <= 1:
        count += 1
    n+=1
    print(n, 4*count/n)
    
    
    
    