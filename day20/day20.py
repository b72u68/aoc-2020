# f = open("./data.txt")
f = open("./test.txt")
lines = f.readlines()

data = {}
blocks = {}
share = {}
ans1 = 0
ans2 = 0

# read data
i = 0
tile = 0
while i < len(lines):
    line = lines[i].strip()
    if line:
        if "Tile" in line:
            tile = int(line[5:-1])
            data[tile] = []
        else:
            data[tile].append(line)
    i += 1

# get block sides
for k, v in data.items():
    top = v[0]
    bot = v[-1]
    left = "".join([x[0] for x in v])
    right = "".join([x[-1] for x in v])
    blocks[k] = [top, bot, left, right]


# check if 2 blocks is adjacent
def adjacent(b1, b2):
    t, b, l, r = blocks[b1]
    if t in blocks[b2] or t[::-1] in blocks[b2]:
        return True
    elif b in blocks[b2] or b[::-1] in blocks[b2]:
        return True
    elif l in blocks[b2] or l[::-1] in blocks[b2]:
        return True
    elif r in blocks[b2] or r[::-1] in blocks[b2]:
        return True
    return False


corners = []
keys = list(blocks.keys())
for i in range(len(keys)):
    share[keys[i]] = []
    for j in range(len(keys)):
        if keys[i] != keys[j]:
            if adjacent(keys[i], keys[j]):
                share[keys[i]].append(keys[j])
    if len(share[keys[i]]) == 2:
        corners.append(keys[i])
