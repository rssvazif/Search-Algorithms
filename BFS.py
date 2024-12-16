graph = {'A':['B','C','D'],
         'B':['E'],
         'C':['F','G'],
         'D':[],
         'E':[],
         'F':[],
         'G':[]
         }

visited = []
queue = []
start = 'A'

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



solution = bfs_algorithm(visited,queue,start)
for i in solution:
    print(i,end=" ")