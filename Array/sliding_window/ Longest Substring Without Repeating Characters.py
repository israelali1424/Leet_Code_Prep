"""
 Longest Substring Without Repeating Characters
Given a string s, find the length of the longest 
substring
 without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
    # implment a sliding window that works but is very slow
    # fist medium problem solved on my own 
    def lengthOfLongestSubstring(self, s: str) -> int:
        long_s = 0
        seen = []
        left =0 
        right = 0
        while right <len(s):
            if s[right] not in seen:
                seen.append(s[right])
                right +=1 
            else: 
                long_s = max(long_s,len(seen))
                seen = []
                left+=1 
                right = left 
        return max(long_s,len(seen))
   
    def lengthOfLongestSubstring_optimized(self, s: str) -> int:
        long_s = 0  # Variable to store the length of the longest substring without repeating characters
        seen = set()  # A set to keep track of unique characters in the current substring
        left = 0  # Pointer to track the start of the sliding window

        for right in range(len(s)):  # Iterate through the string using the right pointer
            while s[right] in seen:  # If the current character (s[right]) is already in the set (duplicate detected):
                seen.remove(s[left])  # Remove the character at the start of the window (s[left]) from the set
                left += 1  # Move the left pointer to the right to shrink the window

            seen.add(s[right])  # Add the current character (s[right]) to the set
            long_s = max(long_s, right - left + 1)  # Update the maximum length of the substring

        return long_s  # Return the length of the longest substring


# brute force solution
    def lengthOfLongestSubstring_brute_force(self, s: str) -> int:
        long_s = 0
        
        for i in range(len(s)):
            seen = set()
            for j in range(i, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                else:
                    break  # Stop the inner loop if a duplicate is found
            long_s = max(long_s, len(seen))
        
        return long_s
    
# Importing the Solution class
solution = Solution()

# Test Case 1: Regular string with repeating characters
print("Test Case 1:", solution.lengthOfLongestSubstring("abcabcbb"))
# Expected Output: 3

# Test Case 2: String with all unique characters
print("Test Case 2:", solution.lengthOfLongestSubstring("abcdef"))
# Expected Output: 6

# Test Case 3: String with all identical characters
print("Test Case 3:", solution.lengthOfLongestSubstring("aaaaaa"))
# Expected Output: 1

# Test Case 4: Empty string
print("Test Case 4:", solution.lengthOfLongestSubstring(""))
# Expected Output: 0

# Test Case 5: String with spaces
print("Test Case 5:", solution.lengthOfLongestSubstring("a b c a b c"))
# Expected Output: 3

# Test Case 6: String with special characters
print("Test Case 6:", solution.lengthOfLongestSubstring("!@#$$%^&*()"))
# Expected Output: 7

# Test Case 7: String with numbers and letters
print("Test Case 7:", solution.lengthOfLongestSubstring("123abc123"))
# Expected Output: 6

# Test Case 8: Long string with mixed characters
print("Test Case 8:", solution.lengthOfLongestSubstring("pwwkew"))
# Expected Output: 3

1/30/2025
# Works for only 409 of 700 test cases 
class Solution_Two:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        right = 0
        seen = set()
        
        while right < len(s):  # Corrected loop condition
            if s[right] not in seen:
                seen.add(s[right])
            else:
                max_len = max(max_len, len(seen))  
                left = right  # Reset left to right
                seen = set()  # Reset seen set
                seen.add(s[right])  # Add current character

            right += 1  
        
        max_len = max(max_len, len(seen))  # Final check for the max length
        return max_len
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        right = 0
        seen = {}
        
        while right < len(s):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1
            
            seen[s[right]] = right
            max_len = max(max_len, right - left + 1)
            right += 1
        
        return max_len