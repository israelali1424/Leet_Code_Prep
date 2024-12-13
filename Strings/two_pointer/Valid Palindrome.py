'''
Valid Palindrome
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.
'''
# umpire 
'''
understnad 
this a string question 
want check if a a sting is spelled the same way going forward as it is going backwords 
you should remove the space when checking
input will only contain alpha chachters
# match 
this a string question 
2 pointer question

# plan 
s = "race car" 

remove space with replace function 
s= "racecar" 
     begin = {0:r} 
     end =  {7:r}
     begin +1 , end -1 
     begin = {2:a}
     end = {6:a}
     begin= {3:c}
     end = {5:c}
     begin = {4}
     end=4 
     the condtion would they the are equal to each like  while s[begin] == s[end]:  
     
    
begin = 0
end = len(s)-1
while loop while end >= begin (not sure if condtion is right)
if s[end]== s[begin]
 begin+=1
 end -=1 
else:
    return false 
return true 
'''
# broken Solution
class broke_Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove spaces from s
        s = s.replace(" ","")
        begin = s[0]
        end = len(s)-1
        while s[begin] == s[end]:
            if s[begin] == s[end]: 
                end-=1
                begin+=1
            else:
                return False
        return True
    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Checks if a given string is a palindrome considering only alphanumeric characters
        and ignoring cases.
        """
        # Initialize left and right pointers at the start and end of the string
        l, r = 0, len(s) - 1

        # Iterate while the left pointer is less than the right pointer
        while l < r:
            # Move the left pointer to the right until an alphanumeric character is found
            while l < r and not self.alphaNum(s[l]):
                l += 1
            
            # Move the right pointer to the left until an alphanumeric character is found
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            
            # Compare the characters at the left and right pointers (ignoring case)
            if s[l].lower() != s[r].lower():
                return False  # If they don't match, it's not a palindrome
            
            # Move both pointers towards the center
            l, r = l + 1, r - 1

        # If all characters matched, it's a palindrome
        return True

    def alphaNum(self, c: str) -> bool:
        """
        Checks if a character is alphanumeric (a-z, A-Z, or 0-9).
        """
        return (
            'A' <= c <= 'Z' or  # Check if the character is an uppercase letter
            'a' <= c <= 'z' or  # Check if the character is a lowercase letter
            '0' <= c <= '9'     # Check if the character is a digit
        )

        
    def isPalindrome_quick(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        s = ''.join(char.lower() for char in s if char.isalnum())
        
        # Check if the modified string is a palindrome
        begin, end = 0, len(s) - 1
def test_isPalindrome():
    solution = Solution()
    
    # Test case 1: Palindrome with special characters and mixed case
    assert solution.isPalindrome("A man, a plan, a canal: Panama") == True, "Test case 1 failed"

    # Test case 2: Not a palindrome
    assert solution.isPalindrome("race a car") == False, "Test case 2 failed"

    # Test case 3: Empty string (considered a palindrome)
    assert solution.isPalindrome("") == True, "Test case 3 failed"

    # Test case 4: String with only spaces
    assert solution.isPalindrome("     ") == True, "Test case 4 failed"

    # Test case 5: Single character (considered a palindrome)
    assert solution.isPalindrome("a") == True, "Test case 5 failed"

    # Test case 6: Palindrome with numbers and letters
    assert solution.isPalindrome("12321") == True, "Test case 6 failed"

    # Test case 7: Palindrome ignoring case
    assert solution.isPalindrome("No lemon, no melon") == True, "Test case 7 failed"

    # Test case 8: String with only special characters (should be considered a palindrome)
    assert solution.isPalindrome("!!!") == True, "Test case 8 failed"

    # Test case 9: Long palindrome string
    assert solution.isPalindrome("Able was I, I saw Elba") == True, "Test case 9 failed"

    # Test case 10: Non-palindromic string with special characters
    assert solution.isPalindrome("Hello, world!") == False, "Test case 10 failed"

    print("All test cases passed!")

# Run the test cases
test_isPalindrome()

    

            
            
        