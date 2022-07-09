import random
import matplotlib.pyplot as plt
import pandas as pd
master = []
for i in range(1000):
    pin = 0
    ptot = 0
    for j in range(1000):
        x = random.random()
        y = random.random()
        z = random.random()
        if (x*x + y*y + z*z)**0.5 <= 1:
            pin += 1
        ptot += 1
    pi = 6*(float(pin/ptot))
    master.append(pi)
master.sort()
plt.hist(master,bins=50)
frame = pd.DataFrame(master)
name = input("Enter file name>>>>>")
frame.to_csv(name)
plt.show()   
