import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
def loadVowelData(path):
    with open(path) as f:
        f.readline()
        data = np.array([map(float, l.split(',')) for l in f])
        y = data[:, 1]
        x = data[:, 2:]
        return x, y

def dup_fig(x, y):
    colors = [None, 'black','blue','brown','purple','orange','cyan','gray','yellow','black','red','green']
    k = len(sp.unique(y))
    for i in range(1, k+1):
        inds = sp.nonzero(y == i)
        plt.plot(x[inds, 0], x[inds, 1], 'o', color=colors[i])
    plt.show()
path = '../data/vowel.train'
x, y = loadVowelData(path)
dup_fig(x, y)



