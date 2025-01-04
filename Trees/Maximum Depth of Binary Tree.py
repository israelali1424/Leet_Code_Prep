'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the 
longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2

'''
# Definition for a binary tree node.
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #recursive  dfs solution
    def maxDepth_dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # Base case: If the node is null, depth is 0.
        
        # Recursively find the depth of left and right subtrees
        left_depth = self.maxDepth_dfs(root.left)
        right_depth = self.maxDepth_dfs(root.right)
        
        # Return the maximum depth + 1 (for the current node)
        return max(left_depth, right_depth) + 1
    
    from collections import deque


    def maxDepth_bfs(self, root: TreeNode) -> int:
        if not root:
            return 0  # Return 0 for an empty tree
        
        level = 0
        q = deque([root])  # Initialize a queue with the root node
        
        while q:
            for i in range(len(q)):  # Process all nodes at the current level
                node = q.popleft()  # Remove the front node from the queue
                
                if node.left:
                    q.append(node.left)  # Add the left child to the queue
                
                if node.right:
                    q.append(node.right)  # Add the right child to the queue
            
            level += 1  # Increment level after processing all nodes at the current level
        
        return level
    
    def maxDepth_iterative(self, root: TreeNode) -> int:
        if not root:
            return 0  # Return 0 for an empty tree
        
        stack = [[root, 1]]  # Start with the root node and depth 1
        res = 1  # Initialize the result with the minimum depth
        
        while stack:
            node, depth = stack.pop()  # Pop the last node and its depth
            
            if node:
                res = max(res, depth)  # Update the maximum depth
                
                # Add child nodes with incremented depth
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        
        return res





# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Test cases
def run_tests():
    solution = Solution()
    
    # Test Case 1: Balanced Tree
    root = TreeNode(1, 
                    TreeNode(2, TreeNode(4), TreeNode(5)), 
                    TreeNode(3, None, TreeNode(6)))
    print(solution.maxDepth_bfs(root))  # Expected: 3
    
    # Test Case 2: Skewed Left Tree
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    print(solution.maxDepth_dfs(root))  # Expected: 3
    
    # Test Case 3: Skewed Right Tree
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    print(solution.maxDepth_dfs(root))  # Expected: 3
    
    # Test Case 4: Single Node Tree
    root = TreeNode(1)
    print(solution.maxDepth_dfs(root))  # Expected: 1
    
    # Test Case 5: Empty Tree
    root = None
    print(solution.maxDepth_bfs(root))  # Expected: 0
    
    # Test Case 6: Two Levels
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    print(solution.maxDepth_dfs(root))  # Expected: 2

run_tests()
