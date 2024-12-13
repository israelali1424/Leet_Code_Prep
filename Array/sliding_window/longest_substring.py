
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}  # Dictionary to track seen characters and their last index
        longest_sub_string = ""  # Track the longest unique substring
        left = 0  # Left pointer of the sliding window
        right = 0  # Right pointer of the sliding window
        sub_string = ""  # Current unique substring

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        
        while right < len(s):
            if s[right] not in seen:
                # Add current character to seen and update substring
                seen[s[right]] = right
                sub_string += s[right]
                if len(sub_string) > len(longest_sub_string):
                    longest_sub_string = sub_string
            else:
                # Move left to the character after the previous occurrence of s[right]
                left = seen[s[right]] + 1
                # Update the window and reset seen to only track the new substring
                sub_string = s[left:right + 1]
                seen = {s[i]: i for i in range(left, right + 1)}

            right += 1
        
        return len(longest_sub_string)
    
    
    
class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            '''
            understand
            input is a string with only chacters 
            the string could be empty 
            find longest without duplicate characters
            match 
            sliding window problem 
            plan 
            use a hashmap to count the number of time a value apperars in the list 
            use a string to store the value the logest substring 
            need a current_substring 
            if hash[char] >1: hash = {} current_string= hash[char] 
            start = end 
            else: end+=1 
            return l_substring 
            '''
            seen = {}
            longest_sub_string = ""
            left = 0
            right = 1
            sub_string = ""

            if len(s) == 0: 
                return ""
            elif len(s) == 1:
                s[0]
            while right < len(s):
                if s[left] not in seen:
                    seen[s[left]] = 1
                    sub_string = sub_string + s[left]
                    if sub_string  > longest_sub_string: 
                        longest_sub_string = sub_string
                if s[left] in seen:
                    left = right
                    seen = {}
                    sub_string = s[left]
                right+=1 
            return longest_sub_string



                