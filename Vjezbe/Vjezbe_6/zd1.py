import numpy as np
import matplotlib.pyplot as plt
import random as rn
from scipy import stats

N=0
x_tot=[]
b=np.linspace(0.1, 3.0, 100)
m=np.linspace(0, 100, 100)
l=np.linspace(1, 100, 100)


while N<10000:
    mean=0
    sigma2=0
    x_data=[]
    y_data=[]
    i=0
    while i<100:
        x_data.append(np.random.exponential(b[i]))
        mean+=b[i]
        sigma2+=b[i]*b[i]
        i+=1

    i=0
    while i<100:
        x_data.append(np.random.normal(m[i], 5))
        mean+=m[i]
        sigma2+=25
        i+=1

    i=0
    while i<100:
        x_data.append(np.random.poisson(l[i]))
        mean+=l[i]
        sigma2+=l[i]
        i+=1

    z=sum(x_data)
    x_tot.append(z)
    N+=1

sigma=np.sqrt(sigma2)
x = np.linspace(mean - 3*sigma, mean + 3*sigma, 100)
plt.hist(x_tot, bins=50, edgecolor='black', density=True) #normalizirat
plt.plot(x, stats.norm.pdf(x, mean, sigma))
plt.savefig("zd1.jpg")