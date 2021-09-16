"""
Question Link: https://leetcode.com/problems/add-two-numbers/
Difficulty: Medium
Related Topics: Linked List, Math
Solved by 08.19.2021 
Runtime: 60(ms), Memory Usage: 14.1(MB)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime: 60(ms)(96.3%), Memory Usage: 14.1(MB)(98.2%)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = l1, l2
        remainder = 0
        new_head = ListNode(-1)
        nptr = new_head
        
        while ptr1 or ptr2:
            if ptr1:
                remainder += ptr1.val
                ptr1 = ptr1.next
            if ptr2:
                remainder += ptr2.val
                ptr2 = ptr2.next
            nptr.next = ListNode(remainder % 10)
            nptr = nptr.next
            remainder //= 10
            
        if remainder: nptr.next = ListNode(remainder)
        return new_head.next
