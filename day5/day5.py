import math

f = open("./data.txt")
lines = f.readlines()

data = []
seat_id = []
ans1 = 0
ans2 = 0

for line in lines:
    data.append(line.strip())

for seat in data:
    row_str = seat[:7]
    col_str = seat[7:]

    row = {"lo": 0, "hi": 127}
    col = {"lo": 0, "hi": 7}

    for r in row_str:
        if r == "B":
            row["lo"] = math.ceil((row["hi"] + row["lo"]) / 2)
        else:
            row["hi"] = math.floor((row["hi"] + row["lo"]) / 2)

    for c in col_str:
        if c == "R":
            col["lo"] = math.ceil((col["hi"] + col["lo"]) / 2)
        else:
            col["hi"] = math.floor((col["hi"] + col["lo"]) / 2)

    seat_id.append(row["hi"] * 8 + col["hi"])

seat_id = sorted(seat_id)

ans1 = seat_id[-1]

for seat in range(seat_id[0], seat_id[-1]+1):
    if (seat not in seat_id and (seat+1) in seat_id) and ((seat-1) in seat_id):
        ans2 = seat

print(ans1)
print(ans2)
