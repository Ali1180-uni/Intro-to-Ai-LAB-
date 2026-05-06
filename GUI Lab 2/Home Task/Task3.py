from collections import deque
import os

import pandas as pd

# Read the text file using pandas
words_path = os.path.join(os.path.dirname(__file__), "words.txt")
df = pd.read_csv(words_path, header=None, names=["word"])

# Convert the column to a Python list or set
words = df['word'].tolist()
WORDS = set(words)

def neighboring_words(word):
    neighbors = {word[:i] + c + word[i+1:]
                 for i in range(len(word))
                 for c in 'abcdefghijklmnopqrstuvwxyz'
                 if c != word[i]}
    return neighbors & WORDS

word_neighbors = {word: neighboring_words(word)
                   for word in WORDS}

# from pprint import pprint
# pprint(word_neighbors)


def breadth_first(start, goal, neighbors):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current_word, path = queue.popleft()

        if current_word == goal:
            return path

        if current_word not in visited:
            visited.add(current_word)
            for neighbor in neighbors.get(current_word, set()):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None


path = breadth_first("cat", "dog", word_neighbors)
print("Path:", path)