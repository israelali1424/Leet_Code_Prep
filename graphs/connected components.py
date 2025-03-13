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

# Test cases for connected_components_count function
try:
    # Test case 1: Basic example from the problem statement
    graph1 = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    }
    result1 = connected_components_count(graph1)
    expected1 = 2  # Two separate components
    print(f"Test case 1 (Basic example):")
    print(f"Result: {result1}, Expected: {expected1}")
    print(f"Test passed: {result1 == expected1}")
    
    # Test case 2: Empty graph
    graph2 = {}
    result2 = connected_components_count(graph2)
    expected2 = 0
    print(f"\nTest case 2 (Empty graph):")
    print(f"Result: {result2}, Expected: {expected2}")
    print(f"Test passed: {result2 == expected2}")
    
    # Test case 3: Second example from the problem statement
    graph3 = {
        1: [2],
        2: [1, 8],
        6: [7],
        9: [8],
        7: [6, 8],
        8: [9, 7, 2]
    }
    result3 = connected_components_count(graph3)
    expected3 = 1  # All nodes are connected in one component
    print(f"\nTest case 3 (Second example):")
    print(f"Result: {result3}, Expected: {expected3}")
    print(f"Test passed: {result3 == expected3}")
    
    # Test case 4: Graph with isolated nodes
    graph4 = {
        0: [],
        1: [],
        2: [3],
        3: [2],
        4: [],
        5: [6],
        6: [5]
    }
    result4 = connected_components_count(graph4)
    expected4 = 5  # Three isolated nodes and two components of size 2
    print(f"\nTest case 4 (Graph with isolated nodes):")
    print(f"Result: {result4}, Expected: {expected4}")
    print(f"Test passed: {result4 == expected4}")
    
    # Test case 5: Graph with multiple components of different sizes
    graph5 = {
        0: [1, 2],
        1: [0],
        2: [0],
        3: [4, 5],
        4: [3, 5],
        5: [3, 4],
        6: [7, 8],
        7: [6],
        8: [6],
        9: []
    }
    result5 = connected_components_count(graph5)
    expected5 = 4  # Three connected components and one isolated node
    print(f"\nTest case 5 (Multiple components of different sizes):")
    print(f"Result: {result5}, Expected: {expected5}")
    print(f"Test passed: {result5 == expected5}")
    
    # Test case 6: Fully connected graph
    graph6 = {
        0: [1, 2, 3, 4],
        1: [0, 2, 3, 4],
        2: [0, 1, 3, 4],
        3: [0, 1, 2, 4],
        4: [0, 1, 2, 3]
    }
    result6 = connected_components_count(graph6)
    expected6 = 1  # All nodes are in one component
    print(f"\nTest case 6 (Fully connected graph):")
    print(f"Result: {result6}, Expected: {expected6}")
    print(f"Test passed: {result6 == expected6}")

except Exception as e:
    print(f"Error running tests: {e}")