f = open("./data.txt")
nums = f.readlines()

arr = []
for num in nums:
    arr.append(int(num))

f.close()

arr = sorted(arr)

def part1(start, end, total):
    i, j = start, end

    while i < j:
        if arr[i] + arr[j] < total:
            i += 1
        elif arr[i] + arr[j] > total:
            j -= 1
        else:
            return [i, j]
    return [None, None]

def part2():
    for i in range(len(arr)-2):
        j, k = part1(i+1, len(arr)-1, 2020-arr[i])
        if (j != None and k != None):
            return arr[j] * arr[i] * arr[k]

if __name__ == "__main__":
    i, j = part1(0, len(arr)-1, 2020)
    print(arr[i]*arr[j])
    print(part2())
