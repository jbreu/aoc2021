from collections import deque


with open('input11') as f:
    octopuses = [list(line.rstrip()) for line in f]
    octopuses = [[int(entry) for entry in line] for line in octopuses]


def print2dlist(lists):
    for line in lists:
        print(','.join(map(str, line)))


def step(x, y):
        
    if covermap[y][x] != 0:
        return

    covermap[y][x] = 1

    octopuses[y][x] += 1

    if octopuses[y][x] < 10:
        return

    if octopuses[y][x] == 10:
        flashing.append([x, y])
        return

    deltas = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]

    for delta in deltas:
        if (
            x + delta[0] >= 0
            and y + delta[1] >= 0
            and x + delta[0] < len(octopuses)
            and y + delta[1] < len(octopuses)
            and octopuses[y + delta[1]][x + delta[0]] < 10
        ):
            step(x+delta[0], y+delta[1])


sum_flashes = 0

for steps in range(100000):
    flashing = deque()

    for line in range(len(octopuses)):
        for cell in range(len(octopuses[0])):
            octopuses[line][cell] += 1
            if octopuses[line][cell] > 9:
                flashing.append([cell, line])

    covermap = []

    while len(flashing)>0:

        covermap = [[0] * len(octopuses) for _ in range(len(octopuses))]

        flash = flashing.popleft()
        step(flash[0], flash[1])

    sum_flashes += sum(sum(cell > 9 for cell in line) for line in octopuses)

    if all(all(cell > 9 for cell in line) for line in octopuses):
        # Task 2
        print(steps+1)
        break

    octopuses = [[0 if cell > 9 else cell for cell in line] for line in octopuses]

# Task 1
print(sum_flashes)