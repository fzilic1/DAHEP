import scipy as sp
from scipy import stats
from scipy import integrate
from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
import random as rn

def CDF(y):
    cdf=integrate.quad(lambda x: stats.norm.pdf(x, 0, 1), -np.inf, y)
    return cdf[0]

x_data=[]
i=0
while i<1000:
    u=rn.random()
    def uCDF(y):
        z=u-CDF(y)
        return abs(z)
    x=optimize.fmin(uCDF, 1)
    x_data.append(x[0])
    i+=1

plt.hist(x_data, bins=30, edgecolor='black')
plt.savefig("rnd2.jpg")