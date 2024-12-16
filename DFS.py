graph = {
    'A':['B','C','D'],
    'B':['E','F'],
    'C':['I','J'],
    'D':[],
    'E':['G','H'],
    'F':[],
    'I':[],
    'J':[],
    'G':[],
    'H':[]
}

stack = []
visited = []
start = 'A'

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

visit_list = dfs_algorithms(visited,stack,start)
for i in visit_list:
    print(i,end=' ')