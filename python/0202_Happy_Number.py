"""
Question Link: https://leetcode.com/problems/happy-number/
Difficulty: Medium
Related Topics: Math
Solved by 10.30.2020 
Runtime: 36(ms), Memory Usage: 14.2(MB)
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        while n >= 10:
            summation = 0
            for digit in str(n):
                summation += int(digit)**2
            n = summation
        return n ==1 or n == 7
