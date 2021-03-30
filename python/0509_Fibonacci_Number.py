"""
Question Link: https://leetcode.com/problems/fibonacci-number/
Difficulty: Easy
Related Topics: Array
Solved by 07.28.2020 
Runtime: 880(ms), Memory Usage: 13.6(MB)
"""

class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return self.fib(N-1) + self.fib(N-2)