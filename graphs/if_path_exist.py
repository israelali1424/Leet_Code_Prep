#3/3/2025
# class from Claude 
class GraphPathFinder:
    def __init__(self, graph):
        """
        Initialize the graph path finder.
        
        Args:
        graph (dict): Adjacency list representation of the graph
        """
        self.graph = graph
    
    def path_exists_dfs(self, start, end):
        """
        Determine if a path exists between start and end nodes using Depth-First Search.
        
        Args:
        start: Starting node
        end: Destination node
        
        Returns:
        bool: True if path exists, False otherwise
        """
        # Set to keep track of visited nodes to prevent infinite loops
        visited = set()
        
        def dfs(current):
            # If we've reached the destination, return True
            if current == end:
                return True
            
            # Mark current node as visited
            visited.add(current)
            
            # Explore all neighboring nodes
            for neighbor in self.graph.get(current, []):
                # Only explore unvisited neighbors
                if neighbor not in visited:
                    # Recursively search from this neighbor
                    if dfs(neighbor):
                        return True
            
            # No path found
            return False
        
        # Start the depth-first search
        return dfs(start)
    
    def path_exists_bfs(self, start, end):
        """
        Determine if a path exists between start and end nodes using Breadth-First Search.
        
        Args:
        start: Starting node
        end: Destination node
        
        Returns:
        bool: True if path exists, False otherwise
        """
        # Queue for BFS
        queue = [start]
        
        # Set to keep track of visited nodes
        visited = set([start])
        
        while queue:
            # Get the next node to explore
            current = queue.pop(0)
            
            # If we've reached the destination, return True
            if current == end:
                return True
            
            # Explore all neighboring nodes
            for neighbor in self.graph.get(current, []):
                # Only add unvisited neighbors to the queue
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        
        # No path found
        return False

# Example usage
def main():
    # Example graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    # Create a graph path finder
    path_finder = GraphPathFinder(graph)
    
    # Test path existence using both DFS and BFS
    print("DFS Path from A to F:", path_finder.path_exists_dfs('A', 'F'))
    print("BFS Path from A to F:", path_finder.path_exists_bfs('A', 'F'))
    
    # Test path that doesn't exist
    print("DFS Path from D to A:", path_finder.path_exists_dfs('D', 'A'))
    print("BFS Path from D to A:", path_finder.path_exists_bfs('D', 'A'))

# Run the example
if __name__ == '__main__':
    main()
    
'''
I'll solve the problem of determining if a path exists in a graph and explain the algorithm in detail. I'll implement this using depth-first search (DFS) and breadth-first search (BFS) approaches.

```python
class GraphPathFinder:
    def __init__(self, graph):
        """
        Initialize the graph path finder.
        
        Args:
        graph (dict): Adjacency list representation of the graph
        """
        self.graph = graph
    
    def path_exists_dfs(self, start, end):
        """
        Determine if a path exists between start and end nodes using Depth-First Search.
        
        Args:
        start: Starting node
        end: Destination node
        
        Returns:
        bool: True if path exists, False otherwise
        """
        # Set to keep track of visited nodes to prevent infinite loops
        visited = set()
        
        def dfs(current):
            # If we've reached the destination, return True
            if current == end:
                return True
            
            # Mark current node as visited
            visited.add(current)
            
            # Explore all neighboring nodes
            for neighbor in self.graph.get(current, []):
                # Only explore unvisited neighbors
                if neighbor not in visited:
                    # Recursively search from this neighbor
                    if dfs(neighbor):
                        return True
            
            # No path found
            return False
        
        # Start the depth-first search
        return dfs(start)
    
    def path_exists_bfs(self, start, end):
        """
        Determine if a path exists between start and end nodes using Breadth-First Search.
        
        Args:
        start: Starting node
        end: Destination node
        
        Returns:
        bool: True if path exists, False otherwise
        """
        # Queue for BFS
        queue = [start]
        
        # Set to keep track of visited nodes
        visited = set([start])
        
        while queue:
            # Get the next node to explore
            current = queue.pop(0)
            
            # If we've reached the destination, return True
            if current == end:
                return True
            
            # Explore all neighboring nodes
            for neighbor in self.graph.get(current, []):
                # Only add unvisited neighbors to the queue
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        
        # No path found
        return False

# Example usage
def main():
    # Example graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    # Create a graph path finder
    path_finder = GraphPathFinder(graph)
    
    # Test path existence using both DFS and BFS
    print("DFS Path from A to F:", path_finder.path_exists_dfs('A', 'F'))
    print("BFS Path from A to F:", path_finder.path_exists_bfs('A', 'F'))
    
    # Test path that doesn't exist
    print("DFS Path from D to A:", path_finder.path_exists_dfs('D', 'A'))
    print("BFS Path from D to A:", path_finder.path_exists_bfs('D', 'A'))

# Run the example
if __name__ == '__main__':
    main()

```

Let me explain how path existence algorithms work:

### Depth-First Search (DFS) Approach
1. DFS explores as far as possible along each branch before backtracking
2. It uses recursion or a stack to keep track of nodes to visit
3. Key steps:
   - Start at the initial node
   - Mark the current node as visited
   - Explore each unvisited neighbor recursively
   - If the destination is found, return True
   - If no path is found after exploring all neighbors, return False

### Breadth-First Search (BFS) Approach
1. BFS explores all neighbors at the present depth before moving to nodes at the next depth level
2. It uses a queue to manage the nodes to visit
3. Key steps:
   - Start at the initial node
   - Add initial node to a queue and mark as visited
   - While the queue is not empty:
     * Remove the first node from the queue
     * If it's the destination, return True
     * Add all unvisited neighbors to the queue

### Key Differences
- DFS goes deep first (uses recursion/stack)
- BFS goes wide first (uses queue)
- DFS can be more memory-efficient for deep graphs
- BFS finds the shortest path in an unweighted graph

### Time and Space Complexity
- Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
- Space Complexity: O(V) for both approaches

The code demonstrates both methods on a sample graph. The main differences are in the implementation:
- DFS uses recursive exploration
- BFS uses a queue-based iterative approach

Would you like me to elaborate on any part of the explanation or the implementation?
'''