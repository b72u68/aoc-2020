import re

f = open("./data.txt")
lines = f.readlines()

data = []
infos = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

ans1 = 0
ans2 = 0

temp = {}
for line in lines:
    if line.strip() != "":
        for info in line.strip().split():
            temp[info.split(":")[0]] = info.split(":")[1]
    else:
        data.append(temp)
        temp = {}

def check_passport(passport):
    byr = passport["byr"]
    iyr = passport["iyr"]
    eyr = passport["eyr"]
    hgt = passport["hgt"]
    hcl = passport["hcl"]
    ecl = passport["ecl"]
    pid = passport["pid"]

    if not (len(byr) == 4 and int(byr) in range(1920, 2003)):
        return False
    if not (len(iyr) == 4 and int(iyr) in range(2010, 2021)):
        return False
    if not (len(eyr) == 4 and int(eyr) in range(2020, 2031)):
        return False
    if "cm" in hgt and int(hgt[:-2]) in range(150, 194):
        pass
    elif "in" in hgt and int(hgt[:-2]) in range(59, 77):
        pass
    else:
        return False
    if not (len(hcl) == 7 and re.compile(r'^#[a-z0-9].').search(hcl)):
        return False
    if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    if not len(pid) == 9:
        return False

    return True

for passport in data:
    if len(passport.keys()) != 8:
        if len(passport.keys()) == 7:
            if "cid" not in passport.keys():
                ans1 += 1
                if check_passport(passport):
                    ans2 += 1
    else:
        ans1 += 1
        if check_passport(passport):
            ans2 += 1

print(ans1)
print(ans2)
