import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats

x=np.linspace(0, 20, 10000)
plt.plot(x, stats.chi2.cdf(x, df=1), label='k=1')
plt.plot(x, stats.chi2.cdf(x, df=2), label='k=2')
plt.plot(x, stats.chi2.cdf(x, df=3), label='k=3')
plt.plot(x, stats.chi2.cdf(x, df=4), label='k=4')
plt.plot(x, stats.chi2.cdf(x, df=5), label='k=5')
plt.legend()
plt.savefig("CDF.jpg")

cdf=0.954
y=stats.chi2.cdf(x, df=1)
i=0
z=1
while i<10000:
    if abs(y[i]-cdf)<z:
        z=abs(y[i]-cdf)
        k=i
    i+=1
print(x[k])