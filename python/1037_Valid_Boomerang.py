"""
Question Link: https://leetcode.com/problems/valid-boomerang/
Difficulty: Easy
Related Topics: Math, Geometry
Solved by 10.18.2021
Runtime: 36(ms), Memory Usage: 14.4(MB)
"""

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        return abs(points[0][0]*points[1][1] - points[1][0]*points[0][1] + \
                   points[1][0]*points[2][1] - points[2][0]*points[1][1] + \
                   points[2][0]*points[0][1] - points[0][0]*points[2][1]) != 0

