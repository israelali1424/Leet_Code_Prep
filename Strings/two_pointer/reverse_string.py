'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
'''
from typing import List
#1/20/2025 
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        '''
        
        have one var start and one at back of the list
        have another var start at the front of the list
        while left < right:
        word[left],word[right] = word[right],word[left]

        left +=1
        right +=1

        Easy question sloved in 7 and half minutes
        '''
        left = 0  
        right = len(s) -1 
        while left < right: 
            s[left], s[right] = s[right],s[left]
            left +=1
            right -=1 
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Regular case
    s1 = ["h", "e", "l", "l", "o"]
    solution.reverseString(s1)
    print("Test Case 1:", s1, "Passed" if s1 == ["o", "l", "l", "e", "h"] else "Failed")
    assert s1 == ["o", "l", "l", "e", "h"]
    # Expected Output: ["o", "l", "l", "e", "h"]

    # Test Case 2: Longer string
    s2 = ["H", "a", "n", "n", "a", "h"]
    solution.reverseString(s2)
    print("Test Case 2:", s2, "Passed" if s2 == ["h", "a", "n", "n", "a", "H"] else "Failed")
    assert s2 == ["h", "a", "n", "n", "a", "H"]
    # Expected Output: ["h", "a", "n", "n", "a", "H"]

    # Test Case 3: Single character
    s3 = ["a"]
    solution.reverseString(s3)
    print("Test Case 3:", s3, "Passed" if s3 == ["a"] else "Failed")
    assert s3 == ["a"]
    # Expected Output: ["a"]

    # Test Case 4: Empty list
    s4 = []
    solution.reverseString(s4)
    print("Test Case 4:", s4, "Passed" if s4 == [] else "Failed")
    assert s4 == []
    # Expected Output: []

    # Test Case 5: Palindrome string
    s5 = ["r", "a", "c", "e", "c", "a", "r"]
    solution.reverseString(s5)
    print("Test Case 5:", s5, "Passed" if s5 == ["r", "a", "c", "e", "c", "a", "r"] else "Failed")
    assert s5 == ["r", "a", "c", "e", "c", "a", "r"]
    # Expected Output: ["r", "a", "c", "e", "c", "a", "r"]
