"""
Question Link: https://leetcode.com/problems/merge-in-between-linked-lists/
Difficulty: Medium
Related Topics: Linked List
Solved by 08.13.2021
Runtime: 452(ms), Memory Usage: 20.2(MB)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time complexity: O(m+n), Space Complexity: O(1)
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        head, tail = list1, list1.next
        for _ in range(a-1):
            head = head.next
        for _ in range(b):
            tail = tail.next
        
        head.next = list2
        while head.next:
            head = head.next
        head.next = tail
        
        return list1
