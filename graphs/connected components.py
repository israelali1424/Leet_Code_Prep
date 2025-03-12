'''
Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. The function should return the number of connected components within the graph.
connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 2

  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
'''
from collections import deque 
def connected_components_count(graph):
  count = 0
  seen = set()
  if not graph:
      return count 
  current  = None 
  for key, value in graph.items():
      current  = key
      break
  if current:
    q = deque([current])
    while q:
        current = q.popleft()
        for neigbor in graph.keys():
            print(neigbor)
            if neigbor in seen:
                count+=1
                continue
            else:
                seen.add(neigbor) 
            q.append(neigbor)

  return count              
          
'''
3/112/25
The main issues with your original code were: From cLaude

You weren't starting a new BFS for each unvisited component, which is necessary to count all components
You were iterating through all graph keys as neighbors rather than using the actual neighbors from the adjacency list
Your visited tracking and component counting logic had issues - you were incrementing count when seeing already visited nodes
You were only exploring from a single starting node

The corrected algorithm:

Iterates through all nodes in the graph
For each unvisited node, increments the component count and performs a BFS
During BFS, marks all reachable nodes as visited
Returns the final count of components

This ensures that we count each separate connected component exactly once.
'''
  


print(connected_components_count({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}) )# -> 3

from collections import deque

def connected_components_count(graph):
    count = 0
    visited = set()
    
    for node in graph:
        if node not in visited:
            count += 1
            # Perform BFS to mark all nodes in this component as visited
            queue = deque([node])
            visited.add(node)
            
            while queue:
                current = queue.popleft()
                neighbors = graph[current]
                
                for neighbor in neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
    
    return count


def connected_components_count_dfs(graph):
    visited = set()
    count = 0
    
    def dfs(node):
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    
    for node in graph:
        if node not in visited:
            count += 1
            dfs(node)
    
    return count