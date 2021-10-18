"""
Question Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Difficulty: Easy
Related Topics: Linked List
Solved by 08.13.2021
Runtime: 40(ms), Memory Usage: 14.1(MB)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime: 40(ms)(79.61%), Memory Usage: 14.1(MB)(94.32%)
# Time complexity: O(n), Space Complexity: O(1)
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return head
        ptr = head
        while ptr and ptr.next:
            if ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return head
