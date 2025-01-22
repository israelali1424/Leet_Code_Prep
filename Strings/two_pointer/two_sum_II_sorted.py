'''
Two Integer Sum II
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1)
O(1) additional space.

Example 1:

Input: numbers = [1,2,3,4], target = 3

Output: [1,2]
Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

'''
from typing import List
#  my solution 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1 
        while end >start:
            if numbers[start] + numbers[end] > target:
                end-=1 
            elif numbers[start] + numbers[end] < target:
                start+=1 
            else: 
                return [start+1,end+1]
            
# faster solution from online 
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start =0
        end = len(numbers) -1
        while numbers[start] + numbers[end]  != target:
            if numbers[start] + numbers[end] > target:
                end-=1 
            else:
                start+=1 
    
        return [start+1,end+1]
    
class SolutionThree:
    # 1/20/2025 20 minutes I got logic right but kept test cases wrong because I was not considering the list being sorted I did not fully read the question
    # and was forget to add one to the index
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        leavge the list being sorted
        left = 0
        right = len  nums -1
        while left < right:
        sum = numsleft + numsright]
        if   sum == target:
        return [ left, right]
        if sum > target:
        right -1
        else:
        left +1
        '''
        left = 0 
        right = len(numbers) -1 
        while left < right:
            sum_val = numbers[left]+ numbers[right]
            if sum_val == target:
                return [left+1,right+1]
            elif sum_val > target:
                right -=1
            else: 
                left +=1 

    
# Test case
def main():
    solution = Solution()
    
    # Example test case 1
    numbers1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: numbers={numbers1}, target={target1}")
    print(f"Output: {solution.twoSum(numbers1, target1)}")  # Expected Output: [1, 2]
    
    # Additional test case 2
    numbers2 = [1, 3, 4, 5, 6, 8, 11]
    target2 = 10
    print(f"Input: numbers={numbers2}, target={target2}")
    print(f"Output: {solution.twoSum(numbers2, target2)}")  # Expected Output: [4, 5]

    # Additional test case 3
    numbers3 = [1, 2, 3, 4, 4]
    target3 = 8
    print(f"Input: numbers={numbers3}, target={target3}")
    print(f"Output: {solution.twoSum(numbers3, target3)}")  # Expected Output: [4, 5]

if __name__ == "__main__":
    main()
