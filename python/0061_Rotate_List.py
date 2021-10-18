"""
Question Link: https://leetcode.com/problems/rotate-list/
Difficulty: Medium
Related Topics: Linked List, Two Pointers
Solved by 08.19.2021
Runtime: 32(ms), Memory Usage: 14.5(MB)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime: 32(ms)(90.88%), Memory Usage: 14.5(MB)(29.02%)
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head
        
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        if k % length == 0:
            return head
            
        k = length - (k % length) 
        ptr = head
        for _ in range(k-1):
            ptr = ptr.next
            
        new_head = ptr.next
        ptr.next = None
        tail.next = head
        
        return new_head
