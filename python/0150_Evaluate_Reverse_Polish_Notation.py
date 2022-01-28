"""
Question Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
Difficulty: Medium
Related Topics: Array, Math, Stack
Solved by 01.26.2022
"""

# Runtime: 60(ms)(96.25%), Memory Usage: 14.7(MB)(48.28%)
# Time complexity: O(n), Space Complexity: O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                y = stack.pop()
                x = stack.pop()
                if token == "+":
                    stack.append(x+y)
                elif token == "-":
                    stack.append(x-y)
                elif token == "*":
                    stack.append(x*y)
                else:
                    stack.append(int(x/y))
            else:
                stack.append(int(token))
        
        return stack[0]
