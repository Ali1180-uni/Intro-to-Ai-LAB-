from queue import Queue, PriorityQueue
from time import time

class Puzzle:
    Goal = [1,2,3,8,0,4,7,6,5]
    count = 0

    def __init__(self, state, parent, action, cost, use_h=False):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.use_h = use_h
        self.g = (parent.g + cost) if parent else 0
        self.h = self.manhattan() if use_h else 0
        self.f = self.g + self.h
        Puzzle.count += 1

    def is_goal(self):
        return self.state == Puzzle.Goal

# Sum of Manhattan distances of each tile
    def manhattan(self):
        total = 0
        for i, val in enumerate(self.state):
            if val == 0:
                continue
            goal_idx = Puzzle.Goal.index(val)
            total += abs(i // 3 - goal_idx // 3) + abs(i % 3 - goal_idx % 3)
        return total

#  Movement of the blank tile
    def children(self):
        blank = self.state.index(0)
        row, col = divmod(blank, 3)
        moves = {
            'U': blank - 3,
            'D': blank + 3,
            'L': blank - 1,
            'R': blank + 1
        }

        if row == 0:
            del moves['U']
        if row == 2:
            del moves['D']
        if col == 0:
            del moves['L']
        if col == 2:
            del moves['R']
        
        result = []
        for action, target in moves.items():
            s = self.state.copy()
            s[blank], s[target] = s[target], s[blank]
            result.append(Puzzle(s, self, action, 1, self.use_h))
        return result
    
    def solution(self):
        path = []
        node = self
        while node.parent:
            path.append(node.action)
            node = node.parent
        return list(reversed(path))
    
# BFS
def bfs(start):
    frontier = Queue()
    frontier.put(Puzzle(start, None, None, 0))
    explored = set()

    while not frontier.empty():
        node = frontier.get()
        if node.is_goal():
            return node.solution()
        explored.add(tuple(node.state))
        for child in node.children():
            if tuple(child.state) not in explored:
                frontier.put(child)

# A* Search

def a_star(start):
    frontier, explored, counter = PriorityQueue(), set(), 0
    frontier.put((0, counter, Puzzle(start, None, None, 0, use_h=True)))
    while not frontier.empty():
        _, _, node = frontier.get()
        if node.is_goal():
            return node.solution()
        explored.add(tuple(node.state))
        for child in node.children():
            if tuple(child.state) not in explored:
                counter += 1
                frontier.put((child.f, counter, child))


states = [
    [1,3,4,8,6,2,7,0,5],
    [2,8,1,0,4,3,7,6,5],
    [2,8,1,4,6,3,0,7,5],
]

for state in states:
    print("Start:", state)
    for name, fn, h in [("BFS", bfs, False), ("A*", a_star, True)]:
        Puzzle.count = 0
        t = time()
        sol = fn(state)
        print(f"{name} --> {sol} | nodes: {Puzzle.count} | time: {time()-t:4f}s")

    print()
