graph = {}

visited = []
stack = []


def ids_algorithm(visited,stack,start):

    target = input('please enter your target!')
    limit = 0

    while True :
        visited = []
        stack = [start]
        count = 0

        while stack :
            p = stack.pop()
            if p not in visited:
                visited.append(p)
                count += 1
                if p == target :
                    print('Deepth:',count - 1)
                    return visited
                if count <= limit :
                    in_list = graph[p]
                    for element in in_list[::-1]:
                        stack.append(element)
        limit += 1

number_nodes = int(input('please enter number of nodes .'))
start = input('enter the start node!')
for j in range(number_nodes):
    parent = input('enter the parent!')
    children = input('enter children!').split()
    graph[parent] = children

ids_list = ids_algorithm(visited,stack,start)
for i in ids_list:
    print(i,end=" ")