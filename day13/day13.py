from math import gcd

f = open("./data.txt")
# f = open("./test.txt")
lines = f.readlines()

data = []
ans1 = 0
ans2 = 0

for line in lines:
    data.append(line.strip())

ar = int(data[0])
bus = []
N = 1
for i, b in enumerate(data[1].split(",")):
    if b != "x":
        bus.append(((int(b) - i) % int(b), int(b)))
        N *= int(b)

time = []
for i, b in bus:
    time.append((ar // b + 1)*b - ar)
sb = bus[time.index(min(time))][1]
ans1 = sb * ((ar // sb + 1)*sb - ar)

# Chinese remainder theorem
def mod_pow(b, e, mod):
    if e == 0:
        return 1
    elif e%2 == 0:
        return mod_pow((b*b)%mod, e/2, mod)
    else:
        return (b*mod_pow(b, e-1, mod)) % mod

def mod_inverse(x, mod):
    return mod_pow(x, mod-2, mod)

for i, b in bus:
    ni = N//b
    assert gcd(ni, b) == 1
    mi = mod_inverse(ni, b)
    assert (mi*ni)%b == 1
    assert (i*mi*ni)%b == i
    for_b = i*mi*ni
    assert for_b%b == i
    assert for_b%ni == 0
    ans2 += for_b

ans2 %= N

print(ans1)
print(ans2)
