from copy import copy
import pickle

def convertTrain():
    f = open(r'D:\data\10000.csv', 'r')
    of = open(r'D:\data\ctrain10000.csv', 'w')
    convertMap = pickle.load(open(r'd:\data\convertMap.data'))

    l = f.readline()
    title = l.split(',')
    r = range(len(title))

    title.insert(2, 'dow')
    title.pop()
    of.write(','.join(title))

    j = 0
    t = copy(title)

    for l in f:
        d = l.split(',')
        writeList = []
        for i in r:
            if i == 2:
                dow = int(d[i][4:6]) % 7
                hour = int(d[i][6:])
                writeList.append(str(convertMap['dow'][dow]))
                writeList.append(str(convertMap['hour'][hour]))
            elif i == 12:
                continue
            elif i == 1 or i == 0:
                writeList.append(d[i])
            else:
                writeList.append(str(convertMap[title[i+1]][d[i]]))
        ol = ','.join(writeList) + '\n'
        of.write(ol)

def convertTest():
    f = open(r'D:\data\10000.csv', 'r')
    of = open(r'D:\data\ctrain10000.csv', 'w')
    convertMap = pickle.load(open(r'd:\data\convertMap.data'))

    l = f.readline()
    title = l.split(',')
    r = range(len(title))

    title.insert(2, 'dow')
    of.write(','.join(title))

    j = 0
    t = copy(title)

    for l in f:
        d = l.split(',')
        writeList = []
        for i in r:
            if i == 2:
                dow = int(d[i][4:6]) % 7
                hour = int(d[i][6:])
                writeList.append(str(convertMap['dow'][dow]))
                writeList.append(str(convertMap['hour'][hour]))
            elif i == 12:
                continue
            elif i == 1 or i == 0:
                writeList.append(d[i])
            else:
                writeList.append(str(convertMap[title[i+1]].get(d[i], 0)))
        ol = ','.join(writeList) + '\n'
        of.write(ol)


convertTrain()