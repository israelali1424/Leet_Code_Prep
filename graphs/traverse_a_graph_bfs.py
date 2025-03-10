# breath first search in graph 
# this can onlt be done iterativly 
from collections import deque
def breathfirstPrint(graph,source):
    q= deque([source])
    while q:
        current = q.popleft()
        print(current)
        for neighbor in graph[current]:
            q.append(neighbor)
graph = {
    'a':['b','c'],
    'b': ['d'],
    'c':['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

breathfirstPrint(graph,'a')