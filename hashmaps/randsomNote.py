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
