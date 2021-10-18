"""
Question Link: https://leetcode.com/problems/backspace-string-compare/
Difficulty: Easy
Related Topics: String, Stack, Two Pointers
Solved by 10.07.2021
Runtime: 28(ms), Memory Usage: 14.3(MB)
"""

# Runtime: 28(ms)(88.72%), Memory Usage: 14.3(MB)(18.73%)
# Time complexity: O(n), Space Complexity: O(n)
# Stack Implementation
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.stack_generator(s) == self.stack_generator(t)
                
    def stack_generator(self, s):
        stack = []
        for ch in s:
            if ch != '#':
                stack.append(ch)
            elif len(stack):
                stack.pop()
        return stack
