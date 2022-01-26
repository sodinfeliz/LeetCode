"""
Question Link: https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy
Related Topics: String, Stack
Solved by 05.24.2021
Runtime: 24(ms), Memory Usage: 14.4(MB)
"""

# Runtime: 24(ms)(97.29%), Memory Usage: 14.4(MB)(35.78%)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack: return False
                tail = stack.pop()
                if ch == ')' and tail == '(':
                    continue
                elif ch == ']' and tail == '[':
                    continue
                elif ch == '}' and tail == '{':
                    continue
                else:
                    return False
        if stack:
            return False
        return True


# Runtime: 32(ms)(76.08%), Memory Usage: 14.4(MB)(35.78%)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            elif len(stack):
                lval = stack.pop()
                if (ch == ')' and lval != '(') or \
                   (ch == ']' and lval != '[') or \
                   (ch == '}' and lval != '{'):
                    return False
            else:
                return False
        return False if len(stack) else True