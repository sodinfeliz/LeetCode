"""
Question Link: https://leetcode.com/problems/linked-list-cycle/
Difficulty: Easy
Related Topics: Hash Table, Linked List, Two Pointers
Solved by 08.04.2021 
Runtime: 56(ms), Memory Usage: 17.8(MB)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        is_circle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                is_circle = True
                break
        return is_circle
