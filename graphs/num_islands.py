'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
'''
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        seen = set() # keeps track of alrradt visted islands
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if self.explore(grid,row,col,seen):
                    islands+=1
        return islands
    def explore(self,grid,row,col,seen):
        row_inbounds = 0<=row<len(grid)
        col_inbounds = 0<=col<len(grid[0])
        if (row_inbounds==False or col_inbounds==False):return False
        if grid[row][col] == "0": return False 
        pos = f'{row , col}'
        if pos in seen:return False
        
        seen.add(pos)
        self.explore(grid,row-1,col,seen) # move/look up one 
        self.explore(grid,row+1,col,seen) # move/look down one 
        self.explore(grid,row,col-1,seen) # move/look right one 
        self.explore(grid,row,col+1,seen) # move/look left  one 

        return True




        