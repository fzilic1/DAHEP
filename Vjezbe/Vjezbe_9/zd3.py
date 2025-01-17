import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
import uproot
import awkward as ak

file=uproot.open("/home/public/data/GaussData.root")
data=file["tree/x_observed"].array()

def logL(x, m, s):
    return -0.5*np.sum((x-m)/s)**2+np.log(2*np.pi*s**2)

i=0
LR=[]
s=np.std(data)
m=np.linspace(0, 20, 1000)
while i<1000:
    LR.append(-2*logL(data, 5, s)+2*logL(data, m[i], s))
    i+=1


#plt.hist(data, bins=50, edgecolor='black')
plt.plot(m, LR)
plt.xlabel('mean')
plt.ylabel('Likelihood Ratio')
plt.savefig("data.jpg")