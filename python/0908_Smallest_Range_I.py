"""
Question Link: https://leetcode.com/problems/smallest-range-i/
Difficulty: Easy
Related Topics: Array, Math
Solved by 07.27.2021
Runtime: 112(ms), Memory Usage: 15.2(MB)
"""

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(max(nums) - min(nums) - 2*k, 0)
