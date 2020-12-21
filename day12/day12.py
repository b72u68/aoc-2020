import copy

f = open("./data.txt")
# f = open("./test.txt")
lines = f.readlines()

data = []
ans1 = 0
ans2 = 0

for line in lines:
    l = line.strip()
    data.append((l[:1], int(l[1:])))

pos = {"E": 0, "N": 0, "W": 0, "S": 0}
deg = {"E": 0, "N": 90, "W": 180, "S": 270}
current = "E"

def turn(di, degree, cur):
    if di == "R":
        degree = deg[cur] - degree
        if degree < 0:
            degree = (360 + degree) % 360
        cur = list(deg.keys())[degree // 90]
    elif di == "L":
        degree = (deg[cur] + degree) % 360
        cur = list(deg.keys())[degree // 90]
    return cur

for d, n in data:
    if d == "F":
        pos[current] += n
    elif d in pos.keys():
        pos[d] += n
    else:
        current = turn(d, n, current)

ans1 = abs(pos["E"] - pos["W"]) + abs(pos["N"] - pos["S"])

wp = {"E": 10, "N": 1, "W": 0, "S": 0}
pos = {"E": 0, "N": 0, "W": 0, "S": 0}

def turn_wp(di, degree):
    tmp = copy.deepcopy(wp)
    if di == "R":
        for d in range(len(list(wp.keys()))):
            nd = d*90 - degree
            if nd < 0:
                nd = (360 + nd) % 360
            wp[list(wp.keys())[nd // 90]] = tmp[list(wp.keys())[d]]
    else:
        for d in range(len(list(wp.keys()))):
            nd = (d*90 + degree) % 360
            wp[list(wp.keys())[nd // 90]] = tmp[list(wp.keys())[d]]

for d, n in data:
    if d == "F":
        for k in wp.keys():
            pos[k] += wp[k] * n
    elif d in wp.keys():
        wp[d] += n
    else:
        turn_wp(d, n)

ans2 = abs(pos["E"] - pos["W"]) + abs(pos["N"] - pos["S"])

print(ans1)
print(ans2)
