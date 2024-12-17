from random import randint

limit = randint(0,10)
graph = {}

visited = []
stack = []

def dls_algorithm(visited,stack,start,limit):
    target = input('please enter your target!')
    stack.append(start)
    count = 0
    while stack and count <= limit:
        p = stack.pop()
        if p == target:
            visited.append(p)
            return visited
        else:
            visited.append(p)
            in_list = graph[p]
            for element in in_list[::-1]:
                stack.append(element)
            count += 1
    print(f'target is after the limit {limit}')
    return -1

count_nodes = int(input('please enter number of nodes.'))
start = input('enter start of graph.')
for j in range(count_nodes):
    parent = input('enter the parent!')
    children = list(input('enter children!'))
    graph[parent] = children


visit_list = dls_algorithm(visited,stack,start,limit)
if visit_list != -1:
    for i in visit_list:
        print(i,end=' ')
    print()
    print('limit:',limit)