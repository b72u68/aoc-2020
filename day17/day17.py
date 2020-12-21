import copy

f = open("./data.txt")
# f = open("./test.txt")
lines = f.readlines()

data = []
ans1 = 0
ans2 = 0

ON = set()
L = list([l.strip() for l in lines])
for r, l in enumerate(L):
    for c, ch in enumerate(l):
        if ch == "#":
            ON.add((r, c, 0, 0))

def count_active(x, y, z):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                if dx != 0 or dy != 0 or dz != 0:
                    if (x+dx, y+dy, z+dz) in ON:
                        count += 1
    return count

def count_active_2(x, y, z, w):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                for dw in [-1, 0, 1]:
                    if dx != 0 or dy != 0 or dz != 0 or dw != 0:
                        if (x+dx, y+dy, z+dz, w+dw) in ON:
                            count += 1
    return count

for _ in range(6):
    NEW_ON = set()
    for x in range(-15, 15):
        for y in range(-15, 15):
            for z in range(-8, 8):
                for w in range(-8, 8):
                    active = count_active_2(x, y, z, w)
                    if (x, y, z, w) not in ON and active == 3:
                        NEW_ON.add((x, y, z, w))
                    if (x, y, z, w) in ON and active in [2, 3]:
                        NEW_ON.add((x, y, z, w))
    ON = NEW_ON
    print(len(ON))
