from __future__ import division
import numpy as np
import scipy as sp
import numpy.linalg as ln

def processData(X, **opts):
    N,M = X.shape
    if opts.get('std', True):
        X = X - np.mean(X, 0)
    if opts.get('scale', True):
        X = X / (X.max(0) - X.min(0))
    if opts.get('addones', True):
        X = sp.c_[sp.ones((N,1)), X]
    return X

def dup_fig(x, y):
    colors = [None, 'black','blue','brown','purple','orange','cyan','gray','yellow','black','red','green']
    k = len(sp.unique(y))
    for i in range(1, k+1):
        inds = sp.nonzero(y == i)
        plt.plot(x[inds, 0], x[inds, 1], 'o', color=colors[i])
    plt.show()