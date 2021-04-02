"""
Question Link: https://leetcode.com/problems/flipping-an-image/
Difficulty: Easy
Related Topics: Array
Solved by 07.16.2020 
Runtime: 60(ms), Memory Usage: 13.9(MB)
"""

class Solution:
    def flipAndInvertImage(self, A):
        for i in range(len(A)):
            A[i] = [elem ^ 1 for elem in A[i][::-1]]
        return A
