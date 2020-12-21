f = open("./data.txt")
lines = f.readlines()

data = []
ans1 = 0
ans2 = ""

for line in lines:
    raw_data = line.strip().split(" (contains ")
    i, a = raw_data[0].split(" "), raw_data[1][:-1].split(", ")
    data.append([i, a])

data = sorted(data, key=lambda x: len(x[1]))


def check_contains_1(c, seen=set()):
    for k in c.keys():
        if len(c[k]) == 1 and k not in seen:
            seen.add(k)
            return k
    return None


def check_contains_larger_1(c):
    for k in c.keys():
        if len(c[k]) > 1:
            return True
    return False


encrypt_food = {}
done = True

while done:
    for i in range(len(data)):
        if len(data[i][1]) == 1:
            contains = [x for x in data if data[i][1][0] in x[1]]
            encrypt = set(data[i][0])
            for food in contains:
                encrypt = encrypt.intersection(set(food[0]))
            encrypt_food[data[i][1][0]] = list(encrypt)

    key = check_contains_1(encrypt_food)
    while key:
        v = encrypt_food[key][0]
        for k in encrypt_food.keys():
            if k != key and v in encrypt_food[k]:
                encrypt_food[k].remove(v)
        key = check_contains_1(encrypt_food)

    for i in range(len(data)):
        for k, v in encrypt_food.items():
            if len(v) == 1:
                if v[0] in data[i][0]:
                    data[i][0].remove(v[0])
                if k in data[i][1]:
                    data[i][1].remove(k)

    done = check_contains_larger_1(encrypt_food)

for i in range(len(data)):
    ans1 += len(data[i][0])

ans2 = ",".join([v[0] for k, v in sorted(encrypt_food.items(), key=lambda item: item[0])])
print(ans1)
print(ans2)
