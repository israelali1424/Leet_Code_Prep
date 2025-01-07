'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0  # Store the maximum diameter
        
        # Helper function to calculate the height
        def dfs(curr):
            if not curr:
                return 0  # Base case: return 0 for null nodes
            left = dfs(curr.left)  # Get height of left subtree
            right = dfs(curr.right)  # Get height of right subtree
            
            # Update the maximum diameter (left + right gives the path through the node)
            self.res = max(self.res, left + right)
            
            # Return the height of the current node
            return 1 + max(left, right)
        
        dfs(root)  # Start DFS from the root node
        return self.res  # Return the maximum diameter found
# Test cases for diameterOfBinaryTree

# Helper function to build a binary tree
def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while i < len(nodes):
        curr = queue.pop(0)
        if nodes[i] is not None:
            curr.left = TreeNode(nodes[i])
            queue.append(curr.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            curr.right = TreeNode(nodes[i])
            queue.append(curr.right)
        i += 1
    return root

# Test Case 1: Basic Tree
root1 = build_tree([1, 2, 3, 4, 5])
print(Solution().diameterOfBinaryTree(root1))  # Expected Output: 3

# Test Case 2: Single Node
root2 = build_tree([1])
print(Solution().diameterOfBinaryTree(root2))  # Expected Output: 0

# Test Case 3: Linear Tree (Skewed Left)
root3 = build_tree([1, 2, None, 3, None, 4])
print(Solution().diameterOfBinaryTree(root3))  # Expected Output: 3

# Test Case 4: Linear Tree (Skewed Right)
root4 = build_tree([1, None, 2, None, 3, None, 4])
print(Solution().diameterOfBinaryTree(root4))  # Expected Output: 3

# Test Case 5: Balanced Tree
root5 = build_tree([1, 2, 3, 4, 5, 6, 7])
print(Solution().diameterOfBinaryTree(root5))  # Expected Output: 4

# Test Case 6: Empty Tree
root6 = build_tree([])
print(Solution().diameterOfBinaryTree(root6))  # Expected Output: 0
