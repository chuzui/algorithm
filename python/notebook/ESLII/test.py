from __future__ import division
from loadData import *
from tools import *
from algorithm import *

def SATest():
    data = loadSAData('../data/SAheart.data')
    XTrain = processData(data['XTrain'], std=False, scale=False)
    XTrain = XTrain[:, :][:, [0,1,2,3,5,7,8,9]]
    N, P = XTrain.shape
    y = data['y']
    name = ['intercept']
    name.append(data['name'])
    beta = logRegres(XTrain, y, maxIter=100000)
    print beta
    m = ln.inv(XTrain.T.dot(XTrain))
    ebx = np.exp(np.dot(XTrain, beta))
    p = ebx / (1.+ebx)
    sigma = np.sum((y - p) ** 2) / (N - P - 1)
    print sigma
    covarBetaHat  =  m
    print covarBetaHat.shape
    for i in range(covarBetaHat.shape[0]):
        print sp.sqrt(covarBetaHat[i][i])

def SAsplines():
    data = loadSAData('../data/SAheart.data')


SATest()

# path = '../data/vowel.train'
# x, y = loadVowelData(path)
# reduced_rank_LDA(x,y, None, None)



