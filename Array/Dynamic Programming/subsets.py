'''
iven an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
'''
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)  # Don't forget to call dfs with initial index 0
        return res
    

# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Regular case with three elements
    nums1 = [1, 2, 3]
    result1 = solution.subsets(nums1)
    print("Test Case 1:", result1, "Passed" if result1 == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]] else "Failed")
    #assert result1 == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    # Expected Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

    # Test Case 2: Single element
    nums2 = [1]
    result2 = solution.subsets(nums2)
    print("Test Case 2:", result2, "Passed" if result2 == [[], [1]] else "Failed")
    #assert result2 == [[], [1]]
    # Expected Output: [[], [1]]

    # Test Case 3: Empty list
    nums3 = []
    result3 = solution.subsets(nums3)
    print("Test Case 3:", result3, "Passed" if result3 == [[]] else "Failed")
    #assert result3 == [[]]
    # Expected Output: [[]]

    # Test Case 4: Two elements
    nums4 = [0, 1]
    result4 = solution.subsets(nums4)
    print("Test Case 4:", result4, "Passed" if result4 == [[], [0], [1], [0, 1]] else "Failed")
    #assert result4 == [[], [0], [1], [0, 1]]
    # Expected Output: [[], [0], [1], [0, 1]]
