class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self,node):

        self.graph[node] = []

    def add_edge(self,start,end,weight):

        self.graph[start].append((end,weight))

    def display(self):
        for key,value in self.graph.items():
            print(key,value)
    
    def get_neighbors(self,node):
        return self.graph.get(node,[])
    

    
def ucs_algorithm(graph,start,target):

    priority_queue = [(0,start,[start])]
    visited = set()
    
    while priority_queue:

        priority_queue.sort(key=lambda x:x[0])

        cost,current,path = priority_queue.pop(0)

        if current in visited:
            continue
        visited.add(current)
        if current == target:
            
            return cost ,path
        for neighbor , weight in graph.get_neighbors(current):
            if neighbor not in visited:
                priority_queue.append((cost + weight , neighbor,path + [neighbor]))

    return None

d_ob = Graph()
list_node = input('enter whole of nodes.').split()

for i in list_node:
    d_ob.add_node(i)

for start in list_node:
    while True:
        end,value = input(f'enter end of a edge for {start} and value(if not children enter -1 -1) .').split()
        if end != '-1' and value != '-1':
            d_ob.add_edge(start,end,int(value))
        else:
            break

d_ob.display()


queue = []
visited = []

start_node = input('enter the start node:')
target_node = input('enter the target node:')

cost,path = ucs_algorithm(d_ob,start_node,target_node)
print(f'answer is {path} with cost:{cost}')


