class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


f = open("./data.txt")
data = [int(x) for x in f.readlines()[0].strip()]

dict = {i: Node(i) for i in range(1, 1000001)}

for i in range(len(data)):
    dict[data[i]].next = dict[data[(i+1) % len(data)]]


def game(max, steps):
    cur = dict[data[0]]
    for _ in range(steps):
        picked = cur.next
        cur.next = cur.next.next.next.next
        label = cur.value
        while label in [cur.value, picked.value, picked.next.value, picked.next.next.value]:
            if label != 1:
                label -= 1
            else:
                label = max
        destination = dict[label]
        picked.next.next.next = destination.next
        destination.next = picked
        cur = cur.next


game(len(data), 100)
pointer, ans1 = dict[1], ""
for _ in range(len(data)-1):
    pointer = pointer.next
    ans1 += str(pointer.value)

print(ans1)

data.extend(list(range(max(data)+1, 1000001)))

for i in range(len(data)):
    dict[data[i]].next = dict[data[(i+1) % len(data)]]

game(1000000, 10000000)
print(dict[1].next.value * dict[1].next.next.value)
