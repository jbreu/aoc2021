import statistics

with open('input10') as f:
    chunks = [line.rstrip() for line in f]


def check(chunk):
      
    open_brackets = ['(', '[', '{', '<']
    close_brackets = [')', ']', '}', '>']
    map = dict(zip(open_brackets, close_brackets))
    queue = []
  
    for i in chunk:
        if i in open_brackets:
            queue.append(map[i])
        elif i in close_brackets:
            if not queue or i != queue.pop():
                return i

    score = 0

    while len(queue)>0:
        score *= 5

        char = queue.pop()

        if char == ')':
            score+=1
        if char == ']':
            score+=2
        if char == '}':
            score+=3
        if char == '>':
            score+=4

    scores.append(score)
    
   
illegal = 0
scores = []

for chunk in chunks:
    result = check(chunk)

    if result == ')':
        illegal+=3
    elif result == '>':
        illegal+=25137
    elif result == ']':
        illegal+=57
    elif result == '}':
        illegal+=1197
print(illegal)

print(statistics.median(scores))