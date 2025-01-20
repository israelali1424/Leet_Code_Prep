"""
Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Input: nums = [-7,-3,2,3,11]

"""
from typing import List
class Solution:
    # This the brute force solution approach using bult  in sort function
    def sortedSquares_brute_force(self, nums: List[int]) -> List[int]:
        # I can only think of the brute force solution will try to improve later

        result = []
        for num in nums:
            val = pow( num,2)
            result.append(val)

        return sorted(result)
    
    # This is brute force apprach using  quick sort on the result array
    def sortedSquares_qucik_sort(self, nums: List[int]) -> List[int]:

        # I can only think of the brute force solution will try to improve later
        def quicksort(nums_list:List[int]):

            if  len(nums_list) <=1:
                return nums_list
            pivot = nums_list.pop()
            left = []
            right = []
            print(pivot)
            for num in nums_list:
                if num < pivot:
                    left.append(num)
                else:
                    right.append(num)
            return quicksort(left) + [pivot] + quicksort(right)


        result = []
        for num in nums:
            val = pow( num,2)
            result.append(val)
            
        #print(quicksort(result))

            

    def sortedSquares_optimzed(self, nums: List[int]) -> List[int]:
        # Initialize two pointers
        left, right = 0, len(nums) - 1
        result = [0] * len(nums)
        
        # Start from the end of the result array
        for i in range(len(nums) - 1, -1, -1):
            # Compare the absolute values of the elements at the two pointers
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
        
        return result
#Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Mixed positive and negative numbers
    nums1 = [-4, -1, 0, 3, 10]
    result1 = solution.sortedSquares_optimized(nums1)
    print("Test Case 1:", result1, "Passed" if result1 == [0, 1, 9, 16, 100] else "Failed")
    assert result1 == [0, 1, 9, 16, 100]
    # Expected Output: [0, 1, 9, 16, 100]

    # Test Case 2: All negative numbers
    nums2 = [-7, -3, -1]
    result2 = solution.sortedSquares_optimized(nums2)
    print("Test Case 2:", result2, "Passed" if result2 == [1, 9, 49] else "Failed")
    assert result2 == [1, 9, 49]
    # Expected Output: [1, 9, 49]

    # Test Case 3: All positive numbers
    nums3 = [1, 2, 3, 4, 5]
    result3 = solution.sortedSquares_optimized(nums3)
    print("Test Case 3:", result3, "Passed" if result3 == [1, 4, 9, 16, 25] else "Failed")
    assert result3 == [1, 4, 9, 16, 25]
    # Expected Output: [1, 4, 9, 16, 25]

    # Test Case 4: Single element
    nums4 = [5]
    result4 = solution.sortedSquares_optimized(nums4)
    print("Test Case 4:", result4, "Passed" if result4 == [25] else "Failed")
    assert result4 == [25]
    # Expected Output: [25]

    # Test Case 5: Empty list
    nums5 = []
    result5 = solution.sortedSquares_optimized(nums5)
    print("Test Case 5:", result5, "Passed" if result5 == [] else "Failed")
    assert result5 == []
    # Expected Output: []