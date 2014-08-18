__author__ = 'Administrator'

from scipy import *
import numpy as np
import scipy.io as sio
from scipy import linalg

def PCA(X, K, method=None):
    n, d = X.shape

    cost = [d**3, n**3, min(n*d**2, d*n**2)]
    junk =  min(cost)
    method = cost.index(junk)

    methodNames = {'eig(Xt X)', 'eig(X Xt)', 'SVD(X)'}

    X, mu = centerCols(X);
    if method == 0:
        evals,  evec= linalg.eig(cov(X, rowvar=0, ddof = 0))
        idx = np.argsort(-evals)
        evals = evals[idx]
        evec = evec[:, idx]
        B = evec[:, :K]
        print B

    Z = X.dot(B)
    Xrecon = Z.dot(B.T) + tile(mu, (n, 1))

    return B, Z, evals, Xrecon, mu

def centerCols(X, mu=None):
    if mu is None:
        mu = mean(X, 0)
    X = X - mu
    return X, mu


if __name__ == '__main__':
    dataPath = 'data/vowelTrain.mat'
    data = sio.loadmat(dataPath)
    Xtrain = data['Xtrain']
    ytrain = data['ytrain']
    B, Z = PCA(Xtrain, 2)



