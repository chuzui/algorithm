from __future__ import division
import jieba
import numpy as np
import scipy.sparse as sp

stopwordsPath = 'dict\\stopwords.txt'
STOP_WORDS = set()
with open(stopwordsPath) as f:
    for l in f:
        STOP_WORDS.add(l.strip())

def getTf(textList, wordDict):
    global STOP_WORDS
    N = len(textList)
    P = len(wordDict)
    tfMat = sp.lil_matrix((N, P), dtype=np.float64)
    for index,text in enumerate(textList):
        wordList = [w.encode('utf-8') for w in jieba.cut(text)]
        for w in wordList:
            if w in STOP_WORDS:
                continue
            if w in wordDict:
                tfMat[index, wordDict[w]] += 1
    return tfMat

def getTfidf(textList, wordDict):
    global STOP_WORDS
    N = len(textList)
    P = len(wordDict)
    tfidfMat = getTf(textList, wordDict)
    idf = np.log(float(N+1) / ((tfidfMat != 0).sum(axis=0) + 1))
    tfidfMat = tfidfMat * sp.spdiags(idf, diags=0, m=P, n=P)
    return tfidfMat



