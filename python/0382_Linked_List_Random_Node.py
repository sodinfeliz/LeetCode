"""
Question Link: https://leetcode.com/problems/linked-list-random-node/
Difficulty: Medium
Related Topics: Linked List, Math
Solved by 08.20.2021
Runtime: 72(ms), Memory Usage: 17.4(MB)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def __init__(self, head: Optional[ListNode]):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.elem = []
        self.literate_linked_list()

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return self.elem[random.randint(0, len(self.elem)-1)]
        
    def literate_linked_list(self):
        ptr = self.head
        while ptr:
            self.elem.append(ptr.val)
            ptr = ptr.next
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()