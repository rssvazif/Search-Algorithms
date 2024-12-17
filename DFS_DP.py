
graph = {}

stack = []
visited = []


def dfs_algorithms(visited,stack,start):
    target = input('please enter your target.')
    stack.append(start)
    
    while stack:
        p = stack.pop()
        if p == target:
            visited.append(p)
            return visited
        else:
            visited.append(p)
            in_list = graph[p]
            for element in in_list[::-1]:
                stack.append(element)
count_nodes = int(input('please enter number of nodes.'))
start = input('enter start of graph!')
for j in range(count_nodes):
    parent = input('enter the parent!')
    children = list(input('enter children!'))
    graph[parent] = children
    
visit_list = dfs_algorithms(visited,stack,start)
for i in visit_list:
    print(i,end=' ')