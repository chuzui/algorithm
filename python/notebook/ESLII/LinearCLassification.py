from __future__ import division
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

def reduced_rank_LDA(XTrain, yTrain, XTest, yTest):
    K = len(sp.unique(yTrain))
    N = XTrain.shape[0]
    p = XTrain.shape[1]

    PiK = sp.zeros((K, 1))
    M = sp.zeros((K, p))
    ScatterMatrix = []
    for ci in range(1, K+1):
        inds = sp.nonzero(yTrain == ci)
        Nci = len(inds[0])
        PiK[ci-1] = Nci / N
        #print XTrain[inds, :]
        M[ci-1, :] = sp.mean(XTrain[inds[0], :], 0)
    print PiK
    print M


path = '../data/vowel.train'
x, y = loadVowelData(path)
reduced_rank_LDA(x,y, None, None)



