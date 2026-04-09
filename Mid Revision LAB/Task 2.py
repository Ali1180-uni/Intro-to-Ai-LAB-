# Task Create a Graph class using Python dictionaries. Add at least 6 cities as vertices
# and connect them with edges. Implement addVertex(), addEdge(), and
# printEdges() methods. Finally, visualize the graph using networkx and matplotlib.
# Objective Test students' ability to implement a graph data structure from scratch and
# visualize it.
# Topics Graph class · Adjacency list · networkx · matplotlib

# Question 1:
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = {}

    def addVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def printEdges(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {', '.join(edges)}")

# Create a graph instance
g = Graph()
# Add vertices (cities)
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"]
for city in cities:
    g.addVertex(city)
# Add edges (connections between cities)
g.addEdge("New York", "Los Angeles")
g.addEdge("New York", "Chicago")
g.addEdge("Los Angeles", "Houston")
g.addEdge("Chicago", "Phoenix")
g.addEdge("Houston", "Philadelphia")
g.addEdge("Phoenix", "Philadelphia")
# Print edges
g.printEdges()
# Visualize the graph
G = nx.Graph(g.graph)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000)
plt.title("Graph of Cities")
plt.show()


