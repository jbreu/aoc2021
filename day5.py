with open('input5') as f:
    vents = [line.rstrip().replace(" -> ", ",").split(",") for line in f]
    vents = [[int(num) for num in sub] for sub in vents]

max_x = max(max(j[0::2] for j in vents)) + 1
max_y = max(max(j[1::2] for j in vents)) + 1

diagram = [[0] * max_x for i in range(max_y)]


def sign(num):
    if num > 0:
        return +1
    if num < 0:
        return -1
    if num == 0:
        return 0


# special range function - in case start and stop are the same, its returning a list with same values with length of other dimension
def jrange(v1, v2, v3, v4):
    if v1 == v2:
        return [v1] * (abs(v4 - v3) + 1)
    else:
        return range(v1, v2 + sign(v2 - v1), sign(v2 - v1))


for vent in vents:
    line = zip(jrange(vent[0], vent[2], vent[1], vent[3]), jrange(vent[1], vent[3], vent[0], vent[2]))

    for x, y in line:
        diagram[x][y] += 1

counter = sum(sum(1 if value > 1 else 0 for value in line) for line in diagram)

print(counter)
