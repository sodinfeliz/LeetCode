"""
Question Link: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
Difficulty: Easy
Related Topics: Array
Solved by 01.15.2021
Runtime: 36(ms), Memory Usage: 14.4(MB)
"""

class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1: return [0]
        result = list(range(1, n))
        result.append(-int(n*(n-1)/2))
        return result
