from queue_example import Queue
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = Queue()  # Using our custom Queue class
        queue.enqueue(root)
        
        while not queue.is_empty():
            num_nodes_in_q = queue.size()
            level = []
            
            for i in range(num_nodes_in_q):
                node = queue.dequeue()  # Use custom dequeue
                if node:
                    level.append(node.val)
                    if node.left:
                        queue.enqueue(node.left)  # Use custom enqueue
                    if node.right:
                        queue.enqueue(node.right)
            
            if level:
                result.append(level)
        
        return result

# Test case
if __name__ == "__main__":
    # Build the tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    # Test the level order traversal
    sol = Solution()
    output = sol.levelOrder(root)
    print(output)  # Expected Output: [[1], [2, 3], [4, 5, 6]]