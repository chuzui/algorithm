import json

path = '{}.json'

N = 20
id_dict = set()
dump_num = 0
for i in range(1, N+1):
    with open(path.format(i), 'r') as f:
        for line, l in enumerate(f):
            art_json = json.loads(l)
            try:
                id = art_json['artObject']['objectNumber']
            except Exception as err:
                print i
                print line
                continue

            if id in id_dict:
                dump_num += 1
            else:
                id_dict.add(id)

path = '../url/id'

lost_num = 0
with open(path, 'r') as id_file, open('lost_id', 'w') as lost_file:
    for l in id_file:
        id = l.strip()
        if not id in id_dict:
            lost_file.write(id + '\n')
            lost_num += 1

print lost_num