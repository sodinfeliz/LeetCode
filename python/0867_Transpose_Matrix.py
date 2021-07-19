"""
Question Link: https://leetcode.com/problems/transpose-matrix/
Difficulty: Easy
Related Topics: Array
Solved by 07.22.2020 
Runtime: 76(ms), Memory Usage: 14.5(MB)
"""

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(A[0])):
            row = []
            for j in range(len(A)):
                row.append(A[j][i])
            result.append(row)
        return result
