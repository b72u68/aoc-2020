f = open("./data.txt")
# f = open("./test.txt")
lines = f.readlines()

data = {}
user_tickets = []
near_tickets = []
OK = [[True for _ in range(20)] for _ in range(20)]
ans1 = 0
ans2 = 1

i = 0
while i < len(lines):
    if lines[i].strip() != "" and lines[i].strip() not in ("your ticket:", "nearby tickets:"):
        r = lines[i].strip().split(": ")
        field = r[0]
        r1, r2 = r[1].split(" or ")
        data[field] = []
        lo, hi = int(r1.split("-")[0]), int(r1.split("-")[1])
        data[field].extend([lo, hi])
        lo, hi = int(r2.split("-")[0]), int(r2.split("-")[1])
        data[field].extend([lo, hi])
        i += 1
    elif lines[i].strip() == "your ticket:":
        tickets = lines[i+1].split(",")
        user_tickets = [int(x) for x in tickets]
        i += 2
    elif lines[i].strip() == "nearby tickets:":
        i += 1
        break
    else:
        i += 1

while i < len(lines):
    tmp = []
    tickets = [int(x) for x in lines[i].split(",")]
    valid = True
    for x in tickets:
        valid = False
        for a, b, c, d in data.values():
            if a <= x <= b or c <= x <= d:
                valid = True
                tmp.append(x)
                break
        if not valid:
            ans1 += x
    near_tickets.append(tmp)
    i += 1

for h in range(len(near_tickets)):
    for i, v in enumerate(near_tickets[h]):
        for j, k in enumerate(data.keys()):
            a, b, c, d = data[k]
            if not (a <= v <= b or c <= v <= d):
                OK[i][j] = False

MAP = [None for _ in range(20)]
USED = [False for _ in range(20)]
found = 0
while True:
    for i in range(20):
        valid_j = [j for j in range(20) if OK[i][j] and not USED[j]]
        print(i, valid_j)
        if len(valid_j) == 1:
            MAP[i] = valid_j[0]
            USED[valid_j[0]] = True
            found += 1
    if found == 20:
        break

for i, v in enumerate(MAP):
    if v in range(6):
        ans2 *= user_tickets[i]

print(ans1)
print(ans2)
