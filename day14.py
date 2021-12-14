import string

with open('input14') as f:
    template = f.readline().rstrip()
with open('input14') as f:
    pairs = [line.rstrip().split(" -> ") for line in f if "->" in line]
    pairs = {pair[0]: pair[1] for pair in pairs}

#print(pairs)
#print(template)

for step in range(40):
    print(step)
    for pos in range(len(template)-2, -1, -1):       
        left = ''.join([template[pos], template[pos+1]])
        if left in pairs:
            template = ''.join([template[:pos+1], pairs[left], template[pos+1:]])


counts = [template.count(character) for character in string.ascii_uppercase if template.count(character) > 0]
counts.sort()

print(counts[-1] - counts[0])
