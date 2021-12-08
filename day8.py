
class Line:
    def __init__(self, string) -> None:
        self.pattern = [list(foo) for foo in string.split(" | ")[0].split(" ")]
        self.value = [list(foo) for foo in string.rstrip().split(" | ")[1].split(" ")]


with open('input8') as f:
    lines = [Line(line) for line in f]

# Task 1

print(sum(sum(len(pat) in [2, 3, 4, 7] for pat in line.value) for line in lines))

# Task 2

result = 0
for line in lines:
    line.pattern.sort(key=len)
    line.pattern = [set(p) for p in line.pattern]

    OBEN = line.pattern[1] - line.pattern[0]

    siebenvier = line.pattern[1].copy()
    siebenvier.update(line.pattern[2])

    fuenfer = [pat-siebenvier for pat in line.pattern if len(pat) == 5]
    fuenfer.sort(key=len)

    LINKS_UNTEN = fuenfer[2]-fuenfer[0]

    UNTEN = fuenfer[2] - LINKS_UNTEN

    fuenfer = [pat for pat in line.pattern if len(pat) == 5 and line.pattern[0].issubset(pat)]

    MITTE = fuenfer[0] - OBEN - UNTEN - line.pattern[0]

    LINKS_OBEN = line.pattern[2] - MITTE - line.pattern[0]

    sixer = [pat for pat in line.pattern if len(pat) == 6 and not line.pattern[0].issubset(pat)]

    RECHTS_OBEN = line.pattern[0]-sixer[0]

    RECHTS_UNTEN = line.pattern[0]-RECHTS_OBEN

    factor=1000
    num=0
    for digit in line.value:
        if OBEN | UNTEN | MITTE | LINKS_OBEN | LINKS_UNTEN | RECHTS_OBEN | RECHTS_UNTEN == set(digit):
            num+=factor*8
        if OBEN | UNTEN | MITTE | LINKS_OBEN | RECHTS_OBEN | RECHTS_UNTEN == set(digit):
            num+=factor*9
        if OBEN | UNTEN | LINKS_OBEN | LINKS_UNTEN | RECHTS_OBEN | RECHTS_UNTEN == set(digit):
            num+=factor*0
        if RECHTS_OBEN | RECHTS_UNTEN == set(digit):
            num+=factor*1
        if RECHTS_OBEN | LINKS_UNTEN | OBEN | MITTE | UNTEN == set(digit):
            num+=factor*2
        if RECHTS_OBEN | RECHTS_UNTEN | OBEN | MITTE | UNTEN == set(digit):
            num+=factor*3
        if RECHTS_OBEN | RECHTS_UNTEN | MITTE | LINKS_OBEN == set(digit):
            num+=factor*4
        if LINKS_OBEN | RECHTS_UNTEN | OBEN | MITTE | UNTEN == set(digit):
            num+=factor*5
        if LINKS_OBEN | RECHTS_UNTEN | OBEN | MITTE | UNTEN | LINKS_UNTEN == set(digit):
            num+=factor*6
        if RECHTS_OBEN | OBEN | RECHTS_UNTEN == set(digit):
            num+=factor*7

        factor //= 10

    result += num

print(result)