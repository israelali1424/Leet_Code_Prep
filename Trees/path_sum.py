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
