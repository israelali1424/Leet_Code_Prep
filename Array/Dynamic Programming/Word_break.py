'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
'''
from typing import List
#2/25/2025
# my solution broke because I did not understand the problem
# I solved if the word from wordDict order 
'''
such as 
Input: s = "leetcode", wordDict = ["leet","code"]
will break 
s =
"bb"
wordDict =
["a","b","bbb","bbbb"]
'''
class Solution_broke:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        create a index called index set to 0 
        create a index for dict called set to 0 rest after every loop 
        for loop in a while loop 
            dictkeyindex= 0 
            while indexstr <= len(str) and dictkeyindex <= len(key):
                if s[indexstr] == word[dictkeyindex]:
                    indexstr+=1
                    dictkey+=1
                else: 
                    return false
            return true 
        # But this good progress 
        '''
        str_index = 0 
        for i in wordDict:
            dictkeyindex = 0 
            while  str_index < len(s) and  dictkeyindex  < len(i):
                if s[str_index] == i[dictkeyindex]:
                    str_index+=1
                    dictkeyindex+=1 
                else: 
                    return False 
        return True
# from claude 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert wordDict to a set for O(1) lookups
        word_set = set(wordDict)
        
        # dp[i] represents whether s[0:i] can be segmented into words from the dictionary
        dp = [False] * (len(s) + 1)
        
        # Empty string is always breakable
        dp[0] = True
        
        # Fill the dp array
        for i in range(1, len(s) + 1):
            for j in range(i):
                # If s[0:j] is breakable and s[j:i] is in the dictionary
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[len(s)]
    
# Test Cases
if __name__ == "__main__":
    solution = Solution_broke()
    
    # Test Case 1: Regular case with valid segmentation
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    result1 = solution.wordBreak(s1, wordDict1)
    print("Test Case 1:", result1, "Passed" if result1 == True else "Failed")
    assert result1 == True
    # Expected Output: True

    # Test Case 2: Valid segmentation with reuse of dictionary words
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    result2 = solution.wordBreak(s2, wordDict2)
    print("Test Case 2:", result2, "Passed" if result2 == True else "Failed")
    assert result2 == True
    # Expected Output: True

    # Test Case 3: No valid segmentation
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    result3 = solution.wordBreak(s3, wordDict3)
    print("Test Case 3:", result3, "Passed" if result3 == False else "Failed")
    assert result3 == False
    # Expected Output: False

    # Test Case 4: Single character string with valid segmentation
    s4 = "a"
    wordDict4 = ["a"]
    result4 = solution.wordBreak(s4, wordDict4)
    print("Test Case 4:", result4, "Passed" if result4 == True else "Failed")
    assert result4 == True
    # Expected Output: True

    # Test Case 5: Single character string with no valid segmentation
    s5 = "b"
    wordDict5 = ["a"]
    result5 = solution.wordBreak(s5, wordDict5)
    print("Test Case 5:", result5, "Passed" if result5 == False else "Failed")
    assert result5 == False
    # Expected Output: False

    # Test Case 6: Empty string
    s6 = ""
    wordDict6 = ["a", "b", "c"]
    result6 = solution.wordBreak(s6, wordDict6)
    print("Test Case 6:", result6, "Passed" if result6 == True else "Failed")
    assert result6 == True
    # Expected Output: True

    # Test Case 7: Large input with valid segmentation
    s7 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict7 = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    result7 = solution.wordBreak(s7, wordDict7)
    print("Test Case 7:", result7, "Passed" if result7 == False else "Failed")
    assert result7 == False
    # Expected Output: False

    # Test Case 8: Large input with valid segmentation
    s8 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict8 = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    result8 = solution.wordBreak(s8, wordDict8)
    print("Test Case 8:", result8, "Passed" if result8 == True else "Failed")
    assert result8 == True
    # Expected Output: True
    
    # Test Case 8: Large input with valid segmentation
    s9= "bb"
    wordDict9= ["a", "aa", "bb", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    result8 = solution.wordBreak(s8, wordDict8)
    print("Test Case 8:", result8, "Passed" if result8 == True else "Failed")
    assert result8 == True
    # Expected Output: True