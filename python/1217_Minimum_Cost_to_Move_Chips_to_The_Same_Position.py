"""
Question Link: https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
Difficulty: Easy
Related Topics: Array, Math, Greedy
Solved by 11.06.2020
Runtime: 28(ms), Memory Usage: 14.2(MB)
"""

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = odd = 0
        for elem in position:
            if elem % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(odd, even)
