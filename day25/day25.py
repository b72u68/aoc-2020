f = open("./data.txt")
lines = f.readlines()

data = []
ans1 = 1

for line in lines:
    data.append(int(line.strip()))

loop = [0, 0]

for i in range(len(data)):
    v = 1
    while v != data[i]:
        v *= 7
        v %= 20201227
        loop[i] += 1

for _ in range(loop[0]):
    ans1 *= data[1]
    ans1 %= 20201227

print(ans1)
