import random
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
master = []
for i in range(1000):
    pin = 0
    ptot = 0
    for j in range(1000):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**0.5 <= 1:
            pin += 1
        ptot += 1
    pi = 4*(float(pin/ptot))
    master.append(pi)
master.sort()
frame = pd.DataFrame(master,columns=["x-axis"])
print(frame)
sns.displot(data=frame,x="x-axis",kind="kde")
plt.show()
# print(frame)
# name = input("Enter file name>>>>>")
# frame.to_csv(name)
# plt.show()   
