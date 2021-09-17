"""
Question Link: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
Difficulty: Easy
Related Topics: Linked List, Math
Solved by 08.06.2021
Runtime: 32(ms), Memory Usage: 14.2(MB)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        value, ptr = head.val, head
        while ptr.next:
            ptr = ptr.next
            value = value*2 + ptr.val
        return value
