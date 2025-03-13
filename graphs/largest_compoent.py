
'''
Write a function, largest_component, that takes in the adjacency list of an undirected graph. 
The function should return the size of the largest connected component in the graph
largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 4

largest_component({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}) # -> 6
'''

def largest_component(graph):
  max_size = 0
  seen = set()  # Changed from dictionary to set
  
  def dfs(node):
    if node in seen:
      return 0
      
    seen.add(node)
    size = 1  # Count the current node
    
    # Explore all neighbors
    for neighbor in graph[node]:
      if neighbor not in seen:
        size += dfs(neighbor)
    
    return size
  
  # Iterate through all nodes in the graph
  for node in graph:
    if node not in seen:
      component_size = dfs(node)
      max_size = max(max_size, component_size)
  
  return max_size


# Test cases for largest_component function
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
    result1 = largest_component(graph1)
    expected1 = 4  # Nodes 0, 1, 5, 8 form a component
    print(f"Test case 1 (Basic example):")
    print(f"Result: {result1}, Expected: {expected1}")
    print(f"Test passed: {result1 == expected1}")
    
    # Test case 2: Empty graph
    graph2 = {}
    result2 = largest_component(graph2)
    expected2 = 0
    print(f"\nTest case 2 (Empty graph):")
    print(f"Result: {result2}, Expected: {expected2}")
    print(f"Test passed: {result2 == expected2}")
    
    # Test case 3: Graph with a single component
    graph3 = {
        1: [2, 3],
        2: [1, 4],
        3: [1, 4],
        4: [2, 3]
    }
    result3 = largest_component(graph3)
    expected3 = 4  # All nodes form a single component
    print(f"\nTest case 3 (Single component):")
    print(f"Result: {result3}, Expected: {expected3}")
    print(f"Test passed: {result3 == expected3}")
    
    # Test case 4: Graph with isolated nodes
    graph4 = {
        1: [],
        2: [],
        3: [4],
        4: [3],
        5: []
    }
    result4 = largest_component(graph4)
    expected4 = 2  # Nodes 3 and 4 form the largest component
    print(f"\nTest case 4 (Graph with isolated nodes):")
    print(f"Result: {result4}, Expected: {expected4}")
    print(f"Test passed: {result4 == expected4}")
    
    # Test case 5: Graph with multiple equal-sized components
    graph5 = {
        1: [2],
        2: [1],
        3: [4],
        4: [3],
        5: [6],
        6: [5],
        7: []
    }
    result5 = largest_component(graph5)
    expected5 = 2  # Multiple components of size 2
    print(f"\nTest case 5 (Multiple equal-sized components):")
    print(f"Result: {result5}, Expected: {expected5}")
    print(f"Test passed: {result5 == expected5}")
    
    # Test case 6: Large connected component
    graph6 = {
        0: [1, 2, 3],
        1: [0, 2],
        2: [0, 1, 3],
        3: [0, 2, 4],
        4: [3, 5, 6],
        5: [4, 6],
        6: [4, 5],
        7: [8],
        8: [7]
    }
    result6 = largest_component(graph6)
    expected6 = 7  # Nodes 0-
except Exception as e:
    print(f"Test failed with error: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
    
'''
the input is anadjacency list
bfs or dfs coulb be used
i will use dfs for this one 
you need a counter and seen list 

plan
set max_counter to zero
create the set for seen 
first you need to loop through the aj list it self 
def should be a help function ( graph,max_counter)
current = graph[node]
for neigbor in graph[current]:
if neibor not in seen:
counter +=1
seen.add 
elsr: 
    counter = 0 
 break
imax_counter = max(max_counter, current_counter)
call dfs 

return max_counter
'''
# my broken version I had the right idea but did not know how to implement 
def largest_component_broke(graph):
  max_counter = 0
  seen = {}
  def dfs(graph,node,max_counter):
      print(node)
      current_counter = 0
     
      print(f' current_node {current_node}')
      for neighbor in graph[node]:
        if neighbor not in seen:
          current_counter+=1 
          seen.add(neighbor)
        else: 
          max_counter = max(max_counter,current_counter)
          current_node =0
        return max_counter
          
        dfs(graph,node,max_counter)
        
        for node in graph:
            dfs(graph,node,max_counter)
        return max_counter
  

  

  
   
      
        
  pass # todo





# Test with the example
test_graph = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}
print(largest_component(test_graph))  # Should output 4