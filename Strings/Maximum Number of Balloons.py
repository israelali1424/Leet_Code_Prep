'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
'''
#1/21/2025
# my Solution
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # create a dict that has ballons and the count of each letter in the word
        # the get the count letter that could be found in ballon 
        # retunr the min from that count 
        char_count = {"b":1,"a":1,"l":2,"o":2,"n":1}
        char_count_text = {}
        result = [] 

        for char in text:
            if char in char_count and char in char_count_text:
                char_count_text[char]+=1
            elif char in char_count and char not in char_count_text:
                char_count_text[char] = 1 
        for key, value in char_count.items():
            if key in char_count_text:
                val = char_count_text[key] // value 
                result.append(val)
            else: 
                
                return 0

        print(result)
        return min(result)
        
        
#
# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Regular case with one "balloon"
    text1 = "nlaebolko"
    result1 = solution.maxNumberOfBalloons(text1)
    print("Test Case 1:", result1, "Passed" if result1 == 1 else "Failed")
    assert result1 == 1
    # Expected Output: 1

    # Test Case 2: No "balloon" can be formed
    text2 = "leetcode"
    result2 = solution.maxNumberOfBalloons(text2)
    print("Test Case 2:", result2, "Passed" if result2 == 0 else "Failed")
    assert result2 == 0
    # Expected Output: 0

    # Test Case 3: Multiple "balloon" can be formed
    text3 = "loonbalxballpoon"
    result3 = solution.maxNumberOfBalloons(text3)
    print("Test Case 3:", result3, "Passed" if result3 == 2 else "Failed")
    assert result3 == 2
    # Expected Output: 2

    # Test Case 4: Empty string
    text4 = ""
    result4 = solution.maxNumberOfBalloons(text4)
    print("Test Case 4:", result4, "Passed" if result4 == 0 else "Failed")
    assert result4 == 0
    # Expected Output: 0

    # Test Case 5: String with exactly one "balloon"
    text5 = "balloon"
    result5 = solution.maxNumberOfBalloons(text5)
    print("Test Case 5:", result5, "Passed" if result5 == 1 else "Failed")
    assert result5 == 1
    # Expected Output: 1
