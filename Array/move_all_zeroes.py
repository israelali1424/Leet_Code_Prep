from typing import List
def move_zeroes(nums):
    """
    Move all zeroes to the end of the array while maintaining the relative order of non-zero elements.
    """
    non_zero_index = 0  # Index to track the position where the next non-zero element should go

    # Iterate through the array
    for i in range(len(nums)):
        if nums[i] != 0:
            # Swap the non-zero element with the element at the current non-zero index
            nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
            non_zero_index += 1  # Increment the non-zero index

    return nums

nums = [0, 1, 0, 3, 12]
print(move_zeroes(nums))  # Output: [1, 3, 12, 0, 0]



class Solution:
    def moveZeroes_optimized(self, nums: List[int]) -> None:
        """
        Moves all zeros to the end while maintaining the order of non-zero elements.
        """
        non_zero_index = 0  # Tracks position to place the next non-zero number
        
        # Move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
        
        # Fill the remaining indices with zeros
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0

## Relation to Quick Sort
    '''
    ### 1. Partitioning Logic
    This algorithm resembles the partitioning step of **Quick Sort**, where elements are rearranged based on a pivot.

    - **In Quick Sort**:
    - Elements smaller than the pivot are moved to the left.
    - Elements larger than the pivot are moved to the right.

    - **In this function**:
    - Non-zero elements act as "smaller" elements (moved to the left).
    - Zeros act as "larger" elements (moved to the right).

    ### 2. Two-Pointer Technique
    Both this algorithm and Quick Sort's partition step use a **two-pointer approach**:
    - `non_zero_index` functions like the left partition pointer in Quick Sort.
    - `i` iterates through the array, similar to how Quick Sort scans elements for swapping.

    ### 3. In-Place Rearrangement
    Like Quick Sort’s partitioning step, this algorithm operates **in-place** without needing extra space, making it space-efficient.

    ### Key Difference
    - **Quick Sort** fully sorts the array.
    - **This function** only partitions the array to move all zeros to the end, preserving the relative order of non-zero elements.
    '''
    #1/20/2025 my solution 
    def moveZeroes_mine(self, nums: List[int]) -> None:
            '''
            my try doing pusedo code I need work on understanding the logic of the problem so I can write the code
            zeroes = len(nums)zero_count-1
            loop in the range of length of the list
            maybe do a while loop and say while index < non_count
            
            
            for i in nums:
            if i !=0 and non_zero_count != non_zero_numbers:
            nums[non_zero_index_count] = i 

            for in range(:len(-non)
            nums[index]= 0 
            '''
            zero_count = nums.count(0)
            non_zero_numbers = (len(nums) - zero_count) -1 
            non_zero_index_place = 0
            for num in nums:
                if num !=0 and non_zero_index_place <= non_zero_numbers:
                    nums[non_zero_index_place] = num 
                    non_zero_index_place+=1
            for index in range(non_zero_numbers+1,len(nums)):
                nums[index] = 0

'''
moveZeroes_optimized explanation
Explanation of Steps:
Initialize j:

Start with j = 0, which points to the position where the next non-zero element should go.
Iterate with i:

For each element in the array (nums[i]):
If it's non-zero, swap it with nums[j] (even if i == j, it still works correctly).
Increment j to point to the next position for a non-zero element.
Result:

After the loop, all non-zero elements are shifted to the front, and the rest of the array (from j onward) consists of zeros.
Example Walkthrough
Input: nums = [0, 1, 0, 3, 12]

Initial State: nums = [0, 1, 0, 3, 12], j = 0
Step 1 (i = 0): nums[0] = 0 → Do nothing.
Step 2 (i = 1): nums[1] = 1 → Swap nums[1] with nums[0], increment j.
Result: nums = [1, 0, 0, 3, 12], j = 1.
Step 3 (i = 2): nums[2] = 0 → Do nothing.
Step 4 (i = 3): nums[3] = 3 → Swap nums[3] with nums[1], increment j.
Result: nums = [1, 3, 0, 0, 12], j = 2.
Step 5 (i = 4): nums[4] = 12 → Swap nums[4] with nums[2], increment j.
Result: nums = [1, 3, 12, 0, 0], j = 3.
Output: nums = [1, 3, 12, 0, 0]
'''
# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Mixed zeros and non-zeros
    nums1 = [0, 1, 0, 3, 12]
    solution.moveZeroes_optimized(nums1)
    print("Test Case 1:", nums1, "Passed" if nums1 == [1, 3, 12, 0, 0] else "Failed")
    assert nums1 == [1, 3, 12, 0, 0]
    # Expected Output: [1, 3, 12, 0, 0]

    # Test Case 2: All zeros
    nums2 = [0, 0, 0, 0]
    solution.moveZeroes_optimized(nums2)
    print("Test Case 2:", nums2, "Passed" if nums2 == [0, 0, 0, 0] else "Failed")
    assert nums2 == [0, 0, 0, 0]
    # Expected Output: [0, 0, 0, 0]

    # Test Case 3: No zeros
    nums3 = [1, 2, 3, 4]
    solution.moveZeroes_optimized(nums3)
    print("Test Case 3:", nums3, "Passed" if nums3 == [1, 2, 3, 4] else "Failed")
    assert nums3 == [1, 2, 3, 4]
    # Expected Output: [1, 2, 3, 4]

    # Test Case 4: Single zero
    nums4 = [0]
    solution.moveZeroes_optimized(nums4)
    print("Test Case 4:", nums4, "Passed" if nums4 == [0] else "Failed")
    assert nums4 == [0]
    # Expected Output: [0]

    # Test Case 5: Single non-zero
    nums5 = [1]
    solution.moveZeroes_optimized(nums5)
    print("Test Case 5:", nums5, "Passed" if nums5 == [1] else "Failed")
    assert nums5 == [1]
    # Expected Output: [1]