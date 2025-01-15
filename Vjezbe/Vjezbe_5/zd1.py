import matplotlib.pyplot as plt
import numpy as np

F=[1, 2, 3, 4, 5]
a=[9.8, 21.2, 34.5, 39.9, 48.5]
err_a=[1.0, 1.9, 3.1, 3.9, 5.1]

theta=(1/(2*sum(F)/sum(np.square(err_a)))+sum(a))/sum(F)
m=1/theta
x=np.arange(0, 6, 0.5)
y=theta*x

plt.plot(x, y, label='F=a/m, m=0.0963')
plt.errorbar(F, a, err_a, fmt='o', capsize=6, label='podatci')
plt.xlabel("F [N]")
plt.ylabel("a [m/s]")
plt.legend()
plt.savefig('podatci')