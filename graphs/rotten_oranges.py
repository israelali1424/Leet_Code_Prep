'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
'''
from typing import List
from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Create Vars for Fresh Rotten and None 
        use bfs 
        var rows cols done 
        mins set to -1 done 
        you need a quue done 
        first loop through the maxtrix 
        make a  count of all fresh oranges 
        and all rooten oranges to the quuue 
        while the q exist: bfs 
        pop all the values from the quue 
        mins +=1 
        loop through the pop.pped q values 
        # check if the ajcenent item is fresh and 
         make rotten by reducing the number of fresh oranges 
        # return minute 
        '''
        EMPTY, FRESH, ROTTEN = 0,1,2
        rows,cols = len(grid),len(grid[0])
        fresh_oranges = 0
        q = deque()
        mins = -1 # set to negative  becuase if set to zero will get an index error 

        for r in range(0,rows):
            for  c in range(0,cols):
                cell = grid[r][c]
                if cell == FRESH:
                    fresh_oranges+=1
                if cell == ROTTEN:
                    q.append((r,c))
        if fresh_oranges == 0: return fresh_oranges
        while q:
            q_size = len(q)
            mins+=1
            for orange in range(0,q_size):
                
                i,j  = q.popleft()
             
                for r, c in [(i, j+1), (i+1,j), (i,j-1), (i-1,j)]:
                    i_inbound = 0<= r < rows
                    j_inbound = 0<= c < cols
                    if i_inbound and j_inbound and grid[r][c] == FRESH:
                        grid[r][c] = ROTTEN
                        fresh_oranges -=1
                        q.append((r,c))
        if fresh_oranges !=0:
            return -1
        return mins
                    






# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Regular case with all oranges rotting
    grid1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    result1 = solution.orangesRotting(grid1)
    print("Test Case 1:", result1, "Passed" if result1 == 4 else "Failed")
    assert result1 == 4
    # Expected Output: 4

    # Test Case 2: Impossible to rot all oranges
    grid2 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    result2 = solution.orangesRotting(grid2)
    print("Test Case 2:", result2, "Passed" if result2 == -1 else "Failed")
    assert result2 == -1
    # Expected Output: -1
    # Test Case 3: No fresh oranges
    grid3 = [[0, 2]]
    result3 = solution.orangesRotting(grid3)
    print("Test Case 3:", result3, "Passed" if result3 == 0 else "Failed")
    assert result3 == 0
    # Expected Output: 0

    # Test Case 4: Single fresh orange
    grid4 = [[1]]
    result4 = solution.orangesRotting(grid4)
    print("Test Case 4:", result4, "Passed" if result4 == -1 else "Failed")
    assert result4 == -1
    # Expected Output: -1

    # Test Case 5: Single rotten orange
    grid5 = [[2]]
    result5 = solution.orangesRotting(grid5)
    print("Test Case 5:", result5, "Passed" if result5 == 0 else "Failed")
    assert result5 == 0
    # Expected Output: 0

    # Test Case 6: Empty grid
    grid6 = [[]]
    result6 = solution.orangesRotting(grid6)
    print("Test Case 6:", result6, "Passed" if result6 == 0 else "Failed")
    assert result6 == 0
    # Expected Output: 0
