f = open("./data.txt")
lines = f.readlines()

data = []
ans1 = 0
ans2 = 0

temp = []
n = 0

for line in lines:
    if line.strip() != "":
        for char in line.strip():
            temp.append(char)
        n += 1
    else:
        data.append([n, temp])
        temp = []
        n = 0

for ans in data:
    n, temp = ans
    s = set(temp)
    ans1 += len(s)
    for char in s:
        if temp.count(char) == n:
            ans2 += 1

print(ans1)
print(ans2)
