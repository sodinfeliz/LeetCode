"""
Question Link: https://leetcode.com/problems/maximum-number-of-balls-in-a-box/
Difficulty: Easy
Related Topics: Math, HashTable
Solved by 07.26.2021
Runtime: 460(ms), Memory Usage: 14.2(MB)
"""

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        htable = dict()
        for num in range(lowLimit, highLimit+1):
            total = 0
            while num != 0:
                total += num % 10
                num //= 10
            htable[total] = htable.get(total, 0) + 1
        return max(htable.values())
