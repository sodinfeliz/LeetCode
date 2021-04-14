"""
Question Link: https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
Difficulty: Easy
Related Topics: Array
Solved by 08.31.2020
Runtime: 32(ms), Memory Usage: 13.9(MB)
"""

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows = [0]*n
        cols = [0]*m
        for ri, ci in indices:
            rows[ri] = (rows[ri] + 1) % 2
            cols[ci] = (cols[ci] + 1) % 2
        odd_row_num = sum(rows)
        odd_col_num = sum(cols)
        return odd_col_num * (n-odd_row_num) + (m - odd_col_num) * odd_row_num
