__author__ = 'Administrator'

from scipy import *
import numpy as np
import scipy.io as sio

def PCA(X, K, method=None):
    n, d = X.shape()

    cost = c_[d**3, n**3, min(n*d**2, d*n**2)]
    min
    pass

if __name__ == '__main__':
    dataPath = 'data/vowelTrain.mat'
    data = sio.loadmat(dataPath)
    Xtrain = data['Xtrain']
    ytrain = data['ytrain']
    B, Z = PCA(Xtrain, 2)



