# my brute fore broken version 
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
            for j in range(i+1,len(nums)): # this the reason it breaks 
                if feq_dict[nums[i]] > feq_dict[nums[j]]:
                    temp = feq_dict[nums[i]]
                    nums[i] = feq_dict[nums[j]]
                    nums[j]= temp
        return nums
    '''
    In the broken version, the code incorrectly swaps the frequencies instead of the elements. The temp variable holds the frequency value, and the code attempts to assign frequencies to nums[i] and nums[j]:
    '''
    
# brute force working version 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Build the frequency dictionary
        freq_dict = {}
        for number in nums:
            if number in freq_dict:
                freq_dict[number] += 1
            else:
                freq_dict[number] = 1

        print(freq_dict)  # This shows the frequency of each number
        result = self.bubbleSortFeq(list(freq_dict.keys()), freq_dict)
        print(result)  # This shows the sorted numbers by frequency
        return result[:k]

    # Bubble Sort to sort elements by their frequency
    def bubbleSortFeq(self, nums: List[int], freq_dict: dict) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):  # Start from i+1 to compare adjacent pairs
                if freq_dict[nums[i]] < freq_dict[nums[j]]:  # Compare frequencies
                    # Swap the numbers, not the frequencies
                    nums[i], nums[j] = nums[j], nums[i]
        return nums
