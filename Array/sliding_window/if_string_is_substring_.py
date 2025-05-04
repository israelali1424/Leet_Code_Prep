class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create a counter for magazine characters
        char_counts = {}
        
        # Count each character in magazine
        for char in magazine:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        
        # Check if we can form ransomNote
        for char in ransomNote:
            # If character doesn't exist or we've used all instances
            if char not in char_counts or char_counts[char] == 0:
                return False
            # Use one occurrence of this character
            char_counts[char] -= 1
        
        return True

# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Regular case where ransomNote can be constructed
    ransomNote1 = "a"
    magazine1 = "bca"
    result1 = solution.canConstruct(ransomNote1, magazine1)
    print("Test Case 1:", result1, "Passed" if result1 == True else "Failed")
    assert result1 == True
    # Expected Output: True

    # Test Case 2: Regular case where ransomNote cannot be constructed
    ransomNote2 = "aa"
    magazine2 = "ab"
    result2 = solution.canConstruct(ransomNote2, magazine2)
    print("Test Case 2:", result2, "Passed" if result2 == False else "Failed")
    assert result2 == False
    # Expected Output: False

    # Test Case 3: Empty ransomNote
    ransomNote3 = ""
    magazine3 = "anything"
    result3 = solution.canConstruct(ransomNote3, magazine3)
    print("Test Case 3:", result3, "Passed" if result3 == True else "Failed")
    assert result3 == True
    # Expected Output: True

    # Test Case 4: Empty magazine
    ransomNote4 = "a"
    magazine4 = ""
    result4 = solution.canConstruct(ransomNote4, magazine4)
    print("Test Case 4:", result4, "Passed" if result4 == False else "Failed")
    assert result4 == False
    # Expected Output: False

    # Test Case 5: Both ransomNote and magazine are empty
    ransomNote5 = ""
    magazine5 = ""
    result5 = solution.canConstruct(ransomNote5, magazine5)
    print("Test Case 5:", result5, "Passed" if result5 == True else "Failed")
    assert result5 == True
    # Expected Output: True

    # Test Case 6: Large ransomNote with sufficient characters in magazine
    ransomNote6 = "abcabc"
    magazine6 = "aabbccabc"
    result6 = solution.canConstruct(ransomNote6, magazine6)
    print("Test Case 6:", result6, "Passed" if result6 == True else "Failed")
    assert result6 == True
    # Expected Output: True

    # Test Case 7: Large ransomNote with insufficient characters in magazine
    ransomNote7 = "abcabcabc"
    magazine7 = "aabbcc"
    result7 = solution.canConstruct(ransomNote7, magazine7)
    print("Test Case 7:", result7, "Passed" if result7 == False else "Failed")
    assert result7 == False
    # Expected Output: False

    # Test Case 8: Case with repeated characters
    ransomNote8 = "aaa"
    magazine8 = "aaaa"
    result8 = solution.canConstruct(ransomNote8, magazine8)
    print("Test Case 8:", result8, "Passed" if result8 == True else "Failed")
    assert result8 == True
    # Expected Output: True