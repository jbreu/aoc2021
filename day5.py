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


for vent in vents:
    line = []

    if vent[1] == vent[3]:
        # vent line in x axis
        line = zip(range(vent[0], vent[2] + sign(vent[2] - vent[0]), sign(vent[2] - vent[0])), [vent[1]] * (abs(vent[2] - vent[0]) + 1))
    elif vent[0] == vent[2]:
        # vent line in y axis
        line = zip([vent[0]] * (abs(vent[3] - vent[1]) + 1), range(vent[1], vent[3] + sign(vent[3] - vent[1]), sign(vent[3] - vent[1])))
    else:
        # diagonal line
        line = zip(range(vent[0], vent[2] + sign(vent[2] - vent[0]), sign(vent[2] - vent[0])), range(vent[1], vent[3] + sign(vent[3] - vent[1]), sign(vent[3] - vent[1])))

    for x, y in line:
        diagram[x][y] += 1

counter = sum(sum(1 if value > 1 else 0 for value in line) for line in diagram)

print(counter)