"""
Question Link: https://leetcode.com/problems/middle-of-the-linked-list/
Difficulty: Easy
Related Topics: Linked List, Two Pointers
Solved by 08.04.2021
Runtime: 32(ms), Memory Usage: 14.4(MB)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        ptr = head
        dptr = head
        
        while dptr.next:
            ptr = ptr.next
            for _ in range(2):
                if dptr.next:
                    dptr = dptr.next
                    
        return ptr
