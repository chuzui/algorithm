filename = r'data.txt'
import pprint
t = {}
for index, line in enumerate(open(filename)):
    l = [t.strip() for t in  line.split()]
    for teacher in l:
        if not teacher in t:
            t[teacher] = [index+1]
        else:
            t[teacher].append(index+1)

one = 0
two = 0
onelist = []
for key in t.keys():
    if len(t[key]) == 1:
        onelist.append(key)
for value in t.values():
    if len(value) == 1:
        one +=1
    else:
        two +=1

pprint.pprint(t)
print(len(t.keys()))
print(one)
print(two)

print(onelist)