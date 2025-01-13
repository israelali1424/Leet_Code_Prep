'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
'''
class MinStack1:
    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        # Update minStack with the minimum of the current value or the last minimum value
        if self.minStack:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)
    
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minStack.pop()
    
    def top(self) -> int:
        return self.stack[-1] if self.stack else None
    
    def getMin(self) -> int:
        return self.minStack[-1] if self.minStack else None
import math 

# Min stack without using the built in .pop
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []  # Helper stack to track minimum values

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            removed_value = self.stack[-1]
            self.stack = self.stack[:-1]  # Manually remove the last element
            if self.min_stack and removed_value == self.min_stack[-1]:
                self.min_stack = self.min_stack[:-1]

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None


