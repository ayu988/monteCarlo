from statistics import mean
import numpy as np
from scipy import rand
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm
import random
import pandas as pd

simul = [100,1000,10000,100000,1000000]
means = []
pin, ptot = 0,0

for i in range(len(simul)):
    sam = []
    for i in range(simul[i]):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        z = random.uniform(-1,1)
        if (x**2 + y**2+ z**2) <= 1 :
            pin+=1
        ptot+=1
        pi = 6*(pin/ptot)
        sam.append(pi)
    means.append(mean(sam))
perErr = [((k-np.pi)/np.pi)*100 for k in means] 
dat = {"mean" : means, "percen-error": perErr}   
df = pd.DataFrame(dat,index=simul)
print(df)
# print(len(sam))
# got = random.sample(sam,100)
# len(got)
# plt.hist(sam,density=True)
# dist = norm(np.mean(sam),np.std(sam))
# value = np.arange(2,4,0.0002)
# prob = [dist.pdf(k) for k in value]
# plt.plot(value,prob)
# plt.show()