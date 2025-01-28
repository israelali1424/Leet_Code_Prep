
'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
Easy Question
'''
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])  # Calculate the sum of the first 'k' elements
        prev_sum = max_sum
        
        for i in range(1, len(nums) - k + 1):
            # Sliding window: subtract the first element of the previous window and add the next element
            current_sum = prev_sum - nums[i - 1] + nums[i + k - 1]
            prev_sum = current_sum
            
            # Update max_sum if the current_sum is greater
            if current_sum > max_sum:
                max_sum = current_sum
        
        return max_sum / k  # Return the average