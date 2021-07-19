"""
Question Link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
Difficulty: Easy
Related Topics: Array
Solved by 07.15.2020 
Runtime: 176(ms), Memory Usage: 14.8(MB)
"""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum([sum([elem < 0 for elem in row]) for row in grid])
