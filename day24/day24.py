import copy

f = open("./data.txt")
lines = f.readlines()

data = []
ans1 = 0
ans2 = 0

for line in lines:
    tmp = []
    i = 0
    line = line.strip()
    while i < len(line):
        if line[i] == 'w' or line[i] == 'e':
            tmp.append(line[i])
            i += 1
        elif line[i] == 's' or line[i] == 'n':
            tmp.append(f'{line[i]}{line[i+1]}')
            i += 2
    data.append(tmp)


def get_location(d):
    e, ne = 0, 0
    for c in d:
        if c == 'e':
            e += 1
        elif c == 'w':
            e -= 1
        elif c == 'ne':
            ne += 1
        elif c == 'nw':
            ne += 1
            e -= 1
        elif c == 'sw':
            ne -= 1
        elif c == 'se':
            ne -= 1
            e += 1
    return e, ne


d = {}
for i in range(len(data)):
    location = get_location(data[i])
    if location not in d.keys():
        d[location] = False
    else:
        d[location] = not d[location]


def count_black():
    result = 0
    for k, v in d.items():
        if not v:
            result += 1
    return result


ans1 = count_black()
print(ans1)


def count_adj(c, dict):
    count = 0
    e, ne = c
    adj = [(e+1, ne), (e, ne+1), (e-1, ne), (e-1, ne+1), (e, ne-1), (e+1, ne-1)]
    for coor in adj:
        if coor in dict.keys() and not dict[coor]:
            count += 1
    return count


for _ in range(100):
    tmp = copy.deepcopy(d)
    for k, v in tmp.items():
        e, ne = k
        adj = [(e+1, ne), (e, ne+1), (e-1, ne), (e-1, ne+1), (e, ne-1), (e+1, ne-1)]
        for coor in adj:
            if coor not in d.keys():
                d[coor] = True

    tmp = copy.deepcopy(d)
    for k, v in tmp.items():
        b_adj = count_adj(k, d)
        if d[k] and b_adj == 2:
            tmp[k] = False
        elif not d[k] and (b_adj == 0 or b_adj > 2):
            tmp[k] = True
    d = copy.deepcopy(tmp)

ans2 = count_black()
print(ans2)
