from collections import deque
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self):
        self.edges = {}
    
    def addVertex(self, vertex):
        self.edges[vertex] = deque()

    def addEdge(self, u, v):
        if v not in self.edges[u]:
            self.edges[u].append(v)
        if u not in self.edges[v]:
            self.edges[v].append(u)
    
    def printEdges(self):
        for vertex, neighbors in self.edges.items():
            print(f"{vertex}: {list(neighbors)}")


vertices = ["Seattle", "San Francisco", "Los Angeles", "Denver", 
            "Kansas City", "Chicago", "Boston", "New York", 
            "Atlanta", "Miami", "Dallas", "Houston"]

edges = [
    [0, 1], [0, 3], [0, 5],            # Seattle - San Francisco, Denver, Chicago
    [1, 2], [1, 3],                    # San Francisco - Los Angeles, Denver
    [2, 3], [2, 4], [2, 10],           # Los Angeles - Denver, Kansas City, Dallas
    [3, 4], [3, 5],                    # Denver - Kansas City, Chicago
    [4, 5], [4, 7], [4, 8], [4, 10],   # Kansas City - Chicago, New York, Atlanta, Dallas
    [5, 6], [5, 7],                    # Chicago - Boston, New York
    [6, 7],                            # Boston - New York
    [7, 8],                            # New York - Atlanta
    [8, 9], [8, 10], [8, 11],          # Atlanta - Miami, Dallas, Houston
    [9, 11],                           # Miami - Houston
    [10, 11]                           # Dallas - Houston
]

# graph = Graph()
# for vertex in vertices:
#     graph.addVertex(vertex)

# for edge in edges:
#     graph.addEdge(vertices[edge[0]], vertices[edge[1]])

# print("\nThe Edges are Here: ")
# graph.printEdges()


G = nx.Graph()
G.add_nodes_from(vertices)
nx_edges = [(vertices[u], vertices[v]) for u, v in edges]
G.add_edges_from(nx_edges)

nx.draw(G, with_labels=True, node_color='lightblue', node_size=1500, font_size=10)
plt.show()