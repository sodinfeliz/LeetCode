"""
Question Link: https://leetcode.com/problems/climbing-stairs/
Difficulty: Easy
Related Topics: Math, DP
Solved by 07.22.2021
Runtime: 28(ms), Memory Usage: 14.2(MB)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3: return n
        l, h = 1, 2
        for _ in range(n-2):
            l, h = h, l+h
        return h
