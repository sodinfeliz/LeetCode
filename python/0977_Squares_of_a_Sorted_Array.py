"""
Question Link: https://leetcode.com/problems/squares-of-a-sorted-array/
Difficulty: Easy
Related Topics: Array
Solved by 08.04.2020 
Runtime: 428(ms), Memory Usage: 15.8(MB)
"""

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(map(lambda x: x**2, A))
