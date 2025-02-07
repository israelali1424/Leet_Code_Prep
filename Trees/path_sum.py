'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # Base case: If root is None, there's no path
        if not root:
            return False
        
        # Check if it's a leaf node and the path sum matches targetSum
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recur for left and right subtrees with the updated targetSum
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))

# Example Tree:
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)

solution = Solution()

# Test Case 1: Valid Path Exists
print(solution.hasPathSum(root, 22))  # Output: True (5 -> 4 -> 11 -> 2)

# Test Case 2: No Valid Path
print(solution.hasPathSum(root, 26))  # Output: False

# Test Case 3: Empty Tree
print(solution.hasPathSum(None, 1))   # Output: False

#Second Try 2/1/2025
# orginal code 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    # if leaf node and the target is not found that means there is no path 
    # create a helper function so that you can keep track of the values beiing adde 
    # 
        total = 0
        def  dfs(root,total):
            if not root:
                return False
            total = total + root.val
            # it fails here because I do not handle for leaf node 
            # the code does not account for reaching a leaf node when checking if the path sum matches the target.
            if total == targetSum:
                return True
                
            left = dfs(root.left,total)
            right = dfs(root.right,total)
            return left or right 
        return dfs(root,total)

#correct from AI 
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, total):
            if not root:
                return False
            
            total += root.val  # Add current node's value to the total sum
            
            # Check if it's a leaf node and the sum matches
            if not root.left and not root.right:
                return total == targetSum
            
            # Recursively check left and right children
            left = dfs(root.left, total)
            right = dfs(root.right, total)
            
            return left or right
        
        return dfs(root, 0)  # Start the dfs with total sum as 0
