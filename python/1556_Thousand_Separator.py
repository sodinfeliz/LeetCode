"""
Question Link: https://leetcode.com/problems/thousand-separator/
Difficulty: Easy
Related Topics: String
Solved by 10.07.2021
Runtime: 32(ms), Memory Usage: 14.4(MB)
"""

class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)[::-1]
        sub = [n[i: i+3][::-1] for i in range(0, len(n), 3)][::-1]
        return '.'.join(sub)
