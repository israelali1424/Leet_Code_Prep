'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None, the trees are identical at this point
        if not p and not q:
            return True
        # If one of the nodes is None or the values are different, the trees are not identical
        if not p or not q or p.val != q.val:
            return False
        # Recursively check the left and right subtrees
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        # Both left and right subtrees must be identical
        return left and right