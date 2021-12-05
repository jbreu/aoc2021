with open('input5') as f:
    vents = [line.rstrip().replace(" -> ", ",").split(",") for line in f]
    vents = [[int(num) for num in sub] for sub in vents]

max_x = max(max(j[0::2] for j in vents)) + 1
max_y = max(max(j[1::2] for j in vents)) + 1

diagram = [[0] * max_x] * max_y

for vent in vents:
    # vent line in x axis
    if vent[1] == vent[3]:
        if vent[0] < vent[2]:
            diagram[vent[1]] = [cell + 1 if i >= vent[0] and i <= vent[2] else cell for i, cell in enumerate(diagram[vent[1]])]
        else:
            diagram[vent[1]] = [cell + 1 if i <= vent[0] and i >= vent[2] else cell for i, cell in enumerate(diagram[vent[1]])]

# transpose diagram
diagram = list(map(list, zip(*diagram)))

for vent in vents:
    # vent line in x axis
    if vent[0] == vent[2]:
        if vent[1] < vent[3]:
            diagram[vent[0]] = [cell + 1 if i >= vent[1] and i <= vent[3] else cell for i, cell in enumerate(diagram[vent[0]])]
        else:
            diagram[vent[0]] = [cell + 1 if i <= vent[1] and i >= vent[3] else cell for i, cell in enumerate(diagram[vent[0]])]

# transpose diagram back
diagram = list(map(list, zip(*diagram)))

counter = sum(sum(1 if value > 1 else 0 for value in line) for line in diagram)

print(counter)
