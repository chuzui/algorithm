from datetime import datetime
from csv import DictReader
from math import exp, log, sqrt
import random
import numpy as np
import pickle
from sklearn.linear_model import PassiveAggressiveRegressor, PassiveAggressiveClassifier, SGDClassifier, \
    LogisticRegression

train = r'D:\data\train.csv.shuffled'               # path to training file
test = r'D:\data\test.csv'                 # path to testing file
submission = 'log.csv'  # path of to be outputted submission file

# D, training/validation
epoch = 1       # learn training data for N passes
holdafter = 29   # data after date N (exclusive) are used as validation
holdout = None  # use every N training instance for holdout validation


def logloss(p, y):
    ''' FUNCTION: Bounded logloss

        INPUT:
            p: our prediction
            y: real answer

        OUTPUT:
            logarithmic loss of p given y
    '''

    p = max(min(p, 1. - 10e-15), 10e-15)
    return -log(p) if y == 1. else -log(1. - p)


def data(path, D):
    ''' GENERATOR: Apply hash-trick to the original csv row
                   and for simplicity, we one-hot-encode everything

        INPUT:
            path: path to training or testing file
            D: the max index that we can hash to

        YIELDS:
            ID: id of the instance, mainly useless
            x: a list of hashed and one-hot-encoded 'indices'
               we only need the index since all values are either 0 or 1
            y: y = 1 if we have a click, else we have y = 0
    '''

    global convertMap
    for t, row in enumerate(DictReader(open(path))):
        # process id
        ID = row['id']
        del row['id']

        # process clicks
        y = 0.
        if 'click' in row:
            if row['click'] == '1':
                y = 1.
            del row['click']

        date = int(row['hour'][4:6])
        # build x
        x = []
        for key in row:
            if key == 'hour':
                #dow = int(row[key][4:6]) % 7
                hour = int(row[key][6:])
                #x.append(convertMap['dow'][dow])
                x.append(convertMap['hour'][hour])
            elif key == 'device_ip':
                continue
            elif key == 'C21':
                c21key = 'C21\n'
                vKey  = row[key] + '\n'
                x.append(convertMap[c21key].get(vKey, 0))
            else:
                x.append(convertMap[key].get(row[key], 0))

        #yield t, ID, np.array(x).T, np.array([y])
        yield t, date, ID, x, y


##############################################################################
# start training #############################################################
##############################################################################

start = datetime.now()

# initialize ourselves a learner
learner = SGDClassifier(penalty='l2', loss='log', alpha=0.002)
# learner = ftrl_proximal(alpha, beta, L1, L2, D, interaction)
convertMap = pickle.load(open(r'd:\data\convertMap.data'))

# start training
for e in xrange(epoch):
    loss = 0.
    count = 0

    X = []
    Y = []
    for t, date, ID, x, y in data(train, D):  # data is a generator
        #    t: just a instance counter
        # date: you know what this is
        #   ID: id provided in original data
        #    x: features
        #    y: label (click)

        # step 1, get prediction from learner

        # if t % 100 > 90:
        # if (holdafter and date > holdafter):
        if False:
            # step 2-1, calculate validation loss
            #           we do not train with the validation data so that our
            #           validation loss is an accurate estimation
            #
            # holdafter: train instances from day 1 to day N
            #            validate with instances from day N + 1 and after
            #
            # holdout: validate with every N instance, train with others
            continue
            if len(Y) > 0:
                learner.partial_fit(np.array(X), np.array(Y), classes=[0,1])
                X = []
                Y = []
            x = np.array(x).T
            y = np.array([y])
            p = learner.predict_proba(np.array(x).T)
            loss += logloss(p[0][1], y)
            count += 1
        else:
            # step 2-2, update learner with label (click) information
            X.append(x)
            Y.append(y)
            if len(Y) == 100:
                learner.partial_fit(np.array(x).T,  np.array([y]), classes=[0,1])
                X = []
                Y = []
            # if t % 100 != 99:
            #     X.append(x)
            #     Y.append(y)
            # else:
            #     learner.partial_fit(np.array(x).T,  np.array([y]), classes=[0,1])
            #     X = []
            #     Y = []

    if len(Y) > 0:
        learner.partial_fit(np.array(X), np.array(Y), classes=[0,1])
        X = []
        Y = []

    # for t, date, ID, x, y in data(train, D):
    #     if (holdafter and date > holdafter):
    #         x = np.array(x).T
    #         y = np.array([y])
    #         p = learner.predict_proba(np.array(x).T)
    #         loss += logloss(p[0][1], y)
    #         count += 1


    # print('Epoch %d finished, validation logloss: %f, elapsed time: %s' % (
    #      e, loss/count, str(datetime.now() - start)))


##############################################################################
# start testing, and build Kaggle's submission file ##########################
##############################################################################

with open(submission, 'w') as outfile:
    outfile.write('id,click\n')
    for t, date, ID, x, y in data(test, D):
        x = np.array(x).T
        y = np.array([y])
        p = learner.predict_proba(x)
        outfile.write('%s,%s\n' % (ID, str(p[0  ][1])))