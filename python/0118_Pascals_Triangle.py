"""
Question Link: https://leetcode.com/problems/pascals-triangle/
Difficulty: Easy
Related Topics: Array
Solved by 07.21.2020 
Runtime: 52(ms), Memory Usage: 13.9(MB)
"""

class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            sub = self.generate(numRows-1)
            left = sub[-1] + [0]
            right = [0] + sub[-1]
            sub.append([a+b for a, b in zip(left, right)])
            return sub