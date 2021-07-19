"""
Question Link: https://leetcode.com/problems/sort-array-by-parity-ii/
Difficulty: Easy
Related Topics: Array, Sort
Solved by 07.22.2020 
Runtime: 396(ms), Memory Usage: 16.4(MB)
"""

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        current_index = 1
        for i in range(0,len(A),2):
            if A[i] % 2 == 1:
                while A[current_index] % 2 == 1:
                    current_index += 2
                A[i], A[current_index] = A[current_index], A[i]
        return A
