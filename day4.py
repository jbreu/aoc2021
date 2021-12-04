import sys

with open('input4') as f:
    first = True
    tables = []
    current_table = []
    draws = []
    for line in f:
        if first:
            draws = [int(value) for value in line.rstrip().split(',')]
            first = False
            continue

        if line.rstrip() == '':
            tables.append(current_table)
            current_table = []
        else:
            current_table.append([int(value) for value in line.rstrip().split()])

    tables.append(current_table)
    tables.pop(0)

for draw in draws:
    for i, table in enumerate(tables):
        table = [[0 if cell == draw else cell for cell in row] for row in table]
        tables[i] = table

        summed_rows = [sum(row) for row in table]

        #transpose
        table = list(map(list, zip(*table)))
        summed_columns = [sum(row) for row in table]

        if any(row == 0 for row in summed_rows) or any(column == 0 for column in summed_columns):
            print(sum(summed_rows) * draw)
            sys.exit()
