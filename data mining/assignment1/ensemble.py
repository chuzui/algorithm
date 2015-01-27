import numpy as np
import numpy.random as nrandom
from sklearn import tree
from sklearn.ensemble import GradientBoostingClassifier


def rf(XTrain, y, XTest, B=50):
    N,P = XTrain.shape
    trees = []
    sampleN = int(N * 0.7)
    sampleP = int(np.sqrt(P))
    for i in range(B):
        sampleNIndex = nrandom.choice(range(N),size=sampleN)
        #samplePIndex = nrandom.choice(range(P),size=sampleP)
        t = tree.DecisionTreeClassifier(max_features=sampleP, splitter='random')
        t.fit(XTrain[sampleNIndex, :], y[sampleNIndex])
        trees.append(t)

    classes = np.unique(y)
    C = len(classes)
    NT = XTest.shape[0]
    p = np.zeros((NT, C), dtype=np.int64)
    for t in trees:
        predy = t.predict(XTest)
        for i, index in enumerate(predy):
            p[i, index] +=1
    return classes[np.argmax(p, axis=1)]

def adaboost(XTrain, y, XTest, T=800):
    N,P = XTrain.shape
    classes = np.unique(y)
    C = len(classes)
    trees = []
    alpha = np.zeros((T,), dtype=np.float64)
    w = np.ones((N,), dtype=np.float64) / N
    i = 0
    for m in range(T):
        t = tree.DecisionTreeClassifier(max_depth=4, splitter='random', max_features=500)
        t.fit(XTrain, y, sample_weight=w)
        trees.append(t)
        pred = t.predict(XTrain)
        err = np.sum(w * (pred != y))
        alpha[m] = np.log((1 - err) / err) + np.log(C-1)
        w = w * np.exp(alpha[m] * (pred != y))
        w = w / np.sum(w)

    p = np.zeros((XTest.shape[0], C), dtype=np.float64)
    row = np.arange(XTest.shape[0])
    for i, t in enumerate(trees):
        pred = t.predict(XTest)
        p[row, pred] += alpha[i]
    return classes[np.argmax(p, axis=1)]

def gb(XTrain, y, XTest):
    clf = GradientBoostingClassifier(n_estimators=200, learning_rate=1.0, max_depth=2)
    clf.fit(XTrain, y)
    return clf.predict(XTest)
