with open('input13') as f:
    dots = [line.rstrip().split(",") for line in f if not line.startswith("fold") and line != "\n"]
    dots = [(int(dot[0]),int(dot[1])) for dot in dots]
with open('input13') as f:
    folds = [line.rstrip().replace("fold along ", "").split("=") for line in f if line.startswith("fold") and line != "\n"]
    folds = [[f[0], int(f[1])] for f in folds]

# Task 1

folded_dots = {
    (folds[0][1] - (dot[0] - folds[0][1]), dot[1])
    if dot[0] > folds[0][1]
    else dot
    for dot in dots
}

print(len(folded_dots))

# Task 2

for fold in folds:
    if fold[0] == 'x':
        dots = {
            (fold[1] - (dot[0] - fold[1]), dot[1])
            if dot[0] > fold[1]
            else dot
            for dot in dots
        }
    else:
        dots = {
            (dot[0], fold[1] - (dot[1] - fold[1]))
            if dot[1] > fold[1]
            else dot
            for dot in dots
        }

max_x = max(d[0] for d in dots)
max_y = max(d[1] for d in dots)

grid = [[' ']*(max_x+1) for i in range(max_y+1)]

for dot in dots:
    grid[dot[1]][dot[0]] = '#'

for line in grid:
    print(''.join(line))