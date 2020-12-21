f = open("./data.txt")
lines = f.readlines()

data = []
ans1 = 0
ans2 = 0

for line in lines:
    data.append(line.strip())


def parse(eqn, is_part_2=False):
    eqn = eqn.replace("(", "( ")
    eqn = eqn.replace(")", " )")

    tokens = eqn.split()[::-1]
    stk = []
    ops = []
    for token in tokens:
        if token == '(':
            while ops[-1] != ")":
                stk.append(ops.pop())
            ops.pop()
        elif token == "*":
            while is_part_2 and ops and ops[-1] == "+":
                stk.append(ops.pop())
            ops.append(token)
        elif token in ")+":
            ops.append(token)
        else:
            stk.append(int(token))

    while ops:
        stk.append(ops.pop())

    cur = []
    for val in stk:
        if val == "+":
            x = cur[-1] + cur[-2]
            cur.pop()
            cur.pop()
            cur.append(x)
        elif val == "*":
            x = cur[-1] * cur[-2]
            cur.pop()
            cur.pop()
            cur.append(x)
        else:
            cur.append(val)

    return cur[0]


for line in data:
    ans1 += parse(line, False)
    ans2 += parse(line, True)

print(ans1)
print(ans2)
