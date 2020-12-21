import copy

f = open("./data.txt")
lines = f.readlines()

data = []
ans1 = 0
ans2 = 0

for line in lines:
    data.append([c for c in line.strip()])

data2 = copy.deepcopy(data)

occ = "#"
emp = "L"
flr = "."

def adj(x, y, data):
    ans = 0
    if x < len(data[0]) - 1:
        if data[y][x+1] == occ:
            ans += 1
    if x > 0:
        if data[y][x-1] == occ:
            ans += 1
    if y > 0:
        if data[y-1][x] == occ:
            ans += 1
        if x < len(data[0]) - 1:
            if data[y-1][x+1] == occ:
                ans += 1
        if x > 0:
            if data[y-1][x-1] == occ:
                ans += 1
    if y < len(data) - 1:
        if data[y+1][x] == occ:
            ans += 1
        if x < len(data[0]) - 1:
            if data[y+1][x+1] == occ:
                ans += 1
        if x > 0:
            if data[y+1][x-1] == occ:
                ans += 1
    return ans

datas = []
while data not in datas:
    tmp = copy.deepcopy(data)
    datas.append(tmp)
    for i in range(len(data)):
        for j in range(len(data[i])):
            occs = adj(j, i, tmp)
            if data[i][j] == occ and occs >= 4:
                data[i][j] = emp
            elif data[i][j] == emp and occs == 0:
                data[i][j] = occ

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == occ:
            ans1 += 1

def adj_vis(x, y, data):
    ans = 0

    i, j = y, x
    while j < len(data[0]) - 1:
        if data[i][j+1] == flr:
            j += 1
        else:
            break

    if j != len(data[0]) -1 and data[i][j+1] == occ:
        ans += 1

    i, j = y, x
    while j > 0:
        if data[i][j-1] == flr:
            j -= 1
        else:
            break
    if j != 0 and data[i][j-1] == occ:
        ans += 1

    i, j = y, x
    while i < len(data) - 1:
        if data[i+1][j] == flr:
            i += 1
        else:
            break
    if i != len(data) - 1 and data[i+1][j] == occ:
        ans += 1

    i, j = y, x 
    while i > 0:
        if data[i-1][j] == flr:
            i -= 1
        else:
            break
    if i != 0 and data[i-1][j] == occ:
        ans += 1

    i, j = y, x
    while i > 0 and j > 0:
        if data[i-1][j-1] == flr:
            i -= 1
            j -= 1
        else:
            break
    if i != 0 and j != 0 and data[i-1][j-1] == occ:
        ans += 1

    i, j = y, x
    while i > 0 and j < len(data[0]) - 1:
        if data[i-1][j+1] == flr:
            i -= 1
            j += 1
        else:
            break
    if i != 0 and j != len(data[0]) - 1 and data[i-1][j+1] == occ:
        ans += 1

    i, j = y, x
    while i < len(data) - 1 and j < len(data[0]) - 1:
        if data[i+1][j+1] == flr:
            i += 1
            j += 1
        else:
            break
    if i != len(data) - 1 and j != len(data[0]) - 1 and data[i+1][j+1] == occ:
        ans += 1

    i, j = y, x
    while i < len(data) - 1 and j > 0:
        if data[i+1][j-1] == flr:
            i += 1
            j -= 1
        else:
            break
    if i != len(data) - 1 and j != 0 and data[i+1][j-1] == occ:
        ans += 1

    return ans

datas2 = []
while data2 not in datas2:
    tmp = copy.deepcopy(data2)
    datas2.append(tmp)
    for i in range(len(data2)):
        for j in range(len(data2[i])):
            occs = adj_vis(j, i, tmp)
            if data2[i][j] == occ and occs >= 5:
                data2[i][j] = emp
            elif data2[i][j] == emp and occs == 0:
                data2[i][j] = occ

for i in range(len(data2)):
    for j in range(len(data2[i])):
        if data2[i][j] == occ:
            ans2 += 1

print(ans1)
print(ans2)
