"""
Question Link: https://leetcode.com/problems/rotate-image/
Difficulty: Medium
Related Topics: Array
Solved by 07.16.2020 
Runtime: 68(ms), Memory Usage: 13.7(MB)
"""

class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i] = matrix[i][::-1]