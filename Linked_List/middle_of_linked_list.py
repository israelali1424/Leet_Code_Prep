'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
'''
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    def middleNode_two_pointers(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        return slow
   
    def middleNode(self,head: ListNode) -> ListNode:
        first = head 
        second = head 
        list_len = 0
        
        if not head:
            return head
        
        # Calculate the length of the linked list
        while first: 
            list_len += 1
            first = first.next

        # Find the middle index
        mid = list_len // 2

        # Move the second pointer to the middle node
        for _ in range(mid):
            second = second.next
        
        return second
        
        