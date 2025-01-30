import numpy as np
import matplotlib.pyplot as plt
import random as rn
from scipy import stats
import uproot
import awkward as ak
from scipy.special import erfcinv

#CL=1-pH1/pH0   

H0_data=[
    np.mean(np.random.normal(loc=168.0, scale=7.0, size=100))
    for _ in range(1000000)]
H0_data = np.array(H0_data)

H1_data=[
    np.mean(np.random.normal(loc=165.5, scale=7.1, size=100))
    for _ in range(1000000)]
H1_data = np.array(H1_data)

H2_data=[
    np.mean(np.random.normal(loc=166.1, scale=6.5, size=100))
    for _ in range(1000000)]
H2_data = np.array(H2_data)

H3_data=[
    np.mean(np.random.normal(loc=170.3, scale=7.5, size=100))
    for _ in range(1000000)]
H3_data = np.array(H3_data)

file=uproot.open("/home/public/data/Height/Height.root")
heights=file["Tree/height"].array()
m=ak.sum(heights)/len(heights)

count=0
for k in H0_data:
    if k>m:
        count+=1

p0=count/len(H0_data)

count=0
for k in H1_data:
    if k>m:
        count+=1

p1=count/len(H1_data)
CL1=1-p1/p0

count=0
for k in H2_data:
    if k>m:
        count+=1

p2=count/len(H2_data)
CL2=1-p2/p0

count=0
for k in H3_data:
    if k<m:
        count+=1

p3=count/len(H3_data)
CL3=1-p3/(1-p0)

plt.axvline(x=m, color='red', label='mjerenja')
plt.hist(H0_data, bins=50, edgecolor='black', label='Španjolska', density='True')
plt.hist(H1_data, bins=50, edgecolor='black', label='Francuska', density='True')
plt.hist(H2_data, bins=50, edgecolor='black', label='Italija', density='True')
plt.hist(H3_data, bins=50, edgecolor='black', label='Nizozemska', density='True')
plt.legend(loc=1)
plt.xlabel('visina [cm]')
plt.savefig("zd2.jpg")
print(CL1)
print(CL2)
print(CL3)