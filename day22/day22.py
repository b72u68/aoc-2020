import copy

f = open("./data.txt")
lines = f.readlines()

data = {}
games = {}

p = 0
for line in lines:
    if "Player" in line:
        p = int(line.strip()[7:-1])
        data[p] = []
    elif line.strip():
        data[p].append(int(line.strip()))

data2 = copy.deepcopy(data)


# part 1
def part1(decks):
    result = 0
    while len(decks[1]) > 0 and len(decks[2]) > 0:
        p1 = decks[1].pop(0)
        p2 = decks[2].pop(0)
        if p1 > p2:
            decks[1].extend([p1, p2])
        else:
            decks[2].extend([p2, p1])

    for k, v in decks.items():
        if len(v) > 0:
            for i in range(len(v)):
                result += (len(v) - i) * v[i]
    return result


# check for duplicate decks
def check_decks(decks, game):
    for deck in games[game]:
        if decks[1] == deck[0] and decks[2] == deck[1]:
            return True
    return False


# return the winner of subgame
def subgame(decks, game):
    if game not in games.keys():
        games[game] = []

    while len(decks[1]) > 0 and len(decks[2]) > 0:
        if not check_decks(decks, game):
            d1 = copy.deepcopy(decks[1])
            d2 = copy.deepcopy(decks[2])
            games[game].append([d1, d2])
            p1 = decks[1].pop(0)
            p2 = decks[2].pop(0)
            if len(decks[1]) >= p1 and len(decks[2]) >= p2:
                s1 = copy.deepcopy(decks[1][:p1])
                s2 = copy.deepcopy(decks[2][:p2])
                winner = subgame({1: s1, 2: s2}, max(list(games.keys()))+1)
                if winner == 1:
                    decks[1].extend([p1, p2])
                else:
                    decks[2].extend([p2, p1])
            elif p1 > p2:
                decks[1].extend([p1, p2])
            else:
                decks[2].extend([p2, p1])
        else:
            return 1

    if len(decks[1]):
        return 1
    else:
        return 2


# part 2
def part2(decks):
    result = 0
    winner = subgame(decks, 1)

    for i in range(len(decks[winner])):
        result += (len(decks[winner]) - i) * decks[winner][i]

    return result


print(part1(data))
print(part2(data2))
