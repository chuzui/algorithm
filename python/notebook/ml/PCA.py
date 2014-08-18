__author__ = 'Administrator'

from mlTool import *
import scipy.io as sio

if __name__ == '__main__':
    dataPath = 'data/vowelTrain.mat'
    data = sio.loadmat(dataPath)
    Xtrain = data['Xtrain']
    ytrain = data['ytrain']
    B, Z = PCA(Xtrain, 2)



