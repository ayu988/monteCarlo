import random
import matplotlib.pyplot as plt
import numpy as np
pin,ptot=0,0
master = []
for j in range(200):
    for i in range(1000):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if (x * x + y * y) ** 0.5 <= 1:
            pin += 1
        ptot += 1
    pi = 4*(pin/ptot)
    master.append(pi)
# fig, axs = plt.subplots(1, 1,figsize =(10, 7),tight_layout = True)
 
# axs.hist(master, bins=500)
master.sort()
x_data,y_data = np.arange(-10,10,0.1),master
plt.plot(x_data,y_data)

print(min(master),"\n",max(master))
plt.show()
