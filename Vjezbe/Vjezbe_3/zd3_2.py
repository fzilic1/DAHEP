import scipy as sp
from scipy import stats
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

def CDF(y, mu, sigma):
    cdf=integrate.quad(lambda x: stats.norm.pdf(x, mu, sigma), -np.inf, y)
    return cdf[0]

x_data=np.arange(-5, 5, 0.1)
y_data=[]
i=0
while i<len(x_data):
    y_data.append(CDF(x_data[i], 0, 1))
    i+=1

plt.plot(x_data, y_data)
plt.title("CDF za Gaussian, mu=0, sig=1")
plt.savefig("cdf.jpg")