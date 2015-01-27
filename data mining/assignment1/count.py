import pickle
# def convertData(l):
#     d = l.split(',')[1:]


f = open(r'D:\data\train.csv', 'r')

title = f.readline().split(',')[1:]

data = {}
for t in title:
    data[t] = {}
data['dow'] = {}
data['click'] = [0, 0]

r = range(len(title))
for l in f:
    d = l.split(',')[1:]
    isClick = int(d[0])
    data['click'][isClick]+=1
    for i in r:
        if i == 1:
            dow = int(d[i][4:6]) % 7
            hour = int(d[i][6:])
            data['dow'].setdefault(dow, [0, 0])[isClick] += 1
            data['hour'].setdefault(hour, [0, 0])[isClick] += 1
        elif i == 11 or i == 0:
            continue
        else:
            data[title[i]].setdefault(d[i], [0, 0])[isClick] += 1
oFile = open(r'd:\data\train.data', 'w')
pickle.dump(data, oFile)
pass