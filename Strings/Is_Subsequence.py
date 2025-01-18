'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
'''

class Solution:
    # own version  that workd 
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        result list =  and the join the list at the end to get a string

        index var and check if

        using a for loop long word :
        in that loop if char is ==[shortword[index]
        if index >= len(short_word)
        result.append[shortword[index].
        index+=1

        join the result
        and compare shortword to result
        '''
        result = []
        index = 0 
        for char_t in t:
            if index <= len(s)-1 and s[index] == char_t:
                result.append(s[index])
                index+=1 
            elif index > len(s):
                break 

        result = "".join(result)
        return result == s 
    # own version that is optimized 
    def isSubsequence_two(self, s: str, t: str) -> bool:
        result = []
        index = 0 
        if not s and t:
            return True
        if not t and s:
            return False 
        for char_t in t:
            if index <= len(s)-1 and s[index] == char_t:
                result.append(s[index])
                index+=1 
            elif index > len(s):
                break 

        result = "".join(result)
        return result == s 
    

if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: s is a subsequence of t
    s1, t1 = "abc", "ahbgdc"
    result1 = solution.isSubsequence_two(s1, t1)
    print("Test Case 1:", result1, "Passed" if result1 == True else "Failed")
    assert result1 == True
    # Expected Output: True

    # Test Case 2: s is not a subsequence of t
    s2, t2 = "axc", "ahbgdc"
    result2 = solution.isSubsequence_two(s2, t2)
    print("Test Case 2:", result2, "Passed" if result2 == False else "Failed")
    assert result2 == False
    # Expected Output: False

    # Test Case 3: s is empty
    s3, t3 = "", "ahbgdc"
    result3 = solution.isSubsequence_two(s3, t3)
    print("Test Case 3:", result3, "Passed" if result3 == True else "Failed")
    assert result3 == True
    # Expected Output: True

    
    # Test Case 4: t is empty
    s4, t4 = "abc", ""
    result4 = solution.isSubsequence_two(s4, t4)
    print("Test Case 4:", result4, "Passed" if result4 == False else "Failed")
    assert result4 == False
    # Expected Output: False

    # Test Case 5: Both s and t are empty
    s5, t5 = "", ""
    result5 = solution.isSubsequence_two(s5, t5)
    print("Test Case 5:", result5, "Passed" if result5 == True else "Failed")
    assert result5 == True
    # Expected Output: True

    # Test Case 6: s is longer than t
    s6, t6 = "abcdef", "abc"
    result6 = solution.isSubsequence_two(s6, t6)
    print("Test Case 6:", result6, "Passed" if result6 == False else "Failed")
    assert result6 == False
    # Expected Output: False

