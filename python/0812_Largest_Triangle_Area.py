"""
Question Link: https://leetcode.com/problems/largest-triangle-area/submissions/
Difficulty: Easy
Related Topics: Math
Solved by 11.03.2020 
Runtime: 152(ms), Memory Usage: 14.1(MB)
"""

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        result = 0.
        n = len(points)
        for i in range(n-2):
            for j in range(i, n-1):
                for k in range(j, n):
                    x, y, z = points[i], points[j], points[k]
                    area = abs(x[0]*(y[1]-z[1]) + y[0]*(z[1]-x[1]) + z[0]*(x[1]-y[1])) / 2
                    result = max(result, area)
        return result
