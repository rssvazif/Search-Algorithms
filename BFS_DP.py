
graph = {}

visited = []
queue = []


def bfs_algorithm(visited,queue,start):
    target = input('please enter your target!!')
    queue.append(start)
    while queue:
        p = queue.pop(0)
        if p == target:
            visited.append(p)
            return visited
        else:
            visited.append(p)
            for element in graph[p]:
                queue.append(element)

count_node = int(input('please enter nodes of your graph!'))
start = input('please enter start node.')
for j in range(count_node):
    parent = input('enter the parent!')
    children = list(input('enter children!'))
    graph[parent] = children

solution = bfs_algorithm(visited,queue,start)
for i in solution:
    print(i,end=" ")