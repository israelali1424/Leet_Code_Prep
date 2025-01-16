'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
'''
from typing import List
class Solution():
    def canFinish(self,numCourses, prerequisites):
        # Create an adjacency list to represent the graph
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        # Keep track of visited courses
        # 0 = unvisited, 1 = visiting (in current path), 2 = completed
        visited = [0] * numCourses
        
        def hasCycle(course):
            # If we're visiting this course in current path, we found a cycle
            if visited[course] == 1:
                return True
            # If we've already completed this course, no cycle here
            if visited[course] == 2:
                return False
                
            # Mark as being visited in current path
            visited[course] = 1
            
            # Check all prerequisites of this course
            for prereq in graph[course]:
                if hasCycle(prereq):
                    return True
                    
            # Mark as completed
            visited[course] = 2
            return False
        
        # Check each course
        for course in range(numCourses):
            if visited[course] == 0:  # if unvisited
                if hasCycle(course):
                    return False  # Can't finish if there's a cycle
                    
        return True
from collections import defaultdict
from typing import List

class SolutionOne:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        courses = prerequisites
        
        # Build the graph
        for a, b in courses:
            g[a].append(b)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses
        
        def dfs(node):
            state = states[node]
            if state == VISITED:
                return True
            elif state == VISITING:
                return False
            
            states[node] = VISITING
            for nei in g[node]:
                if not dfs(nei):
                    return False
            states[node] = VISITED
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True  # Time: O(N)
 # from https://www.youtube.com/watch?v=nz5V5pOiT8w
# Importing the Solution class
solution = Solution()

# Test Case 1: No prerequisites
print("Test Case 1:", solution.canFinish(2, []))
# Expected Output: True

# Test Case 2: Simple cycle
print("Test Case 2:", solution.canFinish(2, [[1, 0], [0, 1]]))
# Expected Output: False

# Test Case 3: Multiple courses with no cycle
print("Test Case 3:", solution.canFinish(4, [[1, 0], [2, 1], [3, 2]]))
# Expected Output: True

# Test Case 4: Multiple courses with a cycle
print("Test Case 4:", solution.canFinish(4, [[1, 0], [2, 1], [3, 2], [1, 3]]))
# Expected Output: False

# Test Case 5: Single course with no prerequisites
print("Test Case 5:", solution.canFinish(1, []))
# Expected Output: True

# Test Case 6: Single course with a self-dependency
print("Test Case 6:", solution.canFinish(1, [[0, 0]]))
# Expected Output: False

# Test Case 7: Disconnected graph with no cycles
print("Test Case 7:", solution.canFinish(5, [[1, 0], [2, 1], [4, 3]]))
# Expected Output: True

# Test Case 8: Disconnected graph with a cycle
print("Test Case 8:", solution.canFinish(5, [[1, 0], [2, 1], [4, 3], [3, 4]]))
# Expected Output: False