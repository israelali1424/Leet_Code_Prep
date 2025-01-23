'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
Input: root = [3,1,4,null,2], k = 1
Output: 1

'''
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# my wrong solution I had the right idea but I was not returning the right value
# becuase originally I had the result list in the inorder function and as part KthSmallest function to global 
#for both function to access it
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder travsal put the items into a list 
        # sort the list and 
        # return list =-1 
        result = []
        def inorder(root,result):
            if not root:
                return result
            inorder(root.left,result)
            print(root.val)
            result.append(root.val)
            inorder(root.right,result)
            return result 
        nodes = inorder(root,result)
        # if len(nodes) >   k:
        #     return 
        
        return result[k-1]
        
        

# Helper function to build a tree from a list
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

        
#Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Regular case
    root1 = build_tree([3, 1, 4, None, 2])
    k1 = 1
    result1 = solution.kthSmallest(root1, k1)
    print("Test Case 1:", result1, "Passed" if result1 == 1 else "Failed")
    assert result1 == 1
    # Expected Output: 1

    # Test Case 2: Larger tree
    root2 = build_tree([5, 3, 6, 2, 4, None, None, 1])
    k2 = 3
    result2 = solution.kthSmallest(root2, k2)
    print("Test Case 2:", result2, "Passed" if result2 == 3 else "Failed")
    assert result2 == 3
    # Expected Output: 3

    # Test Case 3: Single node tree
    root3 = build_tree([1])
    k3 = 1
    result3 = solution.kthSmallest(root3, k3)
    print("Test Case 3:", result3, "Passed" if result3 == 1 else "Failed")
    assert result3 == 1
    
 # optimal solution
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize count to track remaining elements to find
        count = [k]
        # Store the kth smallest element
        ans = [0]
        
        def dfs(node):
            # Base case: if node is None, return
            if not node:
                return
            
            # First, traverse left subtree (smaller elements)
            dfs(node.left)
            
            # Decrement count when visiting a node
            count[0] -= 1
            
            # If count reaches 0, we've found the kth smallest element
            if count[0] == 0:
                ans[0] = node.val
                return
            
            # Continue to right subtree if we haven't found kth element
            if count[0] > 0:
                dfs(node.right)
        
        # Start depth-first search from root
        dfs(root)
        
        # Return the kth smallest element
        return ans[0]
# Time: O(n)
# Space: O(n)
# Time: O(n)
# Space: O(log n) - for the recursion stack in the best case (balanced tree)