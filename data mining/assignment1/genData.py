import os
import numpy as np
import tfidf
import sparseIO
import jieba
dirPath = 'lily'
def readFile(filePath):
    fileName = os.path.basename(filePath).split('.')[0]
    with open(filePath) as f:
        for line in f:
            yield line

def genWordDict():
    ws = set()
    stopwordsPath = 'dict\\stopwords.txt'
    STOP_WORDS = set()
    with open(stopwordsPath) as f:
        for l in f:
            STOP_WORDS.add(l.strip())
    for filePath in os.listdir(dirPath):
        fileName = filePath.split('.')[0]

        for l in readFile(os.path.join(dirPath, filePath)):
            wordlist = jieba.cut(l)
            ws = ws.union(set(wordlist))
    for w in STOP_WORDS:
        if w in ws:
            ws.remove(w)
    ws = map(lambda x: x.encode('utf-8'), ws)
    print len(ws)
    with open('worddict.txt', 'w') as f:
        f.write('\n'.join(list(ws)))

def readFile(filePath):
    fileName = os.path.basename(filePath).split('.')[0]
    with open(filePath) as f:
        for line in f:
            yield line

def loadText():
    textList = []
    y = []
    c = 0
    for filePath in os.listdir(dirPath):
        fileName = filePath.split('.')[0]
        for l in readFile(os.path.join(dirPath, filePath)):
            textList.append(l)
            y.append([c])
        c += 1
    return textList, np.array(y)

def loadWordDict():
    dictPath = 'dict\\worddict.txt'
    worddict = {}
    with open(dictPath) as f:
        for index, l in enumerate(f):
            worddict[l[:-1]] = index
    print index
    return worddict

def genTfidfData():
    tfDataFile = 'data\\tfData'
    tfidfDataFile = 'data\\tfidfData'
    WORD_DICT = loadWordDict()
    textList, y = loadText()
    XTfidf = tfidf.getTfidf(textList, WORD_DICT)
    sparseIO.save_sparse_matrix(tfidfDataFile, XTfidf)
    XTf = tfidf.getTf(textList, WORD_DICT)
    sparseIO.save_sparse_matrix(tfDataFile, XTf)
    np.save('y', y)

genTfidfData()