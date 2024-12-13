'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''
from typing import List 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a for loop
        '''
        Create an empty dict
        loop through the list
        in the loop
        sum = target  - index
        check if sum in dict.keys()
        if sum in dict.keys return
        [dict[sum], index
        else return
        dict[nums[index],index] = index
        '''
        #
        #
        #
        # 
        hashmap = {}
        for index, value in enumerate(nums):
            dif = target - value

            if value in hashmap.keys():
                return [hashmap[nums[index]],index]
            else:
                hashmap[dif] = index
                
# Another way of doing it 

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         # create a seen array 
         # when a num that is seen array is equal to targer - nums 
         # reutn seen[nums] and index 
         seen = {}
         for  index, number in enumerate(nums):
            diff = target - number 
            if diff in seen.keys():
                return [seen[diff],index]
            else:
                seen[number] = index
                
                
def test_two_sum():
    # Case 1: Normal case with a solution present
    nums = [2, 7, 11, 15]
    target = 9
    assert two_sum(nums, target) == [0, 1], "Test Case 1 Failed"

    # Case 2: Multiple valid solutions, return the first one
    nums = [1, 3, 4, 2, 7]
    target = 6
    assert two_sum(nums, target) == [1, 3], "Test Case 2 Failed"

    # Case 3: Negative numbers in the list
    nums = [-1, -2, -3, -4, -5]
    target = -8
    assert two_sum(nums, target) == [2, 4], "Test Case 3 Failed"

    # Case 4: List contains zero and positive numbers
    nums = [0, 4, 3, 0]
    target = 0
    assert two_sum(nums, target) == [0, 3], "Test Case 4 Failed"

    # Case 5: Single element list (no valid solution)
    nums = [1]
    target = 2
    assert two_sum(nums, target) == None, "Test Case 5 Failed"

    # Case 6: No solution exists
    nums = [1, 2, 3]
    target = 7
    assert two_sum(nums, target) == None, "Test Case 6 Failed"

    print("All test cases passed!")

# Function to test
def two_sum(nums, target):
    hashmap = {}
    for index, value in enumerate(nums):
        dif = target - value
        if value in hashmap.keys():
            return [hashmap[value], index]
        else:
            hashmap[dif] = index
