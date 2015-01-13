import random
import datetime

def data(n):
    for i in xrange(n):
        yield i

a =data(100000000)

def text(it):
    for x in it:
        print x

def t(it):
    text(it)

t(a)
