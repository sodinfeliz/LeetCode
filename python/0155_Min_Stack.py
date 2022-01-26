"""
Question Link: https://leetcode.com/problems/min-stack/
Difficulty: Easy
Related Topics: Stack, Design
Solved by 01.25.2022
Runtime: 600(ms), Memory Usage: 18.1(MB)
"""

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)

