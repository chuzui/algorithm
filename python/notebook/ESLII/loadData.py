from __future__ import division
import numpy as np
import scipy as sp
import numpy.linalg as ln

def loadSAData(path):
    data = {}
    with open(path) as f:
        data['name'] = f.readline().split(',')[1:-1]

        XTrain = []
        y = []
        for l in f:
            ls = l.split(',')
            XTrain.append(map(float, ls[1:-1]))
            y.append([float(ls[-1])])
        data['XTrain'] = np.array(XTrain)
        data['y'] = np.array(y)
        return data

def loadVowelData(path):
    with open(path) as f:
        f.readline()
        data = np.array([map(float, l.split(',')) for l in f])
        y = data[:, 1]
        x = data[:, 2:]
        return x, y