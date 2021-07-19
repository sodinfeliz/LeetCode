"""
Question Link: https://leetcode.com/problems/count-largest-group/
Difficulty: Easy
Related Topics: Array
Solved by 07.20.2020 
Runtime: 216(ms), Memory Usage: 13.9(MB)
"""

class Solution:
    def countLargestGroup(self, n: int) -> int:
        result = {}
        for i in range(1, n+1):
            dsum = sum(map(int, str(i)))
            result[dsum] = result.get(dsum, 0) + 1
        return sum([elem == max(result.values()) for elem in result.values()])
