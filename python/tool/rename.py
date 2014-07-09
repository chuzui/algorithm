__author__ = 'Administrator'
import sys, os

for (thisdir, subshere, fileshere) in os.walk('.'):
    for filename in fileshere:
        if filename.startswith('('):
            oldPath = os.path.join(thisdir, filename)
            newPath = os.path.join(thisdir, filename[1:])
            os.system('move %s %s' % (oldPath, newPath))