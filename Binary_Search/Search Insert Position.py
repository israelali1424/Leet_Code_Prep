'''
Easy
Topics
Companies
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
'''
from typing import List
# my orginal solution wrong approach
# wrong because the while should be while left <= right not while left < right
# wrong beccause using nums[mid] == target -1 or nums[mid] == target + 1 does handle all cases and return the wrong result
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        insertBefore = None
        insertAfter  = None
        left = 0 
        right = len(nums)-1
        result = None
        #mid = (left + right) //2 # unsure if I have to restset after every loop

        while left < right: 
            mid = (left + right) //2
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                if nums[mid] == target -1:
                    insertAfter = {target: mid+1}
                left = mid +1 
            else: 
                if nums[mid] == target +1:
                    
                    insertBefore= {target : mid-1}
                right = mid -1 
                
        print(insertBefore,insertAfter)
                
        if insertBefore and insertAfter:
            result = insertBefore[target]

        if  insertBefore and not  insertAfter:
              result = insertBefore[target]
        if  not insertBefore and insertAfter:
            result = insertAfter[target]

        return result 
    
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Check if the target is found
            if nums[mid] == target:
                return mid

            # If the target is greater, adjust the left pointer
            elif nums[mid] < target:
                left = mid + 1

            # If the target is smaller, adjust the right pointer
            else:
                right = mid - 1

        # If the loop ends, return the position where the target would be inserted
        return left

# Test case 1: Basic example from the problem statement
nums1 = [1, 3, 5, 6]
target1 = 5
# Expected output: 2
print(Solution().searchInsert(nums1, target1))

# Test case 2: Insert position in the middle
nums2 = [1, 3, 5, 6]
target2 = 2
# Expected output: 1
print(Solution().searchInsert(nums2, target2))

# Test case 3: Insert position at the end
nums3 = [1, 3, 5, 6]
target3 = 7
# Expected output: 4
print(Solution().searchInsert(nums3, target3))

# Test case 4: Insert position at the beginning
nums4 = [1, 3, 5, 6]
target4 = 0
# Expected output: 0
print(Solution().searchInsert(nums4, target4))

# Test case 5: Empty list
nums5 = []
target5 = 5
# Expected output: 0
print(Solution().searchInsert(nums5, target5))

# Test case 6: Single element list, target less than element
nums6 = [1]
target6 = 0
# Expected output: 0
print(Solution().searchInsert(nums6, target6))

# Test case 7: Single element list, target greater than element
nums7 = [1]
target7 = 2
# Expected output: 1
print(Solution().searchInsert(nums7, target7))