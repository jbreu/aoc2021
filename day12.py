with open('input12') as f:
    connections = [line.rstrip().split("-") for line in f]

graph = dict()

for connection in connections:
    if connection[0] not in graph:
        graph[connection[0]] = []

    graph[connection[0]].append(connection[1])

    if connection[1] not in graph:
        graph[connection[1]] = []

    graph[connection[1]].append(connection[0])

count = 0


def traverse(route, small_twice):
    for next in graph[route[-1]]:
        small_twice_local = small_twice
        if next == 'end':
            route.append('end')
            global count
            count += 1
            # print(','.join(route))
            continue

        # Task 1

        # if next.islower() and next in route:
        #    continue

        # End Task 1

        # Task 2

        if next in ['start', 'end']:
            continue

        if next.islower() and next in route and small_twice_local:
            continue

        if next.islower() and next in route:
            small_twice_local = True

        # End Task 2

        new_route = [r for r in route]
        new_route.append(next)
        traverse(new_route, small_twice_local)


traverse(['start'], False)

print(count)
