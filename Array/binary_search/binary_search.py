'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        left = 0 
        right = len(nums)-1 
        whlie left <= right:
            mid = left +right //2 
            check mid, if mid == target:
            return mid 
            if mid > target : # here where my code broke I had the right answer I just has a syntx error it should be if nums[mid]> target 
                left = mid +1 
            else:
                right = mid -1 
        return -1 if no match 
        
        '''
        left = 0
        right = len(nums)-1
        while left <=right: # unsure about this condtion 
            mid = (left+right)//2 
            print(mid)
            print(left)
            print(right)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: # less than 
                left = mid +1 
            else: right = mid -1 
        return -1 
