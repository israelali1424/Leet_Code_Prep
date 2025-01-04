# Definition for a binary tree node.

import collections
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        #we can use queue appoarch for level order traversal for a regular binary tree
        #and bfs
        q = collections.deque()
        q.append(root)
    
        while q: 
            #how many nodes there are in the queue
            # this q length basically ensure that we are going one level at a time
            num_nodes_in_q = len(q)
            # with node from that level we are going to be adding it to it's own list 
            # then we will that level list to the result  list
            level = []
            #we need to every q item that is has left node or right node next nodes
            # loop  through every value in the queue currently 
            for i in range(num_nodes_in_q):
                node = q.popleft() #pop next node from the front/left of the queue
                if node:
                    # add the current node val to the list of vals of this level 
                    level.append(node.val)
                    # add the children of the current node to the quuee
                    q.append(node.left)
                    q.append(node.right)
            # if a level is not empty add to the result list
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
