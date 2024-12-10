class Graph():
    def __init__(self):
        self.graph = {}
    def add_node(self,node):
        if node not in self.graph:
            self.graph[node] = []
    def add_edge(self,node1,node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)
    def __str__(self):
        return str(self.graph)

def create_graph():
    g = Graph()

    nodes = input("Enter the nodes").split()
    for node in nodes:
        g.add_node(node)

    edges_
