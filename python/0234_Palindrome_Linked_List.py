"""
Question Link: https://leetcode.com/problems/palindrome-linked-list/
Difficulty: Easy
Related Topics: Linked List, Stack, Two Pointers, Recursion
Solved by 08.11.2021
Runtime: 696(ms), Memory Usage: 31.5(MB)
"""

# Runtime: 696(ms)(92.86%), Memory Usage: 31.5(MB)(90.38%)
# Time complexity: O(n), Space Complexity: O(1)
class Solution:
    def isPalindrome(self, head) -> bool:
        slow, fast = head, head
        rev = None
        while fast.next and fast.next.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = rev
            slow, rev = tmp, slow
            
        if fast.next:
            right = slow.next
            slow.next = rev
            left = slow
        else:
            left, right = rev, slow.next
        
        is_palindrome = True
        while left != None:
            if left.val != right.val:
                is_palindrome = False
                break
            left, right = left.next, right.next
        
        return is_palindrome
