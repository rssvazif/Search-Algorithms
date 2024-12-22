class Graph:
    def __init__(self):
        self.graph = {}
        self.h_n = {}

    def add_node(self,node,heuristic=0):
        self.graph[node] = []
        self.h_n[node] = heuristic

    def add_edge(self,start,end,weight):
        self.graph[start].append((end,weight))

    def display(self):
        print('Graph:')
        for key,value in self.graph.items():
            print(key,value)
        
        for key,value in self.h_n.items():
            print(key,value)
    
    def get_neighbors(self,node):
        return self.graph.get(node,[])
    
    def get_heuristic(self,node):
        return self.h_n.get(node,0)
    

def a_star_algorithm(graph,start,target):
    priority_queue = [(0 + graph.get_heuristic(start),0,start,[start])]
    visited = set()

    while priority_queue:
        priority_queue.sort(key=lambda x:x[0])

        f_n,g_n,current,path = priority_queue.pop(0)

        if current in visited:
            continue
        visited.add(current)

        if current == target :
            return g_n,path
        
        for neighbor , weight in graph.get_neighbors(current):
            if neighbor not in visited:
                g_new = g_n + weight
                f_new = g_new + graph.get_heuristic(neighbor)
                priority_queue.append((f_new,g_new,neighbor,path + [neighbor]))

    return None

object_A = Graph()
list_node = input('enter all nodes (separated with space!):').split()

for node in list_node:
    heuristic = int(input(f'enter heuristic value for {node} node:'))
    object_A.add_node(node,heuristic)

for start in list_node:
    while True:
        end, value = input(f'Enter end of an edge for {start} and value (or "-1 -1" to stop): ').split()
        if end != '-1' and value != '-1':
            object_A.add_edge(start, end, int(value))
        else:
            break 

object_A.display()

start_node = input('enter the start node:')
target_node = input('enter the target node:')

G_n,path = a_star_algorithm(object_A,start_node,target_node)
print(G_n,path)