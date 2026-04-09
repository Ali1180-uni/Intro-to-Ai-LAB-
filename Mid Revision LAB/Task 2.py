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

g = Graph()

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"]
for city in cities:
    g.addVertex(city)
g.addEdge("New York", "Los Angeles")
g.addEdge("New York", "Chicago")
g.addEdge("Los Angeles", "Houston")
g.addEdge("Chicago", "Phoenix")
g.addEdge("Houston", "Philadelphia")
g.addEdge("Phoenix", "Philadelphia")
g.printEdges()
G = nx.Graph(g.graph)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000)
plt.title("Graph of Cities")
plt.show()

# Question 2:
romania_graph = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti']
}

def bfs(graph, start, goal):
    visited = set()
    queue = [(start, [start])]
    while queue:
        vertex, path = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor == goal:
                    return path + [neighbor]
                else:
                    queue.append((neighbor, path + [neighbor]))
    return None

def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    visited.add(start)
    path.append(start)
    if start == goal:
        return path
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, visited, path)
            if result is not None:
                return result
    path.pop()
    return None

bfs_path = bfs(romania_graph, 'Sibiu', 'Bucharest')
dfs_path = dfs(romania_graph, 'Sibiu', 'Bucharest')
print("BFS Path from Sibiu to Bucharest:", bfs_path)
print("DFS Path from Sibiu to Bucharest:", dfs_path)


# Question 3:
import random
def minimax(pile, is_ai_turn):
    if pile == 0:
        return -1 if is_ai_turn else 1
    if is_ai_turn:
        best_score = float('-inf')
        for move in range(1, 4):
            if pile - move >= 0:
                score = minimax(pile - move, False)
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in range(1, 4):
            if pile - move >= 0:
                score = minimax(pile - move, True)
                best_score = min(score, best_score)
        return best_score
def ai_move(pile):
    best_score = float('-inf')
    best_move = 1
    for move in range(1, 4):
        if pile - move >= 0:
            score = minimax(pile - move, False)
            if score > best_score:
                best_score = score
                best_move = move
    return best_move

def play_nim():
    pile = 15
    print("Welcome to NIM! The AI will go first.")
    while pile > 0:
        move = ai_move(pile)
        pile -= move
        print(f"AI takes {move}. Counters left: {pile}")
        if pile == 0:
            print("AI wins!")
            break
        player_move = int(input("Enter the number of counters to take (1-3): "))
        while player_move not in [1, 2, 3] or player_move > pile:
            player_move = int(input("Invalid move. Enter a number between 1 and 3 that is less than or equal to the remaining counters: "))
        pile -= player_move
        print(f"You take {player_move}. Counters left: {pile}")
        if pile == 0:
            print("You win!")
            break
    replay = input("Do you want to play again? (yes/no): ")
    if replay.lower() == 'yes':
        play_nim()

play_nim()







# Question 4:
import time
from queue import PriorityQueue

def manhattan_distance(state, goal):
    distance = 0
    for i in range(1, 9):
        current_index = state.index(i)
        goal_index = goal.index(i)
        distance += abs(current_index // 3 - goal_index // 3) + abs(current_index % 3 - goal_index % 3)
    return distance

def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for move in moves:
        new_zero_index = zero_index + move[0] * 3 + move[1]
        if 0 <= new_zero_index < 9 and (zero_index // 3 == new_zero_index // 3 or zero_index % 3 == new_zero_index % 3):
            new_state = state[:]
            new_state[zero_index], new_state[new_zero_index] = new_state[new_zero_index], new_state[zero_index]
            neighbors.append(new_state)
    return neighbors

def a_star(start, goal):
    open_set = PriorityQueue()
    counter = 0
    open_set.put((manhattan_distance(start, goal), counter, start))
    came_from = {}
    g_score = {tuple(start): 0}
    nodes_explored = 0

    while not open_set.empty():
        current = open_set.get()[2]
        current_key = tuple(current)
        nodes_explored += 1

        if current == goal:
            path = []
            while current_key in came_from:
                path.append(list(current_key))
                current_key = came_from[current_key]
            path.append(start)
            return path[::-1], nodes_explored

        for neighbor in get_neighbors(current):
            neighbor_key = tuple(neighbor)
            tentative_g_score = g_score[current_key] + 1
            if neighbor_key not in g_score or tentative_g_score < g_score[neighbor_key]:
                came_from[neighbor_key] = current_key
                g_score[neighbor_key] = tentative_g_score
                f_score = tentative_g_score + manhattan_distance(neighbor, goal)
                counter += 1
                open_set.put((f_score, counter, neighbor))

    return None, nodes_explored

def bfs(start, goal):
    queue = [start]
    visited = {tuple(start)}
    came_from = {}
    nodes_explored = 0

    while queue:
        current = queue.pop(0)
        current_key = tuple(current)
        nodes_explored += 1

        if current == goal:
            path = []
            while current_key in came_from:
                path.append(list(current_key))
                current_key = came_from[current_key]
            path.append(start)
            return path[::-1], nodes_explored

        for neighbor in get_neighbors(current):
            neighbor_key = tuple(neighbor)
            if neighbor_key not in visited:
                came_from[neighbor_key] = current_key
                visited.add(neighbor_key)
                queue.append(neighbor)

    return None, nodes_explored


start_state = [2, 8, 1, 0, 4, 3, 7, 6, 5]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

start_time = time.time()
a_star_path, a_star_nodes = a_star(start_state, goal_state)
a_star_time = time.time() - start_time
print("A* Path:", a_star_path)
print("A* Nodes Explored:", a_star_nodes)
print("A* Time Taken:", a_star_time, "seconds")

start_time = time.time()
bfs_path, bfs_nodes = bfs(start_state, goal_state)
bfs_time = time.time() - start_time
print("BFS Path:", bfs_path)
print("BFS Nodes Explored:", bfs_nodes)
print("BFS Time Taken:", bfs_time, "seconds")