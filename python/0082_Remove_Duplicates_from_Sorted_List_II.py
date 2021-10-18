"""
Question Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
Difficulty: Medium
Related Topics: Two Pointers, Linked List
Solved by 08.19.2021
Runtime: 40(ms), Memory Usage: 14.3(MB)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime: 40(ms)(71.81%), Memory Usage: 14.3(MB)(27.79%)
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: 
            return head
        
        dummy_head = ListNode(-1, head)
        ptr = dummy_head
        
        while ptr and ptr.next and ptr.next.next:
            if ptr.next.val != ptr.next.next.val:
                ptr = ptr.next
            else:
                nptr, val = ptr.next.next, ptr.next.val
                while nptr and nptr.val == val:
                    nptr = nptr.next
                ptr.next = nptr
                
        return dummy_head.next
