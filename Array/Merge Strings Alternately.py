'''
1768. Merge Strings Alternately
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
'''
class Solution:
    # my code that works
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        word1_len= len word-1
        word2_len = len(word)2-1
        max_leb(
        index = 0
        result = ""
        while index <= max:
        if index <= word1len and word2len:
        result += word1[i]+word2[index]
        elif index > word1_len and <=
        word2len:
        result += word_2[index]
        else
        result result += word1[index]
        result
        while loop or range 
        '''
        result = ""
        index =0 
        len_word1= len(word1)-1
        len_word2= len(word2)-1
        max_len = max(len_word2,len_word1)

        #while index <= max_len
        for index in range(0,max_len+1):
            if index <= len_word1 and  index <= len_word2:
                result += word1[index]+ word2[index]
            elif index > len_word1 and index <=len_word2:
                result += word2[index]
            else:
                result += word1[index]
        return result
'''
**Time Complexity**: \(O(n + m)\), where \(n\) is the length of 
`word1` and \(m\) is the length of `word2`.
This is because the loop iterates up to \( \text{max}(n, m) \), and string concatenation 
in Python takes linear time relative 
to the length of the resulting string.

**Space Complexity**: \(O(n + m)\), since the `result` string grows to hold the combined characters from `word1` and `word2`.
'''




# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Both words of equal length
    print("Test Case 1:", solution.mergeAlternately("abc", "def"))
    # Expected Output: "adbecf"

    # Test Case 2: First word longer than second
    print("Test Case 2:", solution.mergeAlternately("abcd", "ef"))
    # Expected Output: "aebfcdd"

    # Test Case 3: Second word longer than first
    print("Test Case 3:", solution.mergeAlternately("ab", "cdef"))
    # Expected Output: "acbdef"

    # Test Case 4: One word is empty
    print("Test Case 4:", solution.mergeAlternately("", "xyz"))
    # Expected Output: "xyz"

    # Test Case 5: Both words are empty
    print("Test Case 5:", solution.mergeAlternately("", ""))
    # Expected Output: ""

    # Test Case 6: Single character words
    print("Test Case 6:", solution.mergeAlternately("a", "b"))
    # Expected Output: "ab"

    # Test Case 7: First word is empty
    print("Test Case 7:", solution.mergeAlternately("", "abc"))
    # Expected Output: "abc"

    # Test Case 8: Second word is empty
    print("Test Case 8:", solution.mergeAlternately("abc", ""))
    # Expected Output: "abc"