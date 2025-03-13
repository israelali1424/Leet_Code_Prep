'''
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

\
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]
        
        def height(node):
            if not node:
                return 0
                
            left = height(node.left)
            if  balanced [0]== False:
                return 0
            right = height(node.right)
            
            # Check if this node is unbalanced
            if abs(left - right) > 1:
                balanced[0]= False
                
            return max(left, right) + 1 
        
        height(root)
        return balanced[0]
# Test cases for Balanced Binary Tree
def test_isBalanced():
    solution = Solution()
    
    # Test Case 1: Empty Tree
    assert solution.isBalanced(None) == True, "Test Case 1 Failed"
    
    # Test Case 2: Single Node Tree
    root = TreeNode(1)
    assert solution.isBalanced(root) == True, "Test Case 2 Failed"
    
    # Test Case 3: Balanced Tree
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert solution.isBalanced(root) == True, "Test Case 3 Failed"
    
    # Test Case 4: Unbalanced Tree
    root = TreeNode(1, TreeNode(2, TreeNode(3)), None)
    assert solution.isBalanced(root) == False, "Test Case 4 Failed"
    
    # Test Case 5: Large Balanced Tree
    root = TreeNode(1,
                    TreeNode(2, TreeNode(4), TreeNode(5)),
                    TreeNode(3, TreeNode(6), TreeNode(7)))
    assert solution.isBalanced(root) == True, "Test Case 5 Failed"
    
    # Test Case 6: Large Unbalanced Tree
    root = TreeNode(1,
                    TreeNode(2, TreeNode(3, TreeNode(4)), None),
                    TreeNode(5))
    assert solution.isBalanced(root) == False, "Test Case 6 Failed"
    
    print("All test cases passed!")

# Run the tests
test_isBalanced()
