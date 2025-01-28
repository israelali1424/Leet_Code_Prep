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

'''
import math
from typing import List
#1/25/2025
# this is a sliding window question
# this solution passes 121/ 127 test cases becuase it is not efficient
# the avg_sum = sum(nums[left:right+1]) /k in each iteration is not efficient and slows it down 
class Solution:
    def findMaxAverage_inefficient(self, nums: List[int], k: int) -> float:
        '''
        start at index 0
        sliding windw question
        left = 0
        right = k -1
        while right <= len( nums)

        avg_sum = sum nums[left:right+1]
        max_sum = max (max_sum,avg_sum)
        '''
        left = 0
        right = k-1 
        max_avg = -math.inf 

        while right <= len(nums)-1: 
            avg_sum = sum(nums[left:right+1]) /k
            max_avg = max(max_avg,avg_sum) 
            left +=1
            right +=1 
        return max_avg
    
# chatgpt solution

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Calculate the sum of the initial window
        current_window_sum = sum(nums[:k])
        max_window_sum = current_window_sum

        # Slide the window across the array
        for i in range(k, len(nums)):
            # Update the window sum: add the new element and remove the leftmost element
            current_window_sum += nums[i] - nums[i - k]
            # Update the maximum sum
            max_window_sum = max(max_window_sum, current_window_sum)

        # Return the maximum average
        return max_window_sum / k
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def test_findMaxAverage(nums, k, expected):
    result = Solution().findMaxAverage(nums, k)
    if abs(result - expected) < 1e-5:  # Allowing a small margin for floating point comparison
        print(f"Test passed for nums={nums}, k={k}. Expected: {expected}, Got: {result}")
    else:
        print(f"Test failed for nums={nums}, k={k}. Expected: {expected}, Got: {result}")

# Test case 1: Basic example from the problem statement
nums1 = [1, 12, -5, -6, 50, 3]
k1 = 4
expected1 = 12.75
test_findMaxAverage(nums1, k1, expected1)

# Test case 2: Single element list
nums2 = [5]
k2 = 1
expected2 = 5.0
test_findMaxAverage(nums2, k2, expected2)

# Test case 3: All positive numbers
nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k3 = 5
expected3 = 8.0
test_findMaxAverage(nums3, k3, expected3)

# Test case 4: All negative numbers
nums4 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
k4 = 5
expected4 = -3.0
test_findMaxAverage(nums4, k4, expected4)

# Test case 5: Mixed positive and negative numbers
nums5 = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]
k5 = 2
expected5 = 0.0
test_findMaxAverage(nums5, k5, expected5)

# Test case 6: Larger k value
nums6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k6 = 10
expected6 = 5.5
test_findMaxAverage(nums6, k6, expected6)

# Test case 7: k equals the length of the list
nums7 = [1, 2, 3, 4, 5]
k7 = 5
expected7 = 3.0
test_findMaxAverage(nums7, k7, expected7)

# Test case 1: Basic example from the problem statement
nums1 = [1, 12, -5, -6, 50, 3]
k1 = 4
expected1 = 12.75
test_findMaxAverage(nums1, k1, expected1)

# Test case 2: Single element list
nums2 = [5]
k2 = 1
expected2 = 5.0
test_findMaxAverage(nums2, k2, expected2)

# Test case 3: All positive numbers
nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k3 = 5
expected3 = 8.0
test_findMaxAverage(nums3, k3, expected3)

# Test case 4: All negative numbers
nums4 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
k4 = 5
expected4 = -3.0
test_findMaxAverage(nums4, k4, expected4)

# Test case 5: Mixed positive and negative numbers
nums5 = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]
k5 = 2
expected5 = 0.0
test_findMaxAverage(nums5, k5, expected5)

# Test case 6: Larger k value
nums6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k6 = 10
expected6 = 5.5
test_findMaxAverage(nums6, k6, expected6)

# Test case 7: k equals the length of the list
nums7 = [1, 2, 3, 4, 5]
k7 = 5
expected7 = 3.0
test_findMaxAverage(nums7, k7, expected7)