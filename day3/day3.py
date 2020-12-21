f = open("./data.txt")
lines = f.readlines()

data = []

for line in lines:
    temp = []
    for char in line.strip():
        temp.append(char)
    data.append(temp)

def main(stepx, stepy):
    x = 0
    y = 0
    ans = 0
    while y < len(data):
        if data[y][x] == "#":
            ans += 1
        x = (x + stepx) % len(data[y])
        y += stepy
    return ans

if __name__ == "__main__":
    ans1 = main(3, 1)
    ans2 = main(1, 1) * main(3, 1) * main(5, 1) * main(7, 1) * main(1, 2)
    print(ans1)
    print(ans2)
