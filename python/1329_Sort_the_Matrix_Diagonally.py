"""
Question Link: https://leetcode.com/problems/sort-the-matrix-diagonally/
Difficulty: Medium
Related Topics: Array, Sort
Solved by 10.23.2020 
Runtime: 80(ms), Memory Usage: 14.2(MB)
"""

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def replace(target, i_, j_):
            for idx, t in enumerate(target):
                mat[i_+idx][j_+idx] = t

        m, n = len(mat), len(mat[0])
        init_idx = [[row, 0] for row in range(m)] + [[0, col] for col in range(1, n)]

        for init_i, init_j in init_idx:
            i, j = init_i, init_j
            elem = []
            while i < m and j < n:
                elem.append(mat[i][j])
                i, j = i+1, j+1
            replace(sorted(elem), init_i, init_j)

        return mat
