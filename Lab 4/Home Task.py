import matplotlib.pyplot as plt
import networkx as nx

# US Cities Graph (from the image)
# 0: Seattle, 1: San Francisco, 2: Los Angeles, 3: Denver, 4: Kansas City
# 5: Chicago, 6: Boston, 7: New York, 8: Atlanta, 9: Miami, 10: Dallas, 11: Houston

graph = {
    'Seattle': ['San Francisco', 'Denver', 'Chicago'],
    'San Francisco': ['Seattle', 'Los Angeles', 'Denver'],
    'Los Angeles': ['San Francisco', 'Denver', 'Kansas City', 'Dallas'],
    'Denver': ['Seattle', 'San Francisco', 'Los Angeles', 'Kansas City', 'Chicago'],
    'Kansas City': ['Los Angeles', 'Denver', 'Chicago', 'New York', 'Atlanta', 'Dallas'],
    'Chicago': ['Seattle', 'Denver', 'Kansas City', 'Boston', 'New York'],
    'Boston': ['Chicago', 'New York'],
    'New York': ['Kansas City', 'Chicago', 'Boston', 'Atlanta'],
    'Atlanta': ['Kansas City', 'New York', 'Miami', 'Dallas', 'Houston'],
    'Miami': ['Atlanta', 'Houston'],
    'Dallas': ['Los Angeles', 'Kansas City', 'Atlanta', 'Houston'],
    'Houston': ['Atlanta', 'Miami', 'Dallas']
}


# BFS
def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited


# DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


print("BFS Traversal:", bfs(graph, 'Seattle'))
print("DFS Traversal:", dfs(graph, 'Seattle'))


# Visualization
G = nx.Graph(graph)
nx.draw(G, with_labels=True, node_color="lightgreen", node_size=2000, font_size=8)
plt.show()
