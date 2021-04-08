"""
Question Link: https://leetcode.com/problems/lucky-numbers-in-a-matrix/
Difficulty: Easy
Related Topics: Array
Solved by 07.19.2020 
Runtime: 140(ms), Memory Usage: 14.2(MB)
"""

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        max_in_column = [float('-inf')] * len(matrix[0])
        max_in_row = []
        for row in matrix:
            max_in_row.append(min(row))
            for index, elem in enumerate(row):
                max_in_column[index] = max(max_in_column[index], elem)

        lucky_number = set(max_in_column).intersection(set(max_in_row))
        return [] if not lucky_number else [lucky_number.pop()]
