f = open("./data.txt")
lines = f.readlines()

data = []
ans1 = 0
ans2 = 0

for line in lines:
    data.append(int(line.strip()))

def check(l, t):
    s = set(l)
    for i in l:
        if t - i in s:
            return True
    return False

pos = -1
for i in range(25, len(data)):
    l = data[i-25:i]
    if not check(l, data[i]):
        ans1 = data[i]
        pos = i
        break

for i in range(len(data)):
    for j in range(i+2, len(data)):
        tmp = data[i:j]
        if sum(tmp) == ans1:
            ans2 = min(tmp) + max(tmp)
            break

print(ans1)
print(ans2)
