from __future__ import division
import pickle
from math import log

data = pickle.load(open(r'd:\data\train.data'))
D = len(data) - 1
bias = (D-1) / D * log(data['click'][0] / data['click'][1])

convertMap = {}
for key, value in data.iteritems():
    print key
    if key != 'click' and  key != 'device_ip':
        for category, count in value.iteritems():
            newValue = log((count[0]+1) / (count[1]+1)) - bias
            convertMap.setdefault(key, {})[category] = newValue

pickle.dump(convertMap, open(r'd:\data\convertMap.data', 'w'))
