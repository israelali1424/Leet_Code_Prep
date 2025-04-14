'''
ou are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
'''
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Step 1: Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()
#Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: 3x3 matrix
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution.rotate(matrix1)
    print("Test Case 1:", matrix1, "Passed" if matrix1 == [[7, 4, 1], [8, 5, 2], [9, 6, 3]] else "Failed")
    assert matrix1 == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    # Expected Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    # Test Case 2: 4x4 matrix
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    solution.rotate(matrix2)
    print("Test Case 2:", matrix2, "Passed" if matrix2 == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]] else "Failed")
    assert matrix2 == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    # Expected Output: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

    # Test Case 3: 2x2 matrix
    matrix3 = [[1, 2], [3, 4]]
    solution.rotate(matrix3)
    print("Test Case 3:", matrix3, "Passed" if matrix3 == [[3, 1], [4, 2]] else "Failed")
    assert matrix3 == [[3, 1], [4, 2]]
    # Expected Output: [[3, 1], [4, 2]]

    # Test Case 4: 1x1 matrix
    matrix4 = [[1]]
    solution.rotate(matrix4)
    print("Test Case 4:", matrix4, "Passed" if matrix4 == [[1]] else "Failed")
    assert matrix4 == [[1]]
    # Expected Output: [[1]]

