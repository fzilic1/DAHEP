import matplotlib.pyplot as plt
import numpy as np

def PDF(t, tau):
    y=(1/tau)*np.exp(-t/tau)
    return y

x_data=np.linspace(0.1, 8, 100)
y_data=[]
i=0
while i<len(x_data):
    y_data.append(PDF(1, x_data[i]))
    i+=1

plt.plot(x_data, y_data, label="t=1")
plt.xlabel("Tau [s]")
plt.ylabel("PDF")
plt.title("PDF funkcije")
plt.legend()
plt.savefig('PDFt')