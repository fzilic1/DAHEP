import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats

"""def lratio(x, m0, s0, m1, s1):
    L0=0
    L1=0
    for k in x:
        L0+=np.log(stats.norm.pdf(k, m0, s0))
        L1+=np.log(stats.norm.pdf(k, m1, s1))
    LR=-2*(L0-L1)
    return LR

i=0
LR=[]
while i<10000:
    data=np.random.normal(5, 2, 1000)
    m=np.mean(data)
    s=np.std(data)
    LR.append(lratio(data, 5, s, m, s))
    i+=1""" #sporo

def logL(x, m, s):
    return -0.5*np.sum((x-m)/s)**2+np.log(2*np.pi*s**2)

i=0
LR=[]
while i<10000:
    data=np.random.normal(5, 2, 1000)
    m=np.mean(data)
    s=np.std(data)
    LR.append(-2*logL(data, 5, s)+2*logL(data, m, s))
    i+=1

plt.hist(LR, bins=100, edgecolor='black', density=True)
x=np.linspace(0, 10000, 1000)
plt.plot(x, stats.chi2.pdf(x, df=1, scale=10000))
plt.savefig("wilktest.jpg")