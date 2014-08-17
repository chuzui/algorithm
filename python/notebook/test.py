%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import pickle

from scipy.stats import uniform
from scipy.stats import norm
N = 100
M = 25
x = uniform.rvs(size=(N,M))
for a in x:
    a.sort()
y = sp.sin(2*sp.pi*x) + norm.rvs(scale=0.3, size=(N,M))
# with open('synthetic.dat', 'wb') as f:
#     pickle.dump((x,y), f)
#
# with open('synthetic.dat', 'rb') as f:
#     x,y = pickle.load(f)
sx = np.linspace(0,1,25)
sy = sp.sin(2*sp.pi*sx)
plt.plot(sx,sy)
for i in range(20):
    plt.plot(x[i],y[i], 'o', color='red')