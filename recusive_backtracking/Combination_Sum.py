'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
'''
#1/25/2025 I did not understand the question so I had to look at the solution. I still
# do not understand the question. I will have to come back to this question to 
# review the logic. Solution via neetcode
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # This will hold all the unique combinations that sum to the target
        res = []

        # Depth-first search (DFS) helper function
        def dfs(i, cur, total):
            """
            i: Index of the current candidate being considered
            cur: Current combination of numbers
            total: Sum of the numbers in the current combination
            """
            # Base case: If the current total matches the target, add the combination to the result
            if total == target:
                res.append(cur.copy())  # Append a copy of the current combination
                return
            
            # If we've gone beyond the list of candidates or exceeded the target, backtrack
            if i >= len(candidates) or total > target:
                return
            
            # Include the current candidate and recurse
            cur.append(candidates[i])  # Choose the current candidate
            dfs(i, cur, total + candidates[i])  # Continue with the current candidate
            cur.pop()  # Backtrack: remove the last chosen candidate
            
            # Exclude the current candidate and move to the next
            dfs(i + 1, cur, total)  # Skip the current candidate

        # Start DFS with the first candidate
        dfs(0, [], 0)
        return res
