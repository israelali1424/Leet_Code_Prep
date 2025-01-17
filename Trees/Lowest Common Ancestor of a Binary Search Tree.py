'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T 
that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
'''
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root 
        while curr:
            if curr.val < p.val and  curr.value < q.val:
                curr = curr.right
            elif curr.val > p.val and  curr.val > q.val:
                curr = curr.left
            else:
                return curr
class Solution:
    def __init__(self):
        self.lca = [None]  # Use a list to store the LCA reference

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(node):
            if not node:
                return

            # Store the current node as a candidate for LCA
            self.lca[0] = node

            # Check if the current node matches either p or q
            if node is p or node is q:
                return

            # Traverse the tree based on the values of p and q
            if node.val < p.val and node.val < q.val:
                search(node.right)
            elif node.val > p.val and node.val > q.val:
                search(node.left)
            else:
                # If neither condition matches, the current node is the LCA
                return

        search(root)
        return self.lca[0]

