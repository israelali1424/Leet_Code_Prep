'''
Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

 

Example 1:

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
Example 2:

Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
'''
import math
from typing import List
class Solution:
    # my answer and thought process
    def findClosestNumber(self, nums: List[int]) -> int:
        '''
        loop through the list 
        when the value is > currn min 
        rest the pairs and 
        and the new min valeus 
        if it == the current min 
        add to a paris dict 
        if < than do nothing 
        return max(min_pairs)
        '''
        min_val = math.inf
        min_pairs = {}
        for num in nums:
            diff = abs(0 - num)
            if diff < min_val:
                min_val = diff
                min_pairs = {}
                min_pairs[num] = diff 
            elif diff == min_val:
                min_pairs[num] = diff 
        return max(min_pairs.keys())
    '''
    **Time Complexity**: \(O(n)\), as you iterate through the list once.  
**Space Complexity**: \(O(k)\), where \(k\) is the number of elements with the same minimum absolute difference.
    '''            

        
# chatgpt answer

    def findClosestNumber_chatgpt(self,nums):
        min_val = float('inf')  # Initialize minimum absolute difference
        closest = None  # Initialize the closest number

        for num in nums:
            diff = abs(num)  # Calculate absolute difference
            # Update the closest number if a smaller diff is found
            if diff < min_val or (diff == min_val and num > closest):
                min_val = diff
                closest = num

        return closest

# Importing the Solution class
solution = Solution()

# Test Case 1: Mixed positive and negative numbers
print("Test Case 1:", solution.findClosestNumber([-4, -2, 1, 4, 8]))
# Expected Output: 1

# Test Case 2: All positive numbers
print("Test Case 2:", solution.findClosestNumber([2, 3, 5, 6, 7]))
# Expected Output: 2

# Test Case 3: All negative numbers
print("Test Case 3:", solution.findClosestNumber([-10, -5, -3, -1]))
# Expected Output: -1

# Test Case 4: Zero in the list
print("Test Case 4:", solution.findClosestNumber([-3, -2, 0, 2, 3]))
# Expected Output: 0

# Test Case 5: Single element list
print("Test Case 5:", solution.findClosestNumber([5]))
# Expected Output: 5

# Test Case 6: Multiple elements with the same absolute value
print("Test Case 6:", solution.findClosestNumber([-2, 2, -1, 1]))
# Expected Output: 1

# Test Case 7: Large numbers
print("Test Case 7:", solution.findClosestNumber([-1000000, 1000000, -999999, 999999]))
# Expected Output: 999999
