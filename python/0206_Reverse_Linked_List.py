"""
Question Link: https://leetcode.com/problems/reverse-linked-list/
Difficulty: Easy
Related Topics: Linked List
Solved by 08.04.2021
Runtime: 28(ms), Memory Usage: 15.6(MB)
"""

# Runtime: 28(ms)(96.71%), Memory Usage: 15.6(MB)(76.85%)
# Time complexity: O(n), Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:        
        rv_list, ptr = None, head
        while ptr:
            tmp = ptr.next
            ptr.next = rv_list
            rv_list, ptr = ptr, tmp 
    
        return rv_list
