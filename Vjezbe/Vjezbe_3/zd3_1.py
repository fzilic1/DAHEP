import scipy as sp
from scipy import stats
from scipy import integrate
import numpy as np

p1=integrate.quad(lambda x: stats.norm.pdf(x, 200, 2), 205, np.inf)
p2=integrate.quad(lambda x: stats.norm.pdf(x, 200, 2), 199, 201)
p3=integrate.quad(lambda x: stats.norm.pdf(x, 200, 2), 203, np.inf)
print(p1[0])
print(p2[0])
print(p3[0]*p3[0])