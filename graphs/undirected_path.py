'''
undirected path
Write a function, undirectedPath, that takes in an array of edges for an undirected graph and 
two nodes (nodeA, nodeB). The function should return a boolean indicating whether or not there 
exists a path between nodeA and nodeB.

# Graph Representation:
#     i - j
#     |
#     k - l
#     |
#     m
#
#     o - n
'''
# The graph 
edges = [
  ['i', 'j'],
  ['k', 'i'],
  ['m', 'k'],
  ['k', 'l'],
  ['o', 'n']
]

def create_undirected_graph(edges):
    graph = {}
    for a,b, in edges:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

print(create_undirected_graph(edges))
    
def undirected_path(edges, node_A, node_B):
    seen = set()
    graph = create_undirected_graph(edges)
    if current == node_B:
        return True
    for neighbor in graph[current]:
        if neighbor not in seen:
            seen.add(neighbor)
        if neighbor in seen:
            return False
        if neighbor == node_B:
            return True
        if undirected_path(edges,neighbor,node_B) == True:
            return True
    return False 


## broke apporah ^^^

# works 
def create_undirected_graph(edges):
    # Initialize empty dictionary to store the graph
    graph = {}
    
    # Iterate through each edge (connection between two nodes)
    for a, b in edges:
        # If node 'a' is not yet in the graph, add it with an empty list
        if a not in graph:
            graph[a] = []
        # If node 'b' is not yet in the graph, add it with an empty list
        if b not in graph:
            graph[b] = []
            
        # Add each node as a neighbor to the other (undirected graph)
        graph[a].append(b)
        graph[b].append(a)
        
    # Return the completed adjacency list representation
    return graph
 
def undirected_path(edges, node_A, node_B):
    # Convert edge list to adjacency list for easier traversal
    graph = create_undirected_graph(edges)
    
    # Helper function to perform depth-first search
    def dfs(current, target, visited):
        # Base case 1: If we found the target node, we have a path
        if current == target:
            return True
            
        # Base case 2: If we've already visited this node, avoid cycles
        if current in visited:
            return False
            
        # Mark the current node as visited
        visited.add(current)
        
        # Recursively check all unvisited neighbors
        for neighbor in graph[current]:
            # If any neighbor leads to the target, return True
            if dfs(neighbor, target, visited):
                return True
                
        # If no neighbors lead to the target, return False
        return False
    
    # Start DFS from node_A, looking for node_B, with an empty visited set
    return dfs(node_A, node_B, set())


print(undirected_path(edges,'j','m'))

# Test Cases
if __name__ == "__main__":
    edges1 = [('i', 'j'), ('k', 'i'), ('m', 'k'), ('k', 'l'), ('o', 'n')]
    result1 = undirected_path(edges1, 'j', 'm')
    print("Test Case 1:", result1, "Passed" if result1 == True else "Failed")
    assert result1 == True
    # Expected Output: True

    edges2 = [('i', 'j'), ('k', 'i'), ('m', 'k'), ('k', 'l'), ('o', 'n')]
    result2 = undirected_path(edges2, 'j', 'o')
    print("Test Case 2:", result2, "Passed" if result2 == False else "Failed")
    assert result2 == False
    # Expected Output: False

    edges3 = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e')]
    result3 = undirected_path(edges3, 'a', 'e')
    print("Test Case 3:", result3, "Passed" if result3 == True else "Failed")
    assert result3 == True
    # Expected Output: True

    edges4 = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e')]
    result4 = undirected_path(edges4, 'a', 'f')
    print("Test Case 4:", result4, "Passed" if result4 == False else "Failed")
    assert result4 == False
    # Expected Output: False