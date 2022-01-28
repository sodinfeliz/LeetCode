"""
Question Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Difficulty: Medium
Related Topics: Linked Lisr, Two Pointers
Solved by 01.28.2022
Runtime: 67(ms), Memory Usage: 13.8(MB)
"""

# Runtime: 67(ms)(6.45%), Memory Usage: 13.8(MB)(99.93%)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:     
        length = 1
        tail = ptr = head
        while tail.next is not None:
            tail = tail.next
            length += 1
        
        if n == length:
            return head.next
        
        for _ in range(length - n - 1):
            ptr = ptr.next
            
        ptr.next = ptr.next.next 
        return head


# Most voted post, Author: TMS
# Runtime: 50(ms)(28.92%), Memory Usage: 14(MB)(98.65%)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:      
        dump = ListNode(0, head)
        slow = fast = dump
        for _ in range(n):
            fast = fast.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dump.next
