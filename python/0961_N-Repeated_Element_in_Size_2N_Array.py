"""
Question Link: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
Difficulty: Easy
Related Topics: Array, Hash Table
Solved by 01.11.2022
Runtime: 311(ms), Memory Usage: 15.6(MB)
"""

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        unique = []
        for num in nums:
            if num not in unique:
                unique.append(num)
            else:
                return num
