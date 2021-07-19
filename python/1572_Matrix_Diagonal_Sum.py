"""
Question Link: https://leetcode.com/problems/matrix-diagonal-sum/
Difficulty: Easy
Related Topics: Array
Solved by 10.23.2020 
Runtime: 100(ms), Memory Usage: 14.3(MB)
"""

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s, n = 0, len(mat)
        for row in range(n):
            s += mat[row][row] + mat[row][n-row-1]
        return s - (n%2==1) * mat[n//2][n//2]
