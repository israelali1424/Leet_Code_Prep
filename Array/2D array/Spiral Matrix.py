'''
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

'''
#my broken example
from typing import List
class Solution:
    def spiralOrderBroke(self, matrix: List[List[int]]) -> List[int]:
        # bounds 
        rows,cols = len(matrix),len(matrix[0])
        # print(f'row:{row}')
        # print(f'col:{col}')
        top_bound = (0,cols-1) # 2,1
        left_bound = (cols-1,rows-1) # (2,2)
        lower_bound = (rows,cols-1) #(0,2)
        right_bound = (rows-1,0) # (0,0)
      
        seen = set()
        row_index =0
        col_index = 0
        result = []
        for row in range(0,rows):
            for col in range(0,cols):
                
                if (row,col) == top_bound:
                    print(row, col)
                    print(matrix[row][col])
                    seen.add((row,col))

        
        
        

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        result = []
        rows, cols = len(matrix), len(matrix[0])
        
        top = 0
        right = cols - 1
        bottom = rows - 1
        left = 0
        
        while top <= bottom and left <= right:
            # Traverse right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            
            # Traverse down
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            
            # Traverse left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            
            # Traverse up
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        
        return result

# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Regular square matrix
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result1 = solution.spiralOrder(matrix1)
    print("Test Case 1:", result1, "Passed" if result1 == [1, 2, 3, 6, 9, 8, 7, 4, 5] else "Failed")
    assert result1 == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    # Expected Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

    # Test Case 2: Rectangular matrix (more columns)
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    result2 = solution.spiralOrder(matrix2)
    print("Test Case 2:", result2, "Passed" if result2 == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7] else "Failed")
    assert result2 == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    # Expected Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    # Test Case 3: Rectangular matrix (more rows)
    matrix3 = [[1, 2], [3, 4], [5, 6], [7, 8]]
    result3 = solution.spiralOrder(matrix3)
    print("Test Case 3:", result3, "Passed" if result3 == [1, 2, 4, 6, 8, 7, 5, 3] else "Failed")
    assert result3 == [1, 2, 4, 6, 8, 7, 5, 3]
    
    
    
    # Test Case 4: Single row
    matrix4 = [[1, 2, 3, 4]]
    result4 = solution.spiralOrder(matrix4)
    print("Test Case 4:", result4, "Passed" if result4 == [1, 2, 3, 4] else "Failed")
    assert result4 == [1, 2, 3, 4]
    # Expected Output: [1, 2, 3, 4]

    # Test Case 5: Single column
    matrix5 = [[1], [2], [3], [4]]
    result5 = solution.spiralOrder(matrix5)
    print("Test Case 5:", result5, "Passed" if result5 == [1, 2, 3, 4] else "Failed")
    assert result5 == [1, 2, 3, 4]
    # Expected Output: [1, 2, 3, 4]

    # Test Case 6: Single element
    matrix6 = [[1]]
    result6 = solution.spiralOrder(matrix6)
    print("Test Case 6:", result6, "Passed" if result6 == [1] else "Failed")
    assert result6 == [1]
    # Expected Output: [1]

    # Test Case 7: Empty matrix
    matrix7 = []
    result7 = solution.spiralOrder(matrix7)
    print("Test Case 7:", result7, "Passed" if result7 == [] else "Failed")
    assert result7 == []
    # Expected Output: []