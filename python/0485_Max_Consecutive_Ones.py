"""
Question Link: https://leetcode.com/problems/max-consecutive-ones/
Difficulty: Easy
Related Topics: Array
Solved by 10.15.2020 
Runtime: 328(ms), Memory Usage: 14.4(MB)
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        curent_len = 0
        for bit in nums:
            if bit == 1:
                curent_len += 1
            else:
                max_len = max(max_len, curent_len)
                curent_len = 0
        return max(max_len, curent_len)
