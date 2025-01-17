'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.ancestors = []  # Initialize the ancestors list
        self.prev = None     # Optional: Initialize prev if you want it tied to nodes (not common)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: If the root is None or matches either p or q, return the root
        if not root or root == p or root == q:
            return root

        # Recursively search in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If p and q are found in different subtrees, the current root is their LCA
        if left and right:
            return root

        # Otherwise, return the non-null value (either left or right)
        return left if left else right

      
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        node = queue.pop(0)
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

# Test Case
if __name__ == "__main__":
    # Input: root = [3,5,1,6,2,0,8,null,null,7,4]
    values = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = build_tree(values)
    
    # Create Solution object
    solution = Solution()
    
    # Find nodes p and q
    p = root.left  # Node with value 5
    q = root.left.right.right  # Node with value 4
    
    # Find the lowest common ancestor
    lca = solution.lowestCommonAncestor(root, p, q)
    print("Lowest Common Ancestor:", lca.val)  # Expected Output: 5