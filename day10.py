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
   
illegal = 0

for chunk in chunks:
    result = check(chunk)

    if result == ')':
        illegal+=3
    if result == ']':
        illegal+=57
    if result == '}':
        illegal+=1197
    if result == '>':
        illegal+=25137

print(illegal)