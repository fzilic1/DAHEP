import scipy as sp
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

x_data = np.arange(100, 300, 1)
y_data=stats.norm.pdf(x_data, 200, 2)
y_data2=stats.norm.pdf(x_data, 150, 1)
y_data3=stats.norm.pdf(x_data, 250, 3)

plt.plot(x_data, y_data, label='m=200, sig=2')
plt.plot(x_data, y_data2, label='m=150, sig=1')
plt.plot(x_data, y_data3, label='m=250, sig=3')
plt.title("Gaussove krivulje")
plt.xlabel('Energija [GeV]')
plt.ylabel('Vjerojatnost produkcije')
plt.legend()
plt.savefig("gauss.jpg")