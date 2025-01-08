'''
The Fibonacci sequence is the series of numbers where each number is the sum of the two preceding numbers. 
For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, …
return the value of the Fibonacci sequence for the nth number
'''
class Solution:
   def fib(self,n:int):
        if n ==0:
            return 0
        if n == 1:
            return 1 
        return self.fib(n-1) + self.fib(n-2)
s= Solution()
# 🛠️ Optimized Fibonacci with Memoization
# Memoization stores previously computed results in a dictionary to avoid redundant calculations.
class Solution:
    def __init__(self):
        self.memo = {}  # Dictionary to store already computed results
    
    def fib(self, n: int) -> int:
        if n in self.memo:  # Check if result is already in memo
            return self.memo[n]
        
        if n == 0:  # Base Case 1
            return 0
        if n == 1:  # Base Case 2
            return 1
        
        # Store result in memo before returning
        self.memo[n] = self.fib(n-1) + self.fib(n-2)
        return self.memo[n]
print(s.fib(4))
