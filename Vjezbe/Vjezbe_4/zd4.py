import matplotlib.pyplot as plt
import numpy as np
import uproot
import awkward as ak

file=uproot.open("/home/public/data/Lifetime/Lifetime.root:Tree")
A=file["t"].array()

def lnPDF(Tau):
    res=0
    i=0
    while i < len(A):
        res+=-np.log(Tau)-A[i]/Tau
        i+=1
    return res

x_data=np.linspace(1, 1.5, 1000)
y_data=[]
i=0
min=-2*lnPDF(x_data[i])
while i<len(x_data):
    temp=-2*lnPDF(x_data[i])
    y_data.append(temp)
    if temp<min:
        min=temp
        taumin=x_data[i]
    i+=1

i=0
cross=abs(-2*lnPDF(x_data[i])-(min+1))
while i<len(x_data):
    temp=abs(-2*lnPDF(x_data[i])-(min+1))
    if temp<cross:
        cross=temp
        tau_sigma=x_data[i]
    i+=1

sigma=abs(tau_sigma-taumin)

plt.plot(x_data, y_data)
plt.xlabel("Tau [s]")
plt.ylabel("-2ln(PDF)")
plt.savefig('lnPDF')

print("Tau=", taumin)
print("sigma=", sigma)