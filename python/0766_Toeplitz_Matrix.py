"""
Question Link: https://leetcode.com/problems/toeplitz-matrix/
Difficulty: Easy
Related Topics: Array
Solved by 07.24.2020 
Runtime: 92(ms), Memory Usage: 13.9(MB)
"""

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix)==1 or len(matrix[0])==1: return True
    
        index = [(0, 0)]
        index.extend([(0, j) for j in range(1, len(matrix[0])-1)])
        index.extend([(i, 0) for i in range(1, len(matrix)-1)])
        for pos in index:
            i, j = pos
            val = matrix[i][j]
            i, j = i+1, j+1

            while i < len(matrix) and j < len(matrix[0]):
                if matrix[i][j] != val:
                    return False
                else:
                    i, j = i+1, j+1
        return True
