'''
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        '''
        Determine if a given number `num` is a perfect square using binary search.
        '''
        # Initialize the left and right pointers for binary search
        left = 0
        right = num

        # Perform binary search
        while left <= right:
            # Calculate the middle value
            mid = (left + right) // 2
            # Square the middle value
            sq = mid * mid

            # Check if the squared value equals `num`
            if sq == num:
                return True  # `num` is a perfect square
            
            # If the squared value is less than `num`, search the right half
            elif sq < num:
                left = mid + 1
            
            # If the squared value is greater than `num`, search the left half
            else:
                right = mid - 1

        # If no perfect square is found, return False
        return False
