'''
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
'''
# this a brute force solution that is two slow to pass leetcode 
class BruteForceSolution:
    def longestPalindrome(self, s: str) -> str:
        substrings = []
        max_pal = ""
        for i in range(0,len(s)):
            current_substring = ""
            
            for j in range(i,len(s)):
                current_substring +=  s[j]
                substrings.append(current_substring)
                if self.isPalindrome(current_substring) and len(max_pal) < len(current_substring):
                    max_pal =  current_substring
        print(substrings)
        return max_pal
    
    
    def isPalindrome(self, s: str) -> bool:
        s = self.cleanString(s)
        # create two pointers one at the end of a string and one at begin of astring 
        # compare the .lower() of each char if the values are the same move to the next char
        # if the are diffrent return False 
        # return true if the loop complete 
        start = 0
        end = len(s) -1
        while start < end:
          
            if s[start].lower() != s[end].lower():
                return False 
            start+=1
            end -=1 
        return True
    

    def cleanString(self,s:str)-> str:
        result = ""
        for char in s:
            if char.isalpha() or char.isnumeric():
                result+= char 
        return result 
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pal = ""
        for i in range(len(s)):
            # Check odd-length palindromes
            odd_pal = self.expandAroundCenter(i, i,s)
            # Check even-length palindromes
            even_pal = self.expandAroundCenter(i, i + 1,s)
            # Update max_pal if a longer palindrome is found
            max_pal = max(max_pal, odd_pal, even_pal, key=len)

        return max_pal
    
    def expandAroundCenter(self, left: int, right: int,s:str) -> str:
        # Expand as long as the characters match and indices are valid
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the longest palindromic substring for this center
        return s[left + 1:right]

        if not s or len(s) == 1:
            return s

 # Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: General case with a long palindrome
    print(solution.longestPalindrome("babad"))  # Expected: "bab" or "aba"
    
    # Test case 2: Single-character string
    print(solution.longestPalindrome("a"))  # Expected: "a"
    
    # Test case 3: Entire string is a palindrome
    print(solution.longestPalindrome("racecar"))  # Expected: "racecar"
    
    # Test case 4: String with no repeating characters
    print(solution.longestPalindrome("abcde"))  # Expected: Any single character like "a", "b", etc.
    
    # Test case 5: String with multiple palindromes of the same length
    print(solution.longestPalindrome("cbbd"))  # Expected: "bb"
    
    # Test case 6: Empty string
    print(solution.longestPalindrome(""))  # Expected: ""
    
    # Test case 7: Even-length palindrome
    print(solution.longestPalindrome("aabbccbbaa"))  # Expected: "aabbccbbaa"
    
    # Test case 8: String with spaces
    print(solution.longestPalindrome("a man a plan a canal panama"))  # Expected: "a man a plan a canal panama" (if considering spaces as part of palindrome)