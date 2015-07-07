import re

path = 'data{}.json'

N = 20

r = re.compile('}{')
for i in range(1, N+1):
    with open(path.format(i), 'r') as f, open(str(i)+'.json', 'w') as out_file:
        for l in f:
            out_file.write(r.sub('}\n{', l).strip())

