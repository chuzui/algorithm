import re
submission = 'submission1234.csv'
o = open('s.csv', 'w')
with open(submission, 'r') as f:
    l = f.readline()
    o.write(l)
    r = re.compile(r'[0|1]')
    for l in f:
        l = l.replace('[', '')
        l = l.replace(']', '')
        o.write(l)
