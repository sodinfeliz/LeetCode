"""
Question Link: https://leetcode.com/problems/add-two-numbers-ii/
Difficulty: Medium
Related Topics: Linked List, Math, Stack
Solved by 08.17.2021
Runtime: 60(ms), Memory Usage: 14.2(MB)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], 
														l2: Optional[ListNode]) -> Optional[ListNode]:

        rl1 = self.reverse_linked_list(l1)  # reverse list1
        rl2 = self.reverse_linked_list(l2)  # reverse list2
        head = ListNode(-1)
        ptr = head
        
        remainder = 0
        while rl1 or rl2:
            if rl1 is not None:
                remainder += rl1.val
                rl1 = rl1.next
            if rl2 is not None:
                remainder += rl2.val
                rl2 = rl2.next
            ptr.next = ListNode(remainder % 10)
            ptr, remainder = ptr.next, remainder // 10
            
        if remainder:
            ptr.next = ListNode(remainder)
                        
        return self.reverse_linked_list(head.next)
        
    def reverse_linked_list(self, head):
        if head is None: return None
        rev = None
        while head:
            tmp = head.next
            head.next = rev
            rev, head = head, tmp
        return rev
