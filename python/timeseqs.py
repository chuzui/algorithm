__author__ = 'Administrator'
import sys, mytimer
reps = 10000
repslist = range(reps)
op = lambda x:  x + 10
def forloop(op):
    res = []
    for x in repslist:
        res.append(op(x))
    return res

def listComp(op):
    return [op(x) for x in repslist]

def mapCall(op):
    return list(map(op, repslist))

def genExpr(op):
    return list(op(x) for x in repslist)

def genFunc(op):
    def gen():
        for x in repslist:
            yield op(x)
    return list(gen())

print(sys.version)
for test in (forloop, listComp, mapCall, genExpr, genFunc):
    func = lambda *pargs, **kargs: test(op, *pargs, **kargs)
    elapsed, result = mytimer.timer(func)
    print('-' * 33)
    print('%-9s: %5f => [%s...%s]' % (test.__name__, elapsed, result[0], result[-1]))