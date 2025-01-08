'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
'''
from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat):
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        # Step 1: Add all '0's to the queue and mark '1's as inf
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))  # Add zero cells to the queue
                else:
                    mat[r][c] = float('inf')  # Mark '1's as infinity
        
        # Step 2: BFS to update distances
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] > mat[r][c] + 1:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))
        
        return mat



sol = Solution()

# Test Case 1
mat1 = [
    [0,0,0],
    [0,1,0],
    [1,1,1]
]
print(sol.updateMatrix(mat1))
# Output: [[0,0,0],[0,1,0],[1,2,1]]

# Test Case 2
mat2 = [
    [0,1,1],
    [1,1,1],
    [1,1,0]
]
print(sol.updateMatrix(mat2))
# Output: [[0,1,2],[1,2,1],[2,1,0]]
