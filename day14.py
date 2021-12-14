import string

with open('input14') as f:
    template = f.readline().rstrip()
with open('input14') as f:
    pairs = [line.rstrip().split(" -> ") for line in f if "->" in line]
    pairs = {pair[0]: pair[1] for pair in pairs}

# Task 1

polymer = template

for step in range(10):
    for pos in range(len(polymer)-2, -1, -1):       
        left = ''.join([polymer[pos], polymer[pos+1]])
        if left in pairs:
            polymer = ''.join([polymer[:pos+1], pairs[left], polymer[pos+1:]])


counts = [polymer.count(character) for character in string.ascii_uppercase if polymer.count(character) > 0]
counts.sort()
print(counts[-1] - counts[0])


#Task 2

counts = {character:0 for character in pairs.values()}
steps = 40

def stack(left, right, depth):
    lr = ''.join([left, right])
    if lr in pairs and depth<steps:
        counts[pairs[lr]] += 1
        stack(left, pairs[lr], depth+1)
        stack(pairs[lr], right, depth+1)
    #if depth==steps:
    #    print(str(depth) + ": " + str(counts))


for i in range(len(template)-1):
    counts[template[i]] += 1
    print(i)
    stack(template[i], template[i+1], 0)
    
    
counts[template[-1]] += 1

counts = dict(sorted(counts.items(), key=lambda item: item[1]))
counts = list(counts.values())

print(counts[-1]-counts[0])