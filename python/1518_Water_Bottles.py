"""
Question Link: https://leetcode.com/problems/water-bottles/
Difficulty: Easy
Related Topics: Math
Solved by 07.31.2021
Runtime: 16(ms), Memory Usage: 14.2(MB)
"""

# Runtime: 16(ms)(100%), Memory Usage: 14.2(MB)(72.35%)
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        while numBottles >= numExchange:
            next_exchange = numBottles // numExchange
            numBottles = numBottles % numExchange + next_exchange
            total += next_exchange
        return total
