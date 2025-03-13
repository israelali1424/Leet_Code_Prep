'''

add to favoritessettings
shortest path
Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return the length of the shortest path between A and B. Consider the length as the number of edges in the path, not the number of nodes. If there is no path between A and B, then return -1. You can assume that A and B exist as nodes in the graph.
'''

from collections import deque
import math
def shortest_path(edges, node_A, node_B):
  visited = set()
  graph = build_graph(edges)
  return find_path(graph,node_A,node_B,visited)
  pass # todo

def find_path(graph,node_A,node_B,visited):
  # in the queue you want to pop left 
  # then loop through the neighbors in that node 
  # if a neighbor == node_B return the distance
  # else keep looping 
  # handle nodes already seen 
  # have a distance counter 
  q = deque([(node_A,0)])
  while q: 
    [node, distance] = q.popleft()
    if node == node_B:
        return distance
    # Check all neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            q.append((neighbor, distance + 1))
  return -1

  
def build_graph(edges):
  graph = {}
  for [a,b] in edges:
    if a not in  graph:
      graph[a]= []

    if b not in  graph:
      graph[b]= []
      
    graph[a].append(b)
    graph[b].append(a)
  return graph
  
  
if __name__ == "__main__":
    edges1 = [
        ['w', 'x'],
        ['x', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'v']
    ]
    result1 = shortest_path(edges1, 'w', 'z')
    print("Test Case 1:", result1, "Passed" if result1 == 2 else "Failed")
    assert result1 == 2
    # Expected Output: 2
    
    edges2 = [
        ['w', 'x'],
        ['x', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'v']
    ]
    result2 = shortest_path(edges2, 'w', 'w')
    print("Test Case 2:", result2, "Passed" if result2 == 0 else "Failed")
    assert result2 == 0
    # Expected Output: 0
    
    edges3 = [
        ['a', 'b'],
        ['b', 'c'],
        ['c', 'd'],
        ['d', 'e']
    ]
    result3 = shortest_path(edges3, 'a', 'e')
    print("Test Case 3:", result3, "Passed" if result3 == 4 else "Failed")
    assert result3 == 4
    # Expected Output: 4
    
    edges4 = [
        ['a', 'b'],
        ['c', 'd'],
        ['e', 'f']
    ]
    result4 = shortest_path(edges4, 'a', 'f')
    print("Test Case 4:", result4, "Passed" if result4 == -1 else "Failed")
    assert result4 == -1
    # Expected Output: -1
    
    edges5 = [
        ['a', 'b'],
        ['a', 'c'],
        ['b', 'd'],
        ['c', 'd']
    ]
    result5 = shortest_path(edges5, 'a', 'd')
    print("Test Case 5:", result5, "Passed" if result5 == 2 else "Failed")
    assert result5 == 2
    # Expected Output: 2