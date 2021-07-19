"""
Question Link: https://leetcode.com/problems/create-target-array-in-the-given-order/
Difficulty: Easy
Related Topics: Array
Solved by 03.12.2021 
Runtime: 32(ms), Memory Usage: 14.3(MB)
"""

class Solution:
    def createTargetArray(self, nums, index):
        result = []
        for num, idx in zip(nums, index):
            result.insert(idx, num)
        return result
