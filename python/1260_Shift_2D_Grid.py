"""
Question Link: https://leetcode.com/problems/shift-2d-grid/
Difficulty: Easy
Related Topics: Array
Solved by 07.20.2020 
Runtime: 152(ms), Memory Usage: 13.8(MB)
"""

class Solution:
    def shiftGrid(self, grid, k: int):
        row_move = (k // len(grid[0])) % len(grid)
        col_move = k % len(grid[0])

        result = []
        if col_move > 0:
            for index, _ in enumerate(grid):
                result.append(grid[index-1][-col_move:] + grid[index][:-col_move])
        else:
            result = grid

        return result[-row_move:] + result[:-row_move]
