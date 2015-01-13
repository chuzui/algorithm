from __future__ import division
import numpy as np
import numpy.random as nrandom

class Node:
    def __init__(self, feauture_index = None,threshold=None, value=None):
        self.feauture_index = feauture_index
        self.threshold = threshold
        self.value = value
        self.leftNode = None
        self.rightNode = None

class DecisionTreeBase:
    def __init__(self, max_depth=10000, min_samples=1):
        self.max_depth = max_depth
        self.min_sample = min_samples

    def fit(self, X, y):
        self.topNode = self.genNode(X, y)

    def predict(self, X):
        N, P = X.shape
        y = []
        for i in range(N):
            node = self.topNode
            while True:
                if node.feauture_index == None:
                    y.append(node.value)
                    break
                if X[i, node.feauture_index] <= node.threshold:
                    node = node.leftNode
                else:
                    node = node.rightNode
        return np.array(y)

class DecisionTreeClassifier(DecisionTreeBase):
    # def __init__(self, max_depth=10000, min_samples=1):
    #     super(DecisionTreeClassifier, self).__init__(max_depth, min_samples)

    def split(self, X, y):
        N, P = X.shape
        minGini= 1000000
        for i in xrange(P):
            x = X[:, i]
            sortedIndex = np.argsort(x, axis=0)
            for j, index in enumerate(sortedIndex[:-1]):
                if j != N - 2 and x[index] == x[sortedIndex[j+1]]:
                    continue
                gini = (j+1) / N * self.calcGini(y[sortedIndex[:j+1]]) + (N - j - 1) / N * self.calcGini(y[sortedIndex[j+1:]])
                if gini < minGini:
                    minGini = gini
                    threshold = x[index]
                    feautureIndex = i
                    leftIndex = sortedIndex[:j+1]
                    rightIndex = sortedIndex[j+1:]
        return feautureIndex,threshold, leftIndex, rightIndex


    def calcGini(self, y):
        classes = np.lib.arraysetops.unique(y)
        N = len(y)
        C = len(classes)
        classCount = np.array([[np.sum(y == c)] for c in classes])
        classPrior = classCount / float(N)
        giny = 1 - np.sum(classPrior ** 2)
        return giny

    def genNode(self, X, y):
        N, P = X.shape
        if len(np.lib.arraysetops.unique(y)) == 1:
            return Node(value=y[0])
        if N <= self.min_sample:
            return Node(value=np.argmax(np.bincount(y)))
        feautureIndex,threshold, leftIndex, rightIndex = self.split(X, y)
        node = Node(feauture_index=feautureIndex, threshold=threshold)
        node.leftNode = self.genNode(X[leftIndex], y[leftIndex])
        node.rightNode = self.genNode(X[rightIndex], y[rightIndex])
        return node

class DecisionTreeRegression(DecisionTreeBase):
    # def __init__(self, max_depth=10000, min_samples=1):
    #     super(DecisionTreeClassifier, self).__init__(max_depth, min_samples)

    def split(self, X, y):
        N, P = X.shape
        minVar= 100000000
        for i in xrange(P):
            x = X[:, i]
            sortedIndex = np.argsort(x, axis=0)
            for j, index in enumerate(sortedIndex[:-1]):
                if j != N - 2 and x[index] == x[sortedIndex[j+1]]:
                    continue
                var = (j+1) / N * np.var(y[sortedIndex[:j+1]]) + (N - j - 1) / N * np.var(y[sortedIndex[j+1:]])
                if var < minVar:
                    minVar = var
                    threshold = x[index]
                    feautureIndex = i
                    leftIndex = sortedIndex[:j+1]
                    rightIndex = sortedIndex[j+1:]
        return feautureIndex,threshold, leftIndex, rightIndex

    def genNode(self, X, y):
        N, P = X.shape
        if N <= self.min_sample:
            return Node(value=np.mean(y))
        feautureIndex,threshold, leftIndex, rightIndex = self.split(X, y)
        node = Node(feauture_index=feautureIndex, threshold=threshold)
        node.leftNode = self.genNode(X[leftIndex], y[leftIndex])
        node.rightNode = self.genNode(X[rightIndex], y[rightIndex])
        return node


def DT(Xtrain, y, XTest, isRegression=False):
    if isRegression:
        tree = DecisionTreeRegression(min_samples=5)
    else:
        tree = DecisionTreeClassifier(min_samples=5)
    tree.fit(Xtrain, y)
    return tree.predict(XTest)

def SDT(Xtrain, y, XTest, isRegression=False):
    N = Xtrain.shape[0]
    K = 10
    M = 20
    minNode = range(1,1+M)
    index = range(N)
    nrandom.shuffle(index)
    groupSize = N // K
    gX = []
    gy = []
    for i in range(K):
        if i != K-1:
            groupIndex = index[groupSize * i : groupSize * (i + 1)]
        else:
            groupIndex = index[groupSize * i : ]
        gX.append(Xtrain[groupIndex])
        gy.append(y[groupIndex])

    if isRegression:
        Tree = DecisionTreeRegression
    else:
        Tree = DecisionTreeClassifier

    mX = []
    my = []
    for i in range(K):
        x = [[] for j in range(gX[i].shape[0])]
        for j in range(M):
            tree = Tree(min_samples=minNode[j])
            tree.fit(gX[i], gy[i])
            yPred = tree.predict(gX[i])
            for k, l in enumerate(x):
                l.append(yPred[k])
        mX += x
    mX = np.array(mX)
    my = y[index]

    metaTree = Tree(min_samples=5)
    metaTree.fit(mX, my)
    f = []
    for i in range(M):
        tree = Tree(min_samples=minNode[i])
        tree.fit(Xtrain, y)
        f.append(tree)

    x = [[] for j in range(XTest.shape[0])]
    for i in range(M):
        yPred = f[i].predict(XTest)
        for k, l in enumerate(x):
            l.append(yPred[k])

    return metaTree.predict(np.array(x))

# X = np.array([[0, 0], [1, 1]])
# y = np.array([0, 1])
# a = DecisionTreeClassifier()
# a.fit(X, y)
# print a.predict(np.array([[2., 2.]]))