"""
Question Link: https://leetcode.com/problems/detect-capital/
Difficulty: Easy
Related Topics: Array, Sorting, Greedy
Solved by 07.27.2021
Runtime: 260(ms), Memory Usage: 16.8(MB)
"""

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums, total = sorted(nums), 0
        for index in range(0,len(nums),2):
            total += nums[index]
        return total
