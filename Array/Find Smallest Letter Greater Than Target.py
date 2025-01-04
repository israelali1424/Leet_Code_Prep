'''
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

 

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
Example 3:

Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].
'''
from typing import List 
# my Solution
import math 
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        base = ord(target)
        min_largest = math.inf 
        # do a binary search 
        for letter in letters:
            if ord(letter) > ord(target):
                return letter 
            
# online solution using binary search
# I had the idea to use but did not know how 


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        # If left goes out of bounds, wrap around to the first element
        return letters[left] if left < len(letters) else letters[0]