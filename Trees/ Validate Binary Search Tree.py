'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional
class Solution:
    # with helper function
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            # An empty tree is a valid BST
            if not node:
                return True
            
            # The current node's value must be within the range
            if not (low < node.val < high):
                return False
            
            # Recursively validate the left and right subtrees
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        
        # Start with the full range of valid values
        return validate(root, float('-inf'), float('inf'))
    
    # without helper function
    def isValidBSTNoHelper(self, root: Optional[TreeNode], low=float('-inf'), high=float('inf')) -> bool:
        if not root:
            return True        
        if not (low < root.val < high):
            return False
        
        return (self.isValidBST(root.left, low, root.val) and
                self.isValidBST(root.right, root.val, high))