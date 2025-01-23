'''
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
Easy Question
'''

# My Solution that works 
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        jewel_count = 0

        for rock in stones:
            if rock in jewels:
                jewel_count += 1
        return jewel_count

# Time Complexity: O(n + m), where n is the length of the jewels string and m is the length of the stones string.
# Space Complexity: O(n), where n is the number of unique characters in the jewels string.

# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Regular case with some jewels
    jewels1 = "aA"
    stones1 = "aAAbbbb"
    result1 = solution.numJewelsInStones(jewels1, stones1)
    print("Test Case 1:", result1, "Passed" if result1 == 3 else "Failed")
    assert result1 == 3
    # Expected Output: 3

    # Test Case 2: No jewels in stones
    jewels2 = "z"
    stones2 = "ZZ"
    result2 = solution.numJewelsInStones(jewels2, stones2)
    print("Test Case 2:", result2, "Passed" if result2 == 0 else "Failed")
    assert result2 == 0
    # Expected Output: 0

    # Test Case 3: All stones are jewels
    jewels3 = "abc"
    stones3 = "aabbcc"
    result3 = solution.numJewelsInStones(jewels3, stones3)
    print("Test Case 3:", result3, "Passed" if result3 == 6 else "Failed")
    assert result3 == 6
    # Expected Output: 6

    # Test Case 4: No stones
    jewels4 = "aA"
    stones4 = ""
    result4 = solution.numJewelsInStones(jewels4, stones4)
    print("Test Case 4:", result4, "Passed" if result4 == 0 else "Failed")
    assert result4 == 0
    # Expected Output: 0

    # Test Case 5: No jewels
    jewels5 = ""
    stones5 = "aAAbbbb"
    result5 = solution.numJewelsInStones(jewels5, stones5)
    print("Test Case 5:", result5, "Passed" if result5 == 0 else "Failed")
    assert result5 == 0
    # Expected Output: 0

    # Test Case 6: Mixed case sensitivity
    jewels6 = "aA"
    stones6 = "aAaAaA"
    result6 = solution.numJewelsInStones(jewels6, stones6)
    print("Test Case 6:", result6, "Passed" if result6 == 6 else "Failed")
    assert result6 == 6
    # Expected Output: 6