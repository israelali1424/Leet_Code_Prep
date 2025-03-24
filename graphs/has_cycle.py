"""
Cycle Detection in a Directed Graph

Problem Statement:
You are given a directed graph represented as an adjacency list. The graph consists of n nodes, labeled from 0 to n-1.
The adjacency list is represented as a dictionary where the keys are node labels and the values are lists of neighboring nodes.

Write a function detect_cycle(graph) that returns True if the graph contains at least one cycle, and False otherwise.
A cycle is a path that starts and ends at the same node, with at least one edge.

Example 1:
Input: graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
Output: True
Explanation: There are multiple cycles in this graph:
- 0 -> 1 -> 2 -> 0
- 0 -> 2 -> 0
- 3 -> 3 (self-loop)

Example 2:
Input: graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
Output: False
Explanation: This is a directed acyclic graph (DAG).

Constraints:
- 1 <= n <= 10^5
- 0 <= graph[i][j] < n
- The graph may contain self-loops.
- The graph may not be connected.

Follow-up: Can you implement both DFS and BFS approaches for this problem?
"""

def detect_cycle(graph):
    seen = set()
    def dfs(graph,node,seen):
         for neighbor in graph[node]:
            if neighbor in seen:
                return True
            else:
                seen.add(neighbor)
            if dfs(graph,neighbor,seen):
                return True
        
    for node in graph:
       seen.add(node)
       if dfs(graph,node,seen):
           return True
             
    return False 

    
    """
    Detects if there is a cycle in a directed graph represented as an adjacency list.
    
    Args:
        graph: A dictionary where keys are nodes and values are lists of neighbors
        
    Returns:
        bool: True if a cycle exists, False otherwise
    """
    # Your solution here
    '''
    creat a visted set 
    seen should  be in the fist lopp
    first loop through the keys
    loop though all the 
    # do the condtion check
    call the function  
    '''
    pass


# Test cases
def test_detect_cycle():
    # Test case 1 - Contains cycles
    graph1 = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
    assert detect_cycle(graph1) == True
    
    # Test case 2 - DAG (no cycles)
    graph2 = {0: [1, 2], 1: [3], 2: [3], 3: []}
    assert detect_cycle(graph2) == False
    
    # Test case 3 - Single node with self-loop
    graph3 = {0: [0]}
    assert detect_cycle(graph3) == True
    
    # Test case 4 - Disconnected graph with a cycle
    graph4 = {0: [1], 1: [2], 2: [], 3: [4], 4: [5], 5: [3]}
    assert detect_cycle(graph4) == True
    
def detect_cycle(graph):
    # Track nodes that have been visited in any path
    visited = set()
    # Track nodes in the current exploration path
    path = set()
    
    def dfs(node):
        # If node is already in our current path, we found a cycle
        if node in path:
            return True
            
        # If we've already completely explored this node before, no need to check again
        if node in visited:
            return False
            
        # Add node to current path and mark as visited
        path.add(node)
        visited.add(node)
        
        # Explore all neighbors
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
                
        # Remove node from current path when we're done exploring it
        path.remove(node)
        return False
    
    # Try starting DFS from each unvisited node
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
                
    return False

test_detect_cycle()