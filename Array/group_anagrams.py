'''
Given an array of strings strs, group the 
anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using a dictionary is more efficient than a list
        anagram_dict = {}
        
        for word in strs:
            # Sort the word to use as key - all anagrams will have the same sorted string
            sorted_word = ''.join(sorted(word))
            
            # Add to existing group or create new group
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
        
        # Convert dictionary values to list
        return list(anagram_dict.values())
    
    
    
    
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the input array
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two-pointer approach
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the second and third elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to simplify the two-pointer approach
        result = set()  # Use a set to avoid duplicate triplets

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements for `i`

            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif current_sum < 0:
                    left += 1  # Move the left pointer to increase the sum
                else:
                    right -= 1  # Move the right pointer to decrease the sum

        # Convert the set of tuples to a list of lists
        return [list(triplet) for triplet in result]
