f = open("./data.txt")
lines = f.readlines()

data = []
ans1 = 0
ans2 = 0

for line in lines:
    data.append(int(line.strip()))

data = sorted(data)
data = [0] + data + [max(data) + 3]
one = 0
three = 0

for i in range(len(data)-1):
    if data[i+1] - data[i] == 1:
        one += 1
    elif data[i+1] - data[i] == 3:
        three += 1

ans1 = one*three

DP = {}
def arrange(l, i):
    if len(l) - 1 == i:
        return 1
    if i in DP:
        return DP[i]
    count = 0
    for j in range(i+1, len(l)):
        if l[j] - l[i] <= 3:
            count += arrange(l, j)
    DP[i] = count
    return count

ans2 = arrange(data, 0)

print(ans1)
print(ans2)
