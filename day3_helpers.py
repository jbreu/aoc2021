def get_most_common_bit(lines, pos=-1):
    num_of_lines = len(lines)

    # transpose
    lines = list(map(list, zip(*lines)))

    lines = [sum(p) for p in lines]

    if pos == -1:
        return [1 if a >= num_of_lines / 2 else 0 for a in lines]

    if lines[pos] >= num_of_lines / 2:
        return 1
    else:
        return 0


def invert_binary_list(list):
    return [1 if e == 0 else 0 for e in list]


def binlisttoint(bin):
    num = 0
    for b in bin:
        num = 2 * num + b
    return num
