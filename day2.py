# Third task

with open('input2') as f:
    lines2 = [line.rstrip() for line in f]

forward = sum(int(a.split()[1]) for a in lines2 if "forward" in a)
up = sum(int(a.split()[1]) for a in lines2 if "up" in a)
down = sum(int(a.split()[1]) for a in lines2 if "down" in a)
print(forward * (down - up))

# Fourth task

aim = 0
x = 0
depth = 0

for entry in lines2:
    value = int(entry.split()[1])
    if "down" in entry:
        aim += value
    if "up" in entry:
        aim -= value
    if "forward" in entry:
        x += value
        depth += value * aim

print(depth * x)