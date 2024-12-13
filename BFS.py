graph = {'5':['3','7'],
         '3':['2','4'],
         '7':['8'],
         '2':[],
         '4':['8'],
         '8':[]
         }

visited = []
queue = []

def bfs_algorithm(visited,queue,node):
    visited.append(node)
    queue.append(node)

    while queue:

        element = queue.pop(0)
        print(f'{element}',end=' ')

        for nei in graph[element]:
            if nei not in visited:
                visited.append(nei)
                queue.append(nei)

bfs_algorithm(visited,queue,'5')