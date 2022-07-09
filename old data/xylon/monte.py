# imp-----area under curve of the 3.14 vlaues for all values, all geometries, discarded and eliminte non-discarded and restriction on cordinates
# shape dependent table with above cols. 
# verify the 4k and 2k logic--result
# improve time-Management
# check for unique random points.
# exo-planet in monte carlo.
# retain discard function and check for all geometries.
# recall fourier too.
import random
import numpy as np
import pandas as pd
def removeDuplicate(arr):
    return list(dict.fromkeys(arr))
def discardKrdo(arr):
    temp = []
    for i in range(len(arr)):
        if (arr[i]>= 3.12) and (arr[i]<= 3.15):
            temp.append(arr[i])
    return temp
master = []
main = {}
print("Hello there, This is the program to crash your system\nRun at your risk")
for i in range(1000):
    pin = 0
    ptot = 0
    for j in range(1000):
        x = random.random()
        y = random.random()
        # z = random.random() #---limit

        if (x*x+y*y)**0.5 <= 1 :
            pin += 1
        ptot += 1
        pi = 4*(pin/ptot)
        master.append(pi)
    
master.sort()
# master = discardKrdo(master)
print(len(master))
frame = pd.DataFrame({'pi-val': master})
freq=pd.crosstab(index=frame['pi-val'],columns='count')
print(freq)
name = str(input("Enter file name: "))
freq.to_csv(name)