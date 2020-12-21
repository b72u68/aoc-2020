import copy

test = [14, 1, 17, 0, 3, 20]
ans1 = 0
ans2 = 0

def get_turn_number(max_turn, data=copy.deepcopy(test)):
    spoken = {}
    for i, n in enumerate(data):
        spoken[n] = {"last": i+1, "prev": None}

    turn = len(data)

    while turn < max_turn:
        if data[turn-1] in spoken.keys():
            if spoken[data[turn-1]]["prev"]:
                n = spoken[data[turn-1]]["last"] - spoken[data[turn-1]]["prev"]
                data.append(n)
                if n in spoken.keys():
                    spoken[n]["last"], spoken[n]["prev"] = turn + 1, spoken[n]["last"]
                else:
                    spoken[n] = {"last": turn + 1, "prev": None}
            else:
                data.append(0)
                spoken[0]["last"], spoken[0]["prev"] = turn + 1, spoken[0]["last"]
        else:
            spoken[data[turn-1]] = {"last": turn + 1, "prev": None}
            data.append(0)
            spoken[0]["last"], spoken[0]["prev"] = turn + 1, spoken[0]["last"]
        turn += 1
    return data[-1]

ans1 = get_turn_number(2020)
ans2 = get_turn_number(30000000)
print(ans1)
print(ans2)
