"""
Question Link: https://leetcode.com/problems/divisor-game/
Difficulty: Easy
Related Topics: String
Solved by 10.29.2020 
Runtime: 24(ms), Memory Usage: 14(MB)
"""

class Solution:
    def divisorGame(self, N: int) -> bool:
        return (N-1)%2 != 0
