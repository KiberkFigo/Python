import matplotlib.pyplot as plt
import numpy as np
import math
with open('./nhl.csv', 'r') as f:
    lines = f.readlines()
    #trick = list(map(str, f.read().split(',')))
    commands = [entry.strip().split(',') for entry in lines]

def Average(l): 
    avg = sum(l) / len(l) 
    return avg


print(commands[1][1])
print(commands[1])

print(commands[1][:7])


#with open("./Day6/day_06.in", 'r') as fin:
#    fish = list(map(int, fin.read().split(',')))

x = commands[1][4].split('|')
print(x[0])
print(x[1])


Prvni_tretina = commands[1][4].split('|')
Druha_tretina = commands[1][5].split('|')
Treti_tretina = commands[1][6].split('|')

print(Prvni_tretina)
print(Druha_tretina)
print(Treti_tretina)

Prodlouzeni = commands[1][7].split('|')
Najezdy = commands[1][8].split('|')

print(Prodlouzeni)
print(Najezdy) 

HomeFirstPeriod = []
HomeSecondPeriod= []
HomeThirdPeriod = []
HostFirstPeriod = []
HostSecondPeriod= []
HostThirdPeriod = []

delka = len(commands)

for i in range(delka):
    if i>0 :
        FirstPeriod  = commands[i][4].split('|')
        SecondPeriod = commands[i][5].split('|')
        ThirdPeriod  = commands[i][6].split('|')
        HomeFirstPeriod.append(int(FirstPeriod[0]))
        HostFirstPeriod.append(int(FirstPeriod[1]))
        HomeSecondPeriod.append(int(SecondPeriod[0]))
        HostSecondPeriod.append(int(SecondPeriod[1]))
        HomeThirdPeriod.append(int(ThirdPeriod[0]))
        HostThirdPeriod.append(int(ThirdPeriod[1]))

plt.hist(HomeFirstPeriod)
plt.show()
plt.close() 


average = Average(HostFirstPeriod) 
print("Average of my_list is", average)


def sumace(x,y):
    delka = len(x)
    TotalGoal = []
    for i in range(delka):
        TotalGoal.append(x[i] + y[i])
    return TotalGoal

FirstPer = sumace(HomeFirstPeriod,HostFirstPeriod)

plt.hist(FirstPer)
plt.show()
plt.close() 
plt.plot(FirstPer)
plt.show()
plt.close() 

print(sum(FirstPer)/len(FirstPer))










axis = plt.subplots(2, 3)
# For Sine Function
axis[0, 0].plot(HomeFirstPeriod)
axis[0, 0].set_title("Home First Per")
  
# For Cosine Function
axis[0, 1].plot(HomeSecondPeriod)
axis[0, 1].set_title("Home Sec Per")


axis[0, 2].plot(HomeThirdPeriod)
axis[0, 2].set_title("Home Sec Per")

axis[0, 0].plot(HostFirstPeriod)
axis[0, 0].set_title("Host First Per")
  
# For Cosine Function
axis[1, 0].plot(HostSecondPeriod)
axis[1, 0].set_title("Host Sec Per")


axis[2, 0].plot(HostThirdPeriod)
axis[2, 0].set_title("Host Sec Per")

# Combine all the operations and display
plt.show()
plt.show()