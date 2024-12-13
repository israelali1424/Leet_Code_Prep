'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
'''
# this Solution will pass the test cases but actually fail the question because it suppoed to use 
# constant space meaning no extra objects such a set or hasmap which what I did 
from typing import List
class Memory_Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # brute force
        # for number in nums:
        #     if nums.count(number)==1:
        #         return number 
        # return None
  
        seen = set()
        for number in nums:
            # 
            if number in seen:
                seen.remove(number)
            else:
                seen.add(number)
        return seen.pop()
    
    class Solution:
        def singleNumber(self, nums: List[int]) -> int:
            # Initialize a variable to store the result of XOR operations
            single_one = 0

            # Iterate over each number in the array
            for num in nums:
                # XOR the current number with the result
                # This will cancel out numbers that appear in pairs and keep the single number
                single_one = single_one ^ num

            # After all XOR operations, the result will be the single number
            return single_one
# Test cases for the singleNumber function

# Test Case 1: Single element in the list
nums1 = [1]
# Expected output: 1

# Test Case 2: All elements appear twice except one
nums2 = [4, 1, 2, 1, 2]
# Expected output: 4

# Test Case 3: Negative numbers with a single occurrence
nums3 = [-1, -2, -3, -1, -2]
# Expected output: -3

# Test Case 4: Large numbers with one single occurrence
nums4 = [1000000, 2000000, 1000000]
# Expected output: 2000000

# Test Case 5: Mixed positive and negative numbers
nums5 = [0, 1, -1, 1, 0]
# Expected output: -1

# Test Case 6: A larger list with one single occurrence
nums6 = [7, 3, 5, 4, 5, 3, 7]
# Expected output: 4

# Test Case 7: All numbers are the same except one
nums7 = [2, 2, 3, 2, 2]
# Expected output: 3

# Test Case 8: Edge case with zero
nums8 = [0, 0, 1]
# Expected output: 1

# Test Case 9: All numbers are negative except one positive
nums9 = [-5, -5, 10]
# Expected output: 10

# Test Case 10: Two numbers only, one without a pair
nums10 = [1, 2, 1]
# Expected output: 2
