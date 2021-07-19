"""
Question Link: https://leetcode.com/problems/three-consecutive-odds/
Difficulty: Easy
Related Topics: Array
Solved by 10.29.2020 
Runtime: 48(ms), Memory Usage: 14.3(MB)
"""

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        roll = 0
        for num in arr:
            if num % 2 == 1:
                roll += 1
                if roll == 3:
                    return True
            else:
                roll = 0
        return False
