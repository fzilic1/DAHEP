import matplotlib.pyplot as plt
import numpy as np

F=[1, 2, 3, 4, 5]
a=[9.8, 21.2, 34.5, 39.9, 48.5]
err_a=[1.0, 1.9, 3.1, 3.9, 5.1]

def chi2(theta):
    i=0
    c=0
    while i<len(F):
        c+=pow((a[i]-theta*F[i]), 2)/pow(err_a[i], 2)
        i+=1
    return c

x=np.arange(6, 14.5, 0.1)
y=chi2(x)
min=y[0]
i=0
while i<len(x):
    if y[i]<min:
        min=y[i]
        theta=x[i]
    i+=1
m=1/theta

plt.plot(x, y)
plt.xlabel("Theta")
plt.ylabel("Chi^2")
plt.savefig('Chi')
print(m)

i=0
x=np.arange(9, 11, 0.01)
y=chi2(x)
min2=abs(min+1-y[i])
while i<len(x):
    z=abs(min+1-y[i])
    if z<min2:
        min2=z
        thetasig=x[i]
    i+=1

sigma=abs(thetasig-theta)
sigma_m=(1/theta**2)*sigma
print(sigma_m)