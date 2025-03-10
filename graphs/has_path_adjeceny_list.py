

def hasPathdfs_recursion(graph, src, dst):
    """
    Depth-First Search (DFS) using recursion to determine if there is a path from src to dst.
    
    :param graph: Dictionary representing the adjacency list of the graph
    :param src: Source node
    :param dst: Destination node
    :return: True if there is a path from src to dst, False otherwise
    """
    # Base case: if the source is the destination, return True
    if src == dst:
        print(src)
        return True
    
    # Recursively visit all neighbors of the current node
    for neighbor in graph[src]:
        if hasPathdfs_recursion(graph, neighbor, dst):
            return True
    
    # If no path is found, return False
    return False

from collections import deque

def hasPathbfs(graph, src, dst):
    """
    Breadth-First Search (BFS) to determine if there is a path from src to dst.
    
    :param graph: Dictionary representing the adjacency list of the graph
    :param src: Source node
    :param dst: Destination node
    :return: True if there is a path from src to dst, False otherwise
    """
    # Initialize a queue with the source node
    q = deque([src])
    
    # Process nodes in the queue
    while q:
        current = q.popleft()
        
        # If the current node is the destination, return True
        if current == dst:
            return True
        
        # Add all neighbors of the current node to the queue
        for neighbor in graph[current]:
            if neighbor == dst:
                return True
            else:
                q.append(neighbor)
    
    # If no path is found, return False
    return False
def hasPathdfs_recursion(graph, src, dst):
    """
    Depth-First Search (DFS) using recursion to determine if there is a path from src to dst.
    
    :param graph: Dictionary representing the adjacency list of the graph
    :param src: Source node
    :param dst: Destination node
    :return: True if there is a path from src to dst, False otherwise
    """
    # Base case: if the source is the destination, return True
    if src == dst:
        print(src)
        return True
    
    # Recursively visit all neighbors of the current node
    for neighbor in graph[src]:
        if hasPathdfs_recursion(graph, neighbor, dst):
            return True
    
    # If no path is found, return False
    return False

from collections import deque

def hasPathbfs(graph, src, dst):
    """
    Breadth-First Search (BFS) to determine if there is a path from src to dst.
    
    :param graph: Dictionary representing the adjacency list of the graph
    :param src: Source node
    :param dst: Destination node
    :return: True if there is a path from src to dst, False otherwise
    """
    # Initialize a queue with the source node
    q = deque([src])
    
    # Process nodes in the queue
    while q:
        current = q.popleft()
        
        # If the current node is the destination, return True
        if current == dst:
            return True
        
        # Add all neighbors of the current node to the queue
        for neighbor in graph[current]:
            if neighbor == dst:
                return True
            else:
                q.append(neighbor)
    
    # If no path is found, return False
    return False
# Time Complexity:
# Both DFS and BFS have a time complexity of O(V + E), where V is the number of vertices and E is the number of edges.
# This is because in the worst case, we need to visit all vertices and all edges.

# Space Complexity:
# DFS has a space complexity of O(V) due to the recursion stack.
# BFS has a space complexity of O(V) due to the queue used to store vertices.

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

#print (hasPathdfs_recursion(graph, 'f', 'k'))

print (hasPathbfs(graph, 'f', 'i'))