f = open("./data.txt")
# f = open("./test.txt")
lines = f.readlines()

data = {}
data2 = {}
ans1 = 0
ans2 = 0

mask = ""
for line in lines:
    if line.startswith("mask"):
        mask = line.strip().split(" = ")[1]
    else:
        d, n = line.strip().split(" = ")
        m = int(d[4:-1])
        i = int(n)
        bi = "{0:b}".format(i)
        if len(bi) < len(mask):
            bi = "0"*(len(mask) - len(bi)) + bi
        data[m] = 0
        for i in range(len(mask)):
            if mask[i] != "X":
                data[m] += int(mask[i]) * 2**(len(mask)-1-i)
            else:
                data[m] += int(bi[i]) * 2**(len(mask)-1-i)

for _, v in data.items():
    if v != 0:
        ans1 += v

mask = ""
for line in lines:
    if line.startswith("mask"):
        mask = line.strip().split(" = ")[1]
    else:
        d, n = line.strip().split(" = ")
        m = int(d[4:-1])
        bm = "{0:b}".format(m)
        if len(bm) < len(mask):
            bm = "0"*(len(mask) - len(bm)) + bm
        result = ""
        count_b = 0
        for i in range(len(mask)):
            if mask[i] == "X" or mask[i] == "1":
                if mask[i] == "X":
                    count_b += 1
                result += mask[i]
            else:
                result += bm[i]

        com = []
        for i in range(2**count_b):
            c = "{0:b}".format(i)
            if len(c) < count_b:
                c = "0"*(count_b - len(c)) + c
            com.append(c)

        nms = []
        for c in com:
            nm = ""
            count_x = 0
            for i in range(len(result)):
                if result[i] == "X":
                    nm += c[count_x]
                    count_x += 1
                else:
                    nm += result[i]
            nms.append(int(nm, 2))

        for i in nms:
            data2[i] = int(n)

for _, v in data2.items():
    if v != 0:
        ans2 += v

print(ans1)
print(ans2)
