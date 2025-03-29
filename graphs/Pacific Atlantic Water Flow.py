from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Initialize queues and visited sets for both oceans
        pacific_que = deque()  # Queue for BFS from Pacific Ocean
        pacific_seen = set()   # Set to track cells visited from Pacific
        
        atlantic_que = deque() # Queue for BFS from Atlantic Ocean
        atlantic_seen = set()  # Set to track cells visited from Atlantic
        
        # Get dimensions of the island
        row, col = len(heights), len(heights[0])
        
        # Add all cells on Pacific borders (top and left edges) to the queue
        # Add top edge (row 0)
        for j in range(col):
            pacific_que.append((0, j))
            pacific_seen.add((0, j))
        
        # Add left edge (column 0, skipping the top-left corner which is already added)
        for i in range(1, row):
            pacific_que.append((i, 0))
            pacific_seen.add((i, 0))
        
        # Add all cells on Atlantic borders (right and bottom edges) to the queue
        # Add right edge (column col-1)
        for j in range(row): 
            atlantic_que.append((j, col-1))
            atlantic_seen.add((j, col-1))
        
        # Add bottom edge (row row-1, skipping the bottom-right corner which is already added)
        for i in range(col-1):
            atlantic_que.append((row-1, i))
            atlantic_seen.add((row-1, i))
        
        def get_coords(que, seen):
            """
            Performs a BFS to find all cells that water can flow from to reach the ocean.
            Since we're starting from the ocean and working backwards, we look for cells
            with height >= the current cell (water flows down, but we're traversing up).
            
            Args:
                que: Queue containing the starting cells (ocean borders)
                seen: Set to track visited cells
                
            Returns:
                Set of coordinates that can reach the given ocean
            """
            coords = set()
            while que:
                i, j = que.popleft()
                coords.add((i, j))
                
                # Check all four adjacent cells (north, south, east, west)
                for i_off, j_off in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    r, c = i + i_off, j + j_off
                    
                    # If the adjacent cell is valid, has sufficient height, and hasn't been seen
                    if (0 <= r < row and 0 <= c < col and 
                        heights[r][c] >= heights[i][j] and  # Water can flow from higher to equal or lower cells
                        (r, c) not in seen):
                        seen.add((r, c))
                        que.append((r, c))
            return coords
        
        # Get all cells that can reach Pacific and Atlantic
        p_coords = get_coords(pacific_que, pacific_seen)
        a_coords = get_coords(atlantic_que, atlantic_seen)
        
        # Return the intersection of both sets - cells that can reach both oceans
        return list(p_coords.intersection(a_coords))