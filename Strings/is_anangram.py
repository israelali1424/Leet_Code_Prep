'''
Valid Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_one = {}
        word_two = {}
        if len(s) != len(t):
            return False
        
        for i in range(0,len(s)):
            if s[i] not in word_one:
                word_one[s[i]] = 1
            else:
                word_one[s[i]] +=1 

        for i in range(0,len(s)):
             if t[i] not in word_two:
                word_two[t[i]] = 1
             else:
                word_two[t[i]] +=1
            
        return word_one == word_two
    
    
class Solution_Fast:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}  # Dictionaries to store character counts

        # Count characters in both strings
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Compare character counts of both dictionaries
        return countS == countT
solution = Solution()

# Test case 1: Valid anagram
print(solution.isAnagram("anagram", "nagaram"))  # Expected output: True

# Test case 2: Invalid anagram
print(solution.isAnagram("rat", "car"))  # Expected output: False

# Test case 3: Empty strings
print(solution.isAnagram("", ""))  # Expected output: Tr