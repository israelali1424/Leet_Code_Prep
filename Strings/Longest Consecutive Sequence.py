'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''
from typing import List
# Neetcode Solution Too slow Fails test caeses 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # Check if it's the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest
 #Chatgpt Solution   
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # Only start counting if `n` is the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest
# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Regular case with a sequence
    nums1 = [100, 4, 200, 1, 3, 2]
    result1 = solution.longestConsecutive(nums1)
    print("Test Case 1:", result1, "Passed" if result1 == 4 else "Failed")
    assert result1 == 4
    # Expected Output: 4

    # Test Case 2: Longer sequence
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    result2 = solution.longestConsecutive(nums2)
    print("Test Case 2:", result2, "Passed" if result2 == 9 else "Failed")
    assert result2 == 9
    # Expected Output: 9

    # Test Case 3: No sequence
    nums3 = [10, 5, 20]
    result3 = solution.longestConsecutive(nums3)
    print("Test Case 3:", result3, "Passed" if result3 == 1 else "Failed")
    assert result3 == 1
    # Expected Output: 1
    
    # Test Case 4: Single element
    nums4 = [1]
    result4 = solution.longestConsecutive(nums4)
    print("Test Case 4:", result4, "Passed" if result4 == 1 else "Failed")
    assert result4 == 1
    # Expected Output: 1

    # Test Case 5: Empty list
    nums5 = []
    result5 = solution.longestConsecutive(nums5)
    print("Test Case 5:", result5, "Passed" if result5 == 0 else "Failed")
    assert result5 == 0
    # Expected Output: 0

    # Test Case 6: Sequence with duplicates
    nums6 = [1, 2, 2, 3, 4]
    result6 = solution.longestConsecutive(nums6)
    print("Test Case 6:", result6, "Passed" if result6 == 4 else "Failed")
    assert result6 == 4
    # Expected Output: 4