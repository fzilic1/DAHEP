import numpy as np
import matplotlib.pyplot as plt
import random as rn
from scipy import stats
import uproot
import awkward as ak
from scipy.special import erfcinv

'''H0_data=[]
j=0
while j<1000000:
    i=0
    x=0
    while i<100:
        x+=np.random.normal(165.5, 7.1)
        i+=1
    x=x/100
    H0_data.append(x)
    j+=1'''

H0_data=[
    np.mean(np.random.normal(loc=165.5, scale=7.1, size=100))
    for _ in range(1000000)]
H0_data = np.array(H0_data)

file=uproot.open("/home/public/data/Height/Height.root")
heights=file["Tree/height"].array()
m=ak.sum(heights)/len(heights)

count=0
for k in H0_data:
    if k>m:
        count+=1

p=count/len(H0_data)
z_score = np.sqrt(2) * erfcinv(2 * p)
print(p)
print(z_score)

plt.axvline(x=m, color='red', label='mjerenja')
plt.hist(H0_data, bins=50, edgecolor='black', label='Francuska', density='True')
plt.legend(loc=1)
plt.xlabel('visina [cm]')
plt.savefig("zd1.jpg")