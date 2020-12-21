import copy

f = open("./data.txt")
lines = f.readlines()

data = []
ans1 = 0
ans2 = 0

for line in lines:
    op, val = line.strip().split(" ")
    data.append([op, int(val)])

def run(data, ans=0):
    seen = []
    i = 0
    while i not in seen and i < len(data):
        seen.append(i)
        op, val = data[i]
        if op == "jmp":
            i = (i + val)
        if op == "nop":
            i += 1
        if op == "acc":
            ans += val
            i += 1
    return (i, ans)

ans1 = run(data)[1]

for j in range(len(data)):
    temp = copy.deepcopy(data)
    if data[j][0] == "nop":
        temp[j][0] = "jmp"
        n = run(temp, 0)[0]
        if n == len(data):
            data[j][0] = "jmp"
            break
    elif data[j][0] == "jmp":
        temp[j][0] = "nop"
        n = run(temp, 0)[0]
        if n == len(data):
            data[j][0] = "nop"
            break

ans2 = run(data)[1]

print(ans1)
print(ans2)
