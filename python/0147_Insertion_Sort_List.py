"""
Question Link: https://leetcode.com/problems/insertion-sort-list/
Difficulty: Medium
Related Topics: Linked List, Sort
Solved by 11.03.2020 
Runtime: 1512(ms), Memory Usage: 15.8(MB)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        result = ListNode()
        
        curr = head
        while curr:
            prev_node = result
            next_node = result.next
            
            while next_node:
                if next_node.val > curr.val:
                    break
                prev_node = next_node
                next_node = next_node.next
                
            temp_next = curr.next
            
            # inseting to the result
            curr.next = next_node
            prev_node.next = curr
            
            curr = temp_next
            
        return result.next