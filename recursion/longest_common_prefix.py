''''
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
# The first version is my broken brute force version, the second version is the chatgpt modfited version and the
# one was create fully by chatgpt 
# This Python file contains three implementations of the Longest Common Prefix problem.
# It also explains why the first solution does not work as intended, why the second solution works,
# and why the recursive solution is often the best choice.
# The fouth Solution is from neetcode 

from typing import List

class Solution:
    # Attempt 1: Initial (Incorrect) Solution
    '''
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = strs[0]
        start = 1
        for string in range(start, len(strs)):
            for index, char in enumerate(strs[string]):
                current_prefix = ""
                if strs[string][index] == longest_prefix[index]:
                    current_prefix += strs[string][index]
                else:
                    if longest_prefix > current_prefix:
                        longest_prefix = current_prefix
                    continue

        return longest_prefix
    '''
    # Why this doesn't work:
    # - `current_prefix` is reset in every inner loop iteration, so it only contains a single character at a time.
    # - The comparison `longest_prefix > current_prefix` doesn't make sense in this context.
    # - It doesn't properly find and update the common prefix between strings.
    # - Edge cases (e.g., empty list, mismatched strings) are not handled.

    # Solution 2: Iterative Approach (Correct and Efficient)
    def iterativeLongestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""  # Handle the edge case of an empty list

        longest_prefix = strs[0]  # Start with the first string as the prefix

        for i in range(1, len(strs)):
            current_string = strs[i]
            temp_prefix = ""

            # Find the common prefix between `longest_prefix` and `current_string`
            for index in range(min(len(longest_prefix), len(current_string))):
                if longest_prefix[index] == current_string[index]:
                    temp_prefix += longest_prefix[index]
                else:
                    break  # Stop as soon as characters differ

            # Update the longest prefix
            longest_prefix = temp_prefix

            # Early exit if there's no common prefix
            if not longest_prefix:
                break

        return longest_prefix

    # Solution 3: Recursive Approach (Elegant and Modular)
    def recursiveLongestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""  # Handle the edge case of an empty list

        # Helper function to find the common prefix between two strings
        def commonPrefix(str1: str, str2: str) -> str:
            min_length = min(len(str1), len(str2))
            for i in range(min_length):
                if str1[i] != str2[i]:
                    return str1[:i]  # Return the common prefix up to the mismatch
            return str1[:min_length]  # If one string is a prefix of the other

        # Recursive function to find the longest common prefix in the list
        def findLCP(start: int, end: int) -> str:
            # Base case: single string
            if start == end:
                return strs[start]

            # Divide the list into two halves
            mid = (start + end) // 2
            left_lcp = findLCP(start, mid)  # Longest common prefix of left half
            right_lcp = findLCP(mid + 1, end)  # Longest common prefix of right half

            # Merge the results
            return commonPrefix(left_lcp, right_lcp)

        # Start recursion over the entire list
        return findLCP(0, len(strs) - 1)
    
class Neet_Code_Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""  # Initialize result as an empty string
        for i in range(len(strs[0])):  # Loop through each character in the first string
            for s in strs:  # Loop through each string in the list
                if i == len(s) or s[i] != strs[0][i]:  # If character is not common or string is shorter
                    return res  # Return the result (common prefix) found so far
            res += strs[0][i]  # Add the character to the result if it's common across all strings
        return res


# Why Recursive is the Best Choice in Some Scenarios:
# - The recursive approach leverages divide-and-conquer, breaking the problem into smaller subproblems.
# - It is elegant and modular, making it easy to understand and extend.
# - For large datasets, it can be more efficient by reducing redundant comparisons.
#
# Complexity Analysis:
# - Iterative and Recursive approaches both have a time complexity of O(S), where S is the total number of characters in all strings.
# - The recursive approach has additional space complexity due to the call stack (O(log n) for balanced splits).

# Example Usage:
if __name__ == "__main__":
    solution = Solution()

    # Test case for Iterative Approach
    print("Iterative Solution:", solution.iterativeLongestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"

    # Test case for Recursive Approach
    print("Recursive Solution:", solution.recursiveLongestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
