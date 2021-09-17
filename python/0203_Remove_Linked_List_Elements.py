"""
Question Link: https://leetcode.com/problems/remove-linked-list-elements/
Difficulty: Easy
Related Topics: Linked List
Solved by 08.13.2021
Runtime: 64(ms), Memory Usage: 17.3(MB)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time complexity: O(n), Space Complexity: O(1)
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None: return head
        
        while head and head.val == val:
            head = head.next
        
        ptr = head
        while ptr and ptr.next:
            if ptr.next.val == val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
            
        return head
