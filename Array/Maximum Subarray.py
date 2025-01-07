'''
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.


Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
# must be atv least o(n) time
'''
#brute force
import math
from typing import List
class Solution:
    def maxSubArrayBruteForce(self, nums: List[int]) -> int:
        max_sum =-5000
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                 max_sum  = max(max_sum,sum(nums[i:j+1]))
        return max_sum
    
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        curr_sum = 0
        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n
            max_sub = max(max_sub, curr_sum)
        return max_sub