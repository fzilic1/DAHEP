import scipy as sp
from scipy import stats
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt
import random as rn

N=10000
def PDF(x, mu, sigma):
    p=stats.norm.pdf(x, mu, sigma)
    return p

x_data=[]
y_data=[]
acc=0
count=0
while acc<N:
    x=10*rn.random()-5
    y=rn.random()
    if PDF(x, 0, 1)>y:
        x_data.append(x)
        y_data.append(PDF(x, 0, 1))
        acc+=1
    count+=1

print("Postotak prihvaćanja:", acc/count)
plt.hist(x_data, bins=30, edgecolor='black')
plt.savefig("rnd.jpg")