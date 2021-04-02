"""
Question Link: https://leetcode.com/problems/find-the-highest-altitude/
Difficulty: Easy
Related Topics: Array
Solved by 03.12.2020 
Runtime: 36(ms), Memory Usage: 14.3(MB)
"""

class Solution:
    def largestAltitude(self, gain) -> int:
        highest = 0
        cur_high = 0
        for step in gain:
            cur_high += step
            if cur_high > highest:
                highest = cur_high
        return highest
