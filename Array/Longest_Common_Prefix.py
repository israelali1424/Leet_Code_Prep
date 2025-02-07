'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
2/1/2025
# I could not sloe this question my anwer as all the way wrong


from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # Handle edge case: empty list
            return ""
        
        # Find the length of the shortest string in the list
        min_length = float('inf')
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)
        
        i = 0  # Index tracker for characters in the prefix
        while i < min_length:  # Iterate up to the shortest string length
            for s in strs:  
                if s[i] != strs[0][i]:  # If any character differs, return the prefix found so far
                    return strs[0][:i]
            i += 1  # Move to the next character
        
        return strs[0][:min_length]  # Return the full prefix if all characters match


# My soultion 
class SolutionBroke:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #max_prefix = len(strs)
        if len(strs) == 1:
            return strs[0]
        max_prefix = []
        for i in range(0,len(strs)-1):
            str_index =0
            curr_prefix= []
            while str_index  <= len(strs[i])-1 and  strs[i][str_index] == strs[i+1][str_index]:
                print(strs[i][str_index])
                curr_prefix.append(strs[i][str_index])
                str_index+=1
            
            if len(curr_prefix) == len(max_prefix):
                max_prefix = curr_prefix
        return "".join(max_prefix)
        # for i in strs[1::]:
        #     while i 
#Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Regular case with common prefix
    strs1 = ["flower", "flow", "flight"]
    result1 = solution.longestCommonPrefix(strs1)
    print("Test Case 1:", result1, "Passed" if result1 == "fl" else "Failed")
    assert result1 == "fl"
    # Expected Output: "fl"

    # Test Case 2: No common prefix
    strs2 = ["dog", "racecar", "car"]
    result2 = solution.longestCommonPrefix(strs2)
    print("Test Case 2:", result2, "Passed" if result2 == "" else "Failed")
    assert result2 == ""
    # Expected Output: ""

    # Test Case 3: All strings are the same
    strs3 = ["test", "test", "test"]
    result3 = solution.longestCommonPrefix(strs3)
    print("Test Case 3:", result3, "Passed" if result3 == "test" else "Failed")
    assert result3 == "test"
    # Expected Output: "test"
    
    # Test Case 4: Single string in the list
    strs4 = ["single"]
    result4 = solution.longestCommonPrefix(strs4)
    print("Test Case 4:", result4, "Passed" if result4 == "single" else "Failed")
    assert result4 == "single"
    # Expected Output: "single"

    # Test Case 5: Empty list
    strs5 = []
    result5 = solution.longestCommonPrefix(strs5)
    print("Test Case 5:", result5, "Passed" if result5 == "" else "Failed")
    assert result5 == ""
    # Expected Output: ""

    # Test Case 6: Mixed case strings
    strs6 = ["Interstellar", "Internet", "Interval"]
    result6 = solution.longestCommonPrefix(strs6)
    print("Test Case 6:", result6, "Passed" if result6 == "Inter" else "Failed")
    assert result6 == "Inter"
    # Expected Output: "Inter"

    # Test Case 7: Strings with no common prefix
    strs7 = ["apple", "banana", "cherry"]
    result7 = solution.longestCommonPrefix(strs7)
    print("Test Case 7:", result7, "Passed" if result7 == "" else "Failed")
    assert result7 == ""
    # Expected Output: ""

    # Test Case 8: Common prefix with different lengths
    strs8 = ["prefix", "pre", "prefixes"]
    result8 = solution.longestCommonPrefix(strs8)
    print("Test Case 8:", result8, "Passed" if result8 == "pre" else "Failed")
    assert result8 == "pre"
    # Expected Output: "pre"