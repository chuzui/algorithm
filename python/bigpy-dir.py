# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import os, glob, sys, pprint
try:
    dir = r'D:\百度云同步盘\bookyun'

    allsize = []
    allpy = glob.glob(dir + os.sep + '*.py')
    for (dirname, subshere, fileshere) in os.walk(dir):
        for filename in fileshere:
            fullname = os.path.join(dirname, filename)
            fullsize = os.path.getsize(fullname)
            allsize.append((fullsize, fullname))

    allsize.sort()
    pprint.pprint(allsize[:2])
    pprint.pprint(allsize[-2:])
except Exception as e:
    print(e)



x = input()