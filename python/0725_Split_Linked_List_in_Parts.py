"""
Question Link: https://leetcode.com/problems/split-linked-list-in-parts/
Difficulty: Medium
Related Topics: Linked List
Solved by 08.18.2021
Runtime: 28(ms), Memory Usage: 14.8(MB)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime: 28(ms)(98.28%), Memory Usage: 14.8(MB)(72.81%)
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        if head is None:
            return [None]*k
        elif k==1:
            return [head]
        
        ls = self.literate_linked_list(head)
        ls = self.split_list(ls, k)
        
        result = []
        for subls in ls:
            result.append(self.linked_list_construct(subls))
            
        return result
        
    def literate_linked_list(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result
    
    def linked_list_construct(self, nums):
				head = ListNode(-1)
        ptr = head
        for elem in nums:
            node = ListNode(elem)
            ptr.next, ptr = node, node
        return head.next

    def split_list(self, ls, k):
        nums = [len(ls)//k]*k
        for i in range(len(ls)%k):
            nums[i] += 1

        cumsum = 0
        result = []
        for num in nums:
            result.append(ls[cumsum: cumsum+num])
            cumsum += num

        return result