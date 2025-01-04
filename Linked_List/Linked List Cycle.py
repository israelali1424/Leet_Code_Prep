'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
'''
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # you use the fast and slow poiner method 
        # the fast pointer 2x as slow poiner will move faster 
        # if the slow and fast pointer ever meet that means we have a cycle 
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True 
        return False
    
# Helper function to create a cycle in the linked list
def create_cycle(nodes, pos):
    if pos == -1:
        return nodes[0] if nodes else None
    
    cycle_node = nodes[pos] if pos < len(nodes) else None
    if nodes and cycle_node:
        nodes[-1].next = cycle_node
    return nodes[0]

# Test cases
def run_tests():
    solution = Solution()
    
    # Test Case 1: Cycle Exists
    nodes = [ListNode(i) for i in range(1, 5)]
    for i in range(3):
        nodes[i].next = nodes[i + 1]
    nodes[3].next = nodes[1]  # Cycle back to node 2
    print(solution.hasCycle(nodes[0]))  # Expected: True
    
    # Test Case 2: No Cycle
    nodes = [ListNode(i) for i in range(1, 5)]
    for i in range(3):
        nodes[i].next = nodes[i + 1]
    print(solution.hasCycle(nodes[0]))  # Expected: False
    
    # Test Case 3: Single Node with Cycle
    node = ListNode(1)
    node.next = node
    print(solution.hasCycle(node))  # Expected: True
    
    # Test Case 4: Single Node without Cycle
    node = ListNode(1)
    print(solution.hasCycle(node))  # Expected: False
    
    # Test Case 5: Empty List
    print(solution.hasCycle(None))  # Expected: False

run_tests()
