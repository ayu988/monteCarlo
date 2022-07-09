import random
import matplotlib.pyplot as plt
import pandas as pd
import datetime
current_time = datetime.datetime.now()
parent = "/media/ayush/StudyFiles/Elite research/monteCarlo/"
def uniqKrdo(arr):
    return list(dict.fromkeys(arr))
def discard(arr):
    temp = []
    for i in range(len(arr)):
        if (arr[i]>= 2.82) and ( arr[i]<= 3.45):
            temp.append(arr[i])
    return temp
master = []
for j in range(1000):
    pin = 0
    ptot = 0
    for k in range(1000):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**0.5 <= 1:
            pin += 1
        ptot += 1
        pi = 4*(pin/ptot)
        master.append(pi)
master = discard(master)
master.sort()
plt.plot(master)
plt.show()
df = pd.DataFrame(master)
df.to_csv('bkk1.csv')