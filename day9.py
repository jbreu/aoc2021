with open('input9') as f:
    heightmap = [list(line.rstrip()) for line in f]
    heightmap = [[int(entry) for entry in line] for line in heightmap]
    x_len = len(heightmap[0])
    y_len = len(heightmap)

# wrap heightmap with "10"s

heightmap.insert(0, [10]*x_len)
heightmap.insert(y_len+1, [10]*x_len)

for line in heightmap:
    line.insert(0, 10)
    line.append(10)

minima = []
basins = []

covermap = [[0] * (len(heightmap)+2) for i in range(len(heightmap)+2)]


class Basin:
    def __init__(self) -> None:
        self.size = 0


def step(basin, x, y):
    if covermap[y][x] != 0:
        return

    basin.size+= 1
    covermap[y][x] = 1

    if heightmap[y][x-1] < 9:
        step(basin, x-1, y)

    if heightmap[y][x+1] < 9:
        step(basin, x+1, y)

    if heightmap[y-1][x] < 9:
        step(basin, x, y-1)

    if heightmap[y+1][x] < 9:
        step(basin, x, y+1)

for y in range(1,y_len+1):
    for x in range(1,x_len+1):
        current = heightmap[y][x]

        if current < heightmap[y][x-1] and current < heightmap[y][x+1] and current < heightmap[y+1][x] and current < heightmap[y-1][x]:
            minima.append(current+1)
            basin = Basin()
            step(basin, x, y)
            basins.append(basin)

# Task 1

print(sum(minima))

# Task 2

basins.sort(key=lambda x: x.size, reverse=True)

print(basins[0].size * basins[1].size * basins[2].size)