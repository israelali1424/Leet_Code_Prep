#Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True  # An empty tree is symmetric
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (
                left.val == right.val and
                isMirror(left.left, right.right) and
                isMirror(left.right, right.left)
    )
        return isMirror(root.left, root.right)