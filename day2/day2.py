f = open("./data.txt")
lines = f.readlines()

ans1, ans2 = 0, 0

for line in lines:
    data = line.split(":")

    rules = data[0]
    password = data[1].strip()

    char = rules.split()[1]

    min_char = int(rules.split()[0].split("-")[0])
    max_char = int(rules.split()[0].split("-")[1])

    if min_char <= password.count(char) <= max_char:
        ans1 += 1
    if (password[min_char-1] == char) ^ (password[max_char-1] == char):
        ans2 += 1

f.close()

print(ans1)
print(ans2)
