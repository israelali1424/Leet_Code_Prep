'''
Given the root of a Binary Search Tree (BST), 
return the minimum absolute difference between the values of any two different nodes in the tree.
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_distance = [float("inf")]
        prev = [None]
        
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            if prev[0] is not None:
                min_distance[0] = min(min_distance[0], node.val - prev[0].val)
            prev[0] = node
            dfs(node.right)
        
        dfs(root)
        return min_distance[0]