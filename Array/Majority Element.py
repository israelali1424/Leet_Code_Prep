'''
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums)
        count_dict = {}
        for num in nums:
            if num not in count_dict:
                count_dict[num] = 1
            else: 
                count_dict[num] +=1
        for key, val in count_dict.items():
            if val > (size //2):
                return key 