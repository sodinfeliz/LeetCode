"""
Question Link: https://leetcode.com/problems/linked-list-cycle-ii/
Difficulty: Medium
Related Topics: Linked List, Two Pointers 
Solved by 10.28.2020 
Runtime: 48(ms), Memory Usage: 17.3(MB)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## Using Floyd's Cycle Detection Algorithm

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        def same_node(n1, n2):
            return n1.val == n2.val and n1.next == n2.next
        
        if head is None:
            return None
        
        t = head  # tortoise
        h = head  # hare
        
        while True:
            if h.next is None or h.next.next is None:
                return None
            h = h.next.next
            t = t.next
            
            if same_node(t, h):
                break
                
        t = head  # return tortoise to the start point
        while not same_node(t, h):
            t = t.next
            h = h.next
            
        return t
