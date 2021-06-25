"""
Question Link: https://leetcode.com/problems/minimum-time-visiting-all-points/
Difficulty: Easy
Related Topics: Array
Solved by 07.22.2020 
Runtime: 56(ms), Memory Usage: 13.7(MB)
"""

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        num_step = 0
        for i in range(len(points)-1):
            num_step += max(abs(points[i][0]-points[i+1][0]), abs(points[i][1]-points[i+1][1]))
        return num_step