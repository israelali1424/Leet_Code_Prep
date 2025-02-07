'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
'''
#2/07/2025 Failed Solution
'''
  Issues with the original implementation:
        1. **Incorrect condition handling (`total_sum == target`)**:
           - The function should update `min_sum` whenever `total_sum >= target`, not only when `total_sum == target`.
           - Otherwise, it may miss cases where a subarray exceeds `target` but could still be minimized.

        2. **Incorrect pointer handling**:
           - In the `elif total_sum == target:` block, `right` is incremented unnecessarily.
           - Instead of blindly expanding `right`, the function should shrink the window from the `left` 
             to minimize the subarray size.

        3. **Failure to minimize window efficiently**:
           - The function should always attempt to shrink the window (by moving `left`) while `total_sum >= target`.
           - The original implementation only shrinks the window in the `else` block but doesn't do so aggressively.

        4. **Edge case handling**:
           - If no valid subarray is found, `math.inf` should be converted to `0` before returning.

'''
import math
from typing import List
class Solution_One:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        left = 0
        right =0 
        min_window = math.inf
        total_sum = 0
        create a while loop with the bounds right <= len(nums):
        if total_sum < target:
        toal_sum += nums[right]
        if total_sum == target: 
        min_win = min(right-left) +1, min_window)
        else:
        total_sum - = nums[left]
        left+=1 
        '''
        '''
        [2,3,1,2,4,3]
        total_sum = 0
        left =0 nums[0] = 2 
        right = 0 nums[0] =2 
        total_sum +=  nums[right] 2 
        right +=1 
        left = 0 nums[0] = 2 
        right =1 nums[1] = 3 
        total_sum = 2
        total_sum+= nums[1](3) =5 
        right+=1 
        total_sum = 5 
        left =0 nums[0] = 2
        right = nums[2] = 1 
        total_sum =5+= 1 
        total_sum = 6 
        right +=1 
        total_sum = 6 
        left = 0 
        right = nums[3] = 2 
        total_sum = 6 
        total_sum +=2 = 8 
        right +=1
        total_sum = 8 
        total_sum -=2 =6
        left = 
        right [4] = 4
        6+4 = 10 
        total - 3 = 7 
        right+=1 
        left +1 

        total
        '''
        left = 0 
        right = 0 
        min_sum= math.inf 
        total_sum = 0 
        while right < len(nums):
            if total_sum < target:
                total_sum+=nums[right]
                right+=1 

            elif total_sum == target:
                print(nums[left:right+1])
                min_sum = min(min_sum,right-left+1)
                right+=1
            else:
                total_sum-=nums[left]
                left+=1
        return min_sum if min_sum != math.inf else 0  # Return 0 if no subarray is found

# Working Solution

import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_window = math.inf
        total_sum = 0

        for right in range(len(nums)):  # Expand the window
            total_sum += nums[right]
            
            # Shrink the window while the sum is at least `target`
            while total_sum >= target:
                min_window = min(min_window, right - left + 1)
                total_sum -= nums[left]
                left += 1  # Shrink from left

        return min_window if min_window != math.inf else 0  # Return 0 if no subarray is found
# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Regular case with a valid subarray
    target1 = 7
    nums1 = [2, 3, 1, 2, 4, 3]
    result1 = solution.minSubArrayLen(target1, nums1)
    print("Test Case 1:", result1, "Passed" if result1 == 2 else "Failed")
    assert result1 == 2
    # Expected Output: 2

    # Test Case 2: No valid subarray
    target2 = 100
    nums2 = [1, 2, 3, 4, 5]
    result2 = solution.minSubArrayLen(target2, nums2)
    print("Test Case 2:", result2, "Passed" if result2 == 0 else "Failed")
    assert result2 == 0
    # Expected Output: 0

    # Test Case 3: Single element equal to target
    target3 = 5
    nums3 = [5]
    result3 = solution.minSubArrayLen(target3, nums3)
    print("Test Case 3:", result3, "Passed" if result3 == 1 else "Failed")
    assert result3 == 1
    # Expected Output: 1

    # Test Case 4: Single element less than target
    target4 = 5
    nums4 = [3]
    result4 = solution.minSubArrayLen(target4, nums4)
    print("Test Case 4:", result4, "Passed" if result4 == 0 else "Failed")
    assert result4 == 0
    # Expected Output: 0