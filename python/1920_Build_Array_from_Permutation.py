"""
Question Link: https://leetcode.com/problems/build-array-from-permutation/
Difficulty: Easy
Related Topics: Array, Simulation
Solved by 11.02.2021
Runtime: 124(ms), Memory Usage: 14.6(MB)
"""

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[num] for num in nums]
