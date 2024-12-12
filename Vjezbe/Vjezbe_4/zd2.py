import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy import stats
from scipy import integrate

tau=2
x_data=np.linspace(0, 8, 100)
y_data=[]
y_data1=[]
y_data2=[]
y_data3=[]
i=0
while i<len(x_data):
    y_data.append((1/tau)*np.exp(-x_data[i]/tau))
    y_data1.append(np.exp(-x_data[i]))
    y_data2.append((1/3)*np.exp(-x_data[i]/3))
    y_data3.append((1/1.5)*np.exp(-x_data[i]/1.5))
    i+=1

plt.plot(x_data, y_data1, label="Tau=1")
plt.plot(x_data, y_data3, label="Tau=1.5")
plt.plot(x_data, y_data, label="Tau=2")
plt.plot(x_data, y_data2, label="Tau=3")
plt.xlabel("t [s]")
plt.ylabel("Vjerojatnost mjerenja")
plt.title("PDF funkcije")
plt.legend()
plt.savefig('PDF')

def PDF(t, tau):
    y=(1/tau)*np.exp(-t/tau)
    return y

p=integrate.quad(lambda x: PDF(x, 2), 0, 1)
print(p[0])