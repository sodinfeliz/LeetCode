"""
Question Link: https://leetcode.com/problems/odd-even-linked-list/
Difficulty: Medium
Related Topics: Linked List
Solved by 08.13.2021
Runtime: 53(ms), Memory Usage: 16.3(MB)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time complexity: O(n), Space Complexity: O(1)
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        o_head, e_head = head, head.next
        ptr_o, ptr_e = o_head, e_head
        
        while ptr_e and ptr_e.next:
            ptr_o.next, ptr_e.next = ptr_e.next, ptr_e.next.next
            ptr_o, ptr_e = ptr_o.next, ptr_e.next

        ptr_o.next = e_head
        return o_head
