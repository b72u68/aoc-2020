from collections import deque

f = open("./data.txt")
lines = f.readlines()

data = {}
data2 = {}
ans1 = 0
ans2 = 0

target = "shiny gold"
for line in lines:
    outer, inner = line.strip()[:-1].split(" contain ");
    outer = outer[:-5]
    if inner != "no other bags":
        for bag in inner.split(", "):
            total = bag[0]
            if "bags" in bag:
                bag = bag[2:-5]
            else:
                bag = bag[2:-4]
            if bag not in data.keys():
                data[bag] = []
            if outer not in data2.keys():
                data2[outer] = []
            data[bag].append(outer)
            data2[outer].append((int(total), bag))

# BFS
seen = set()
Q = deque([target])
while Q:
    x = Q.popleft()
    if x not in seen:
        seen.add(x)
    for y in data.get(x, []):
        Q.append(y)

ans1 = len(seen) - 1

def size(bag):
    ans = 1
    for (n, y) in data2.get(bag, []):
        ans += n * size(y)
    return ans

ans2 = size(target) - 1
print(ans1)
print(ans2)
