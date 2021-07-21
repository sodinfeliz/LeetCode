"""
Question Link: https://leetcode.com/problems/sqrtx/
Difficulty: Easy
Related Topics: Math, Binary Search
Solved by 07.21.2021
Runtime: 28(ms), Memory Usage: 14.1(MB)
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return x
        l, r = 1, x
        while r - l > 1:
            m = (r+l)//2
            if m*m > x:
                r = m
            else:
                l = m
        return l
