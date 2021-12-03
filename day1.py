with open('input') as f:
    lines = [int(line.rstrip()) for line in f]

# First task

increases_count = sum(b > a for a, b in zip(lines, lines[1:]))

print(increases_count)

# Second task

sum_3 = [a + b + c for a, b, c in zip(lines, lines[1:], lines[2:])]
increases_count_window3 = sum(b > a for a, b in zip(sum_3, sum_3[1:]))

print(increases_count_window3)