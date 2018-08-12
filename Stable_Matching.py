#stable matching problem

import random
import numpy as np

n = int(input("Enter the number of pairs: "))

men = ['m'+str(i) for i in range(0, n)]
women = ['w'+str(i) for i in range(0, n)]

men_prefer = {}
women_prefer = {}
men_status = {}
women_status = {}

for i in range(0, n):
    tempm = list(men)
    random.shuffle(tempm)
    women_prefer[women[i]] = tempm
    tempw = list(women)
    random.shuffle(tempw)
    men_prefer[men[i]] = tempw
    men_status[men[i]] = None
    women_status[women[i]] = None

k = 0
while None in men_status.values():
    k += 1
    for i in range(0, n):
        if men_status[men[i]] == None:
            j = 0
            while men_status[men[i]] == None:
                temp = women_status[men_prefer[men[i]][j]]
                if temp == None:
                    men_status[men[i]] = men_prefer[men[i]][j]
                    women_status[men_prefer[men[i]][j]] = men[i]
                elif women_prefer[men_prefer[men[i]][j]].index(men[i]) < women_prefer[men_prefer[men[i]][j]].index(temp):
                    men_status[men[i]] = men_prefer[men[i]][j]
                    men_status[temp] = None
                    women_status[men_prefer[men[i]][j]] = men[i]
                j += 1

m = []
w = []
print("ith preference that a man got paired with")
for i in range(0, n):
    temp = men_prefer[men[i]].index(men_status[men[i]])
    m.append(temp)
print(m)
m = np.asarray(m)
print("Mean: ", np.mean(m))

print("ith preference that a woman got paired with")
for i in range(0, n):
    temp = women_prefer[women[i]].index(women_status[women[i]])
    w.append(temp)
print(w)
w = np.asarray(w)
print("Mean: ", np.mean(w))
print(k)