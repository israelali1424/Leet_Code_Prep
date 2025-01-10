'''
150. Evaluate Reverse Polish Notation
Solved
Medium
Topics
Companies
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22'''
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = 0
        for char in tokens: 
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(b - a )
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                 a,b = stack.pop(), stack.pop()
                 stack.append(int(b / a ))
                
            else:
                stack.append(int(char))
                  
        return stack.pop()

# Importing the Solution class
solution = Solution()

# Test Case 1: Basic operations
print("Test Case 1:", solution.evalRPN(["2", "1", "+", "3", "*"]))
# Expected Output: 9

# Test Case 2: Division and addition
print("Test Case 2:", solution.evalRPN(["4", "13", "5", "/", "+"]))
# Expected Output: 6

# Test Case 3: Complex expression
print("Test Case 3:", solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
# Expected Output: 22

# Test Case 4: Single number
print("Test Case 4:", solution.evalRPN(["42"]))
# Expected Output: 42

# Test Case 5: Negative result
print("Test Case 5:", solution.evalRPN(["2", "3", "-"]))
# Expected Output: -1

# Test Case 6: Multiple operations
print("Test Case 6:", solution.evalRPN(["5", "1", "2", "+", "4", "*", "+", "3", "-"]))
# Expected Output: 14

# Test Case 7: Division resulting in zero
print("Test Case 7:", solution.evalRPN(["4", "2", "/", "2", "/"]))
# Expected Output: 1

# Test Case 8: Large numbers
print("Test Case 8:", solution.evalRPN(["100", "200", "+", "2", "/"]))
# Expected Output: 150