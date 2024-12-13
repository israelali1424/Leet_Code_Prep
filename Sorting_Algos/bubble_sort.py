'''
## How Bubble Sort Works:
1. Compare adjacent elements.
2. Swap them if they are in the wrong order.
3. Repeat the process for the next pair of elements.
4. Continue this process for multiple passes until no swaps are needed.
'''
from typing import List
# this is navie bubblesort
class Solution():
    #my bubble_sort
    def bubbleSort(self,nums:List[int]) ->List[int] :
        for i in range(0,len(nums)):
            print(nums[i])
            for j in range(i+1,len(nums)):
                if nums[i] > nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        return nums
    
class Solution():
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        feq_dict = {}
        for number in nums:
            if number in feq_dict:
                feq_dict[number] += 1 
            else:
                feq_dict
                
        result = self.bubbleSortFeq(nums,feq_dict)
        return result[0:k-1]
            
    #my bubble_sort
    def bubbleSortFeq(self,nums:List[int],feq_dict) ->List[int] :
        for i in range(0,len(nums)):
            print(nums[i])
            for j in range(i+1,len(nums)):
                if feq_dict[nums[i]] > feq_dict[nums[j]]:
                    temp = feq_dict[nums[i]]
                    nums[i] = feq_dict[nums[j]]
                    nums[j]= temp
        return nums
        


temp = [1,5,3,4,7,4]
sol = Solution()
print(sol.bubbleSort(temp))

def test_bubble_sort():
    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([3, 1, 2, 3, 4, 1], [1, 1, 2, 3, 3, 4]),
        ([7, 7, 7, 7, 7], [7, 7, 7, 7, 7]),
        ([42], [42]),
        ([], []),
        ([-3, -1, -2, 0, 2, 1], [-3, -2, -1, 0, 1, 2]),
    ]

    for i, (input_arr, expected) in enumerate(test_cases):
        sol.bubbleSort(input_arr)
        assert input_arr == expected, f"Test case {i+1} failed: {input_arr} != {expected}"
    print("All test cases passed!")

test_bubble_sort()
