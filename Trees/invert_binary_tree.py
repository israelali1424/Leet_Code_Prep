# Invert Binary Tree - Test Cases

"""
## Problem Description
Given the root of a binary tree, invert the tree, and return its root. Inverting a binary tree means swapping the left and right subtrees of every node.

## Example Input and Output

### Example 1:
**Input:**
    4
   / \
  2   7
 / \ / \
1  3 6  9

**Output:**
    4
   / \
  7   2
 / \ / \
9  6 3  1

**Test Case Code:**
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
result = invertTree(root)
"""
import unittest
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp
        #one line
        #root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
    def invertTreebfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root

# Helper function to print the tree in level order for verification
def print_tree(root: Optional[TreeNode]):
    if not root:
        return "Empty"
    
    result, queue = [], [root]
    while queue:
        level = []
        next_queue = []
        for node in queue:
            if node:
                level.append(node.val)
                next_queue.append(node.left)
                next_queue.append(node.right)
            else:
                level.append(None)
        result.append(level)
        queue = next_queue
    return result

# Test Case
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case: Example tree
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    result = solution.invertTree(root)
    expected = [[4], [7, 2], [9, 6, 3, 1]]
    print("Test Case:", print_tree(result))
    print("Passed" if print_tree(result) == expected else "Failed")