'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
'''
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        
        def explore(r, c):
            # Check if out of bounds, not a land cell, or already visited
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                grid[r][c] == 0):
                return 0
            
            # Mark the current cell as visited
            grid[r][c] = 0
            
            # Recursively explore and count connected land cells
            return 1 + (
                explore(r+1, c) +  # down
                explore(r-1, c) +  # up
                explore(r, c+1) +  # right
                explore(r, c-1)    # left
            )
        
        # Iterate through the grid to find maximum island area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, explore(r, c))
        
        return max_area