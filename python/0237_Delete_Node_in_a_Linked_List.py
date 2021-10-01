"""
Question Link: https://leetcode.com/problems/delete-node-in-a-linked-list/
Difficulty: Easy
Related Topics: Linked List
Solved by 08.13.2021
Runtime: 44(ms), Memory Usage: 14.8(MB)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
