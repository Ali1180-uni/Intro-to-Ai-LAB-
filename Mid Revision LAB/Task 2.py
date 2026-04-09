# Task Create a Graph class using Python dictionaries. Add at least 6 cities as vertices
# and connect them with edges. Implement addVertex(), addEdge(), and
# printEdges() methods. Finally, visualize the graph using networkx and matplotlib.
# Objective Test students' ability to implement a graph data structure from scratch and
# visualize it.
# Topics Graph class · Adjacency list · networkx · matplotlib

# Question 1:
# import networkx as nx
# import matplotlib.pyplot as plt

# class Graph:
#     def __init__(self):
#         self.graph = {}

#     def addVertex(self, vertex):
#         if vertex not in self.graph:
#             self.graph[vertex] = []

#     def addEdge(self, vertex1, vertex2):
#         if vertex1 in self.graph and vertex2 in self.graph:
#             self.graph[vertex1].append(vertex2)
#             self.graph[vertex2].append(vertex1)

#     def printEdges(self):
#         for vertex, edges in self.graph.items():
#             print(f"{vertex}: {', '.join(edges)}")

# # Create a graph instance
# g = Graph()
# # Add vertices (cities)
# cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"]
# for city in cities:
#     g.addVertex(city)
# # Add edges (connections between cities)
# g.addEdge("New York", "Los Angeles")
# g.addEdge("New York", "Chicago")
# g.addEdge("Los Angeles", "Houston")
# g.addEdge("Chicago", "Phoenix")
# g.addEdge("Houston", "Philadelphia")
# g.addEdge("Phoenix", "Philadelphia")
# # Print edges
# g.printEdges()
# # Visualize the graph
# G = nx.Graph(g.graph)
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000)
# plt.title("Graph of Cities")
# plt.show()


#  Implement BFS and DFS on the Romania map and
# compare their paths Lab 5 Graphs
# Task Using the Romania dictionary graph from the lab, implement both Breadth-First
# Search (BFS) and Depth-First Search (DFS). Run both from Sibiu to Bucharest.
# Print the path found by each algorithm and explain the difference in results.
# Objective Verify students understand how BFS and DFS traverse graphs differently and can
# interpret the output.
# Topics BFS · DFS · Dictionary graph · Path finding

# Question 2:
# Romania graph as an adjacency list
# romania_graph = {
#     'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
#     'Zerind': ['Arad', 'Oradea'],
#     'Oradea': ['Zerind', 'Sibiu'],
#     'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
#     'Fagaras': ['Sibiu', 'Bucharest'],
#     'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
#     'Timisoara': ['Arad', 'Lugoj'],
#     'Lugoj': ['Timisoara', 'Mehadia'],
#     'Mehadia': ['Lugoj', 'Drobeta'],
#     'Drobeta': ['Mehadia', 'Craiova'],
#     'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
#     'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
#     'Bucharest': ['Fagaras', 'Pitesti']
# }

# def bfs(graph, start, goal):
#     visited = set()
#     queue = [(start, [start])]
#     while queue:
#         vertex, path = queue.pop(0)
#         if vertex not in visited:
#             visited.add(vertex)
#             for neighbor in graph[vertex]:
#                 if neighbor == goal:
#                     return path + [neighbor]
#                 else:
#                     queue.append((neighbor, path + [neighbor]))
#     return None

# def dfs(graph, start, goal, visited=None, path=None):
#     if visited is None:
#         visited = set()
#     if path is None:
#         path = []
#     visited.add(start)
#     path.append(start)
#     if start == goal:
#         return path
#     for neighbor in graph[start]:
#         if neighbor not in visited:
#             result = dfs(graph, neighbor, goal, visited, path)
#             if result is not None:
#                 return result
#     path.pop()
#     return None

# # Run BFS and DFS from Sibiu to Bucharest
# bfs_path = bfs(romania_graph, 'Sibiu', 'Bucharest')
# dfs_path = dfs(romania_graph, 'Sibiu', 'Bucharest')
# print("BFS Path from Sibiu to Bucharest:", bfs_path)
# print("DFS Path from Sibiu to Bucharest:", dfs_path)

#  Modify the NIM game so the AI always starts first and
# plays optimally Lab 6 Minimax
# Task Adapt the NIM game so the AI makes the first move. Use the minimax() function
# to ensure optimal AI strategy. Test with a pile of 15 counters. Print each game
# state and declare the winner at the end. Add a replay option after the game ends.
# Objective Ensure students understand the minimax algorithm and can restructure game
# logic independently.
# Topics Minimax · NIM game · Game tree · AI strategy

# Question 3:
# import random
# def minimax(pile, is_ai_turn):
#     if pile == 0:
#         return -1 if is_ai_turn else 1
#     if is_ai_turn:
#         best_score = float('-inf')
#         for move in range(1, 4):
#             if pile - move >= 0:
#                 score = minimax(pile - move, False)
#                 best_score = max(score, best_score)
#         return best_score
#     else:
#         best_score = float('inf')
#         for move in range(1, 4):
#             if pile - move >= 0:
#                 score = minimax(pile - move, True)
#                 best_score = min(score, best_score)
#         return best_score
# def ai_move(pile):
#     best_score = float('-inf')
#     best_move = 1
#     for move in range(1, 4):
#         if pile - move >= 0:
#             score = minimax(pile - move, False)
#             if score > best_score:
#                 best_score = score
#                 best_move = move
#     return best_move

# def play_nim():
#     pile = 15
#     print("Welcome to NIM! The AI will go first.")
#     while pile > 0:
#         move = ai_move(pile)
#         pile -= move
#         print(f"AI takes {move}. Counters left: {pile}")
#         if pile == 0:
#             print("AI wins!")
#             break
#         player_move = int(input("Enter the number of counters to take (1-3): "))
#         while player_move not in [1, 2, 3] or player_move > pile:
#             player_move = int(input("Invalid move. Enter a number between 1 and 3 that is less than or equal to the remaining counters: "))
#         pile -= player_move
#         print(f"You take {player_move}. Counters left: {pile}")
#         if pile == 0:
#             print("You win!")
#             break
#     replay = input("Do you want to play again? (yes/no): ")
#     if replay.lower() == 'yes':
#         play_nim()

# play_nim()


# Solve a given 8-puzzle using A* and measure the
# Manhattan heuristic's impact
# Lab 7 A*
# Search
# Task Given the starting state [2, 8, 1, 0, 4, 3, 7, 6, 5], solve the 8-puzzle using astar().
# Print the sequence of moves, total nodes explored, and time taken. Then solve
# the same puzzle using BFS and compare: which explored more nodes? Why does
# the Manhattan heuristic help A*?
# Objective Students demonstrate they can run and compare A* vs BFS, and explain the role
# of the heuristic.
# Topics A* search · Manhattan distance · Heuristic · BFS vs A*

# Question 4:
