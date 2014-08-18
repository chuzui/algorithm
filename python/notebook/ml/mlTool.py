__author__ = 'chuzui'
from scipy import *
import numpy as np
from scipy import linalg

def fisherLdaFit(Xtrain, ytrain):
    C = max(ytrain)

    if C == 2:
        ndx1 = nonzero(ytrain == 1)
        ndx2 = nonzero(ytrain == 2)

        m1 = mean(Xtrain[ndx1[0], :], 0)
        m2 = mean(Xtrain[ndx2[0], :], 0)
        s1 = cov(Xtrain[ndx1[0], :].T, bias=1)
        s2 = cov(Xtrain[ndx2[0], :].T, bias=1)
        sw = s1+ s2
        W = linalg.inv(sw).dot(m1 - m2)
    Z = Xtrain * W
    return W, Z

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