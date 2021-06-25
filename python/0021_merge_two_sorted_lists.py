"""
Question Link: https://leetcode.com/problems/merge-two-sorted-lists/
Difficulty: Easy
Related Topics: Linked List, Recursion
Solved by 06.01.2021
Runtime: 52(ms), Memory Usage: 14.3(MB)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None: return None
        head = ListNode()
        pointer = head
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                pointer.next = l1
                pointer = l1
                l1 = l1.next
            else:
                pointer.next = l2
                pointer = l2
                l2 = l2.next

        pointer.next = l2 if l1 is None else l1
        return head.next
