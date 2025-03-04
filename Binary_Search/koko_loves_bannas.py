
'''
875. Koko Eating Bananas
Solved
Medium
Topics
Companies
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
'''
import math
class Solution():
    def minEatingSpeed(self,piles, h):
        # Binary search range: from 1 to max pile size
        left = 1
        right = max(piles)
        
        # Initialize result variable
        result = right  # Start with maximum possible value
        
        while left <= right:
            mid = (left + right) // 2
            
            # Calculate hours needed to eat all piles at speed 'mid'
            hours_needed = 0
            for pile in piles:
                # Ceiling division: (pile + mid - 1) // mid or math.ceil(pile / mid)
                hours_needed += math.ceil(pile / mid)
                #hours_needed += (pile + mid - 1) // mid
            
            # Check if we can finish within h hours
            if hours_needed <= h:
                # This speed works, but we want to find minimum speed
                result = min(result, mid)
                right = mid - 1  # Try smaller speed
            else:
                # Too slow, need to increase speed
                left = mid + 1
        
        return result
# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Regular case
    piles1 = [3, 6, 7, 11]
    h1 = 8
    result1 = solution.minEatingSpeed(piles1, h1)
    print("Test Case 1:", result1, "Passed" if result1 == 4 else "Failed")
    assert result1 == 4
    # Expected Output: 4

    # Test Case 2: Minimum speed required
    piles2 = [30, 11, 23, 4, 20]
    h2 = 5
    result2 = solution.minEatingSpeed(piles2, h2)
    print("Test Case 2:", result2, "Passed" if result2 == 30 else "Failed")
    assert result2 == 30
   

    
    # Test Case 5: All piles are the same
    piles5 = [1, 1, 1, 1]
    h5 = 4
    result5 = solution.minEatingSpeed(piles5, h5)
    print("Test Case 5:", result5, "Passed" if result5 == 1 else "Failed")
    assert result5 == 1
    # Expected Output: 1

    # Test Case 6: Large number of piles
    piles6 = [1000000000] * 100000
    h6 = 100000000
    result6 = solution.minEatingSpeed(piles6, h6)
    print("Test Case 6:", result6, "Passed" if result6 == 10 else "Failed")
    assert result6 == 10
    # Expected Output: 10