'''
572. Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def isSubtree_broke(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return False
        def isSubroot(subRoot,root):
            if not subRoot and  not root:
                return True 
            if subRoot.val != root.val:
                return False
            return isSubroot(subRoot.left,root.left) and  isSubroot(subRoot.right,root.right)

        left =  isSubroot(subRoot,root.left)
        right = isSubroot(subRoot,root.right)

        if left or right:
            print(left)
            print(right)
            return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:  # An empty subtree is always a subtree.
            return True
        if not root:  # If the main tree is empty, it can't contain a subtree.
            return False

        def isSubroot(root, subRoot):
            if not root and not subRoot:  # Both trees are empty.
                return True
            if not root or not subRoot:  # One tree is empty, but the other is not.
                return False
            if root.val != subRoot.val:  # Root values do not match.
                return False
            return isSubroot(root.left, subRoot.left) and isSubroot(root.right, subRoot.right)

        # Check if the current root matches the subRoot or recurse left and right.
        return isSubroot(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# Test case 1: Subtree is a valid subtree
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)
assert Solution().isSubtree(root, subRoot) == True  # Expected output: True

# Test case 2: Subtree is not a valid subtree
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(3)
assert Solution().isSubtree(root, subRoot) == False  # Expected output: False

# Test case 3: Empty subRoot (always a subtree)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
subRoot = None
assert Solution().isSubtree(root, subRoot) == True  # Expected output: True

# Test case 4: Empty root and non-empty subRoot
root = None
subRoot = TreeNode(1)
assert Solution().isSubtree(root, subRoot) == False  # Expected output: False

# Test case 5: Both root and subRoot are empty
root = None
subRoot = None
assert Solution().isSubtree(root, subRoot) == True  # Expected output: True

# Test case 6: Subtree is the entire tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
subRoot = TreeNode(1)
subRoot.left = TreeNode(2)
subRoot.right = TreeNode(3)
assert Solution().isSubtree(root, subRoot) == True  # Expected output: True

print("All test cases passed!")