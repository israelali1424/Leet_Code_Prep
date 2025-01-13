'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''
# my broke solution
from collections import deque 
class Solution:
    def productExceptSelf_broke(self, nums: List[int]) -> List[int]:
        q = deque(nums)
        result = []
        length = len(nums)
        for i in range(0,length):
            product = 1 
            #print(nums[i])
            not_allowed = q.popleft()
            #print(not_allowed)
            for j in range(0,length):
                if nums[j] != not_allowed: # this falies becuase you are skiping the value of the current index when 
                    # you should be skipping acutal index 
                    product *= nums[j]    
            result.append(product)
        return result
# working solution brute force

    def productExceptSelf_brute_force(self, nums: List[int]) -> List[int]:
        result = []
        length = len(nums)
        
        # Iterate over each element in the list
        for i in range(length):
            product = 1
            
            # Calculate the product for all elements except nums[i]
            for j in range(length):
                if i != j:  # Skip the current index
                    product *= nums[j]
            
            result.append(product)
        
        return result
from typing import List
# optimized solution``

def productExceptSelf(self, nums: List[int]) -> List[int]:
    # Get the length of the input array
    length = len(nums)
    
    # Initialize the result array with 1s
    # This will hold the final product of all elements except self
    result = [1] * length
    
    # Variable to keep track of the product of all elements to the left of the current index
    left_product = 1
    
    # First pass: Calculate the products of all elements to the left of each index
    for i in range(length):
        # Assign the current left_product to the result for index i
        result[i] = left_product
        # Update left_product by multiplying it with nums[i] (current element)
        left_product *= nums[i]
    
    # Variable to keep track of the product of all elements to the right of the current index
    right_product = 1
    
    # Second pass: Calculate the products of all elements to the right of each index
    # and multiply them with the left products already stored in result
    for i in range(length - 1, -1, -1):  # Start from the last element and move left
        # Multiply the current result[i] (left product) with right_product
        result[i] *= right_product
        # Update right_product by multiplying it with nums[i] (current element)
        right_product *= nums[i]
    
    # Return the result array containing the product of all elements except self
    return result
