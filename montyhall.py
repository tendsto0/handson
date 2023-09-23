import random as rnd
import matplotlib.pyplot as plt
prize = ["car","goat","goat"]

win_prob_switch = []
win_prob_stay = []

door = [0,1,2]
stay_win = 0
switch_win = 0
for i in range(1,2000):
    
    
    rnd.shuffle(prize)
    k = rnd.choice(door)
    
    if prize[k] != "car":
        switch_win += 1
    else:
        stay_win += 1
        
    prob_stay = stay_win/i
    prob_switch = switch_win/i
    
    win_prob_stay.append(prob_stay)
    win_prob_switch.append(prob_switch)
    
plt.plot(win_prob_stay, label = 'prob of win by staying')
plt.plot(win_prob_switch, label = 'prob of win by switching')
plt.legend()
print("prob of win by switching", win_prob_switch[-1])        
print("prob of win by staying", win_prob_stay[-1]) 
plt.show()  
    




