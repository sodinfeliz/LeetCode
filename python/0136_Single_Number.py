"""
Question Link: https://leetcode.com/problems/single-number/
Difficulty: Easy
Related Topics: Hash Table, Bit Manipulation 
Solved by 07.16.2020 
Runtime: 112(ms), Memory Usage: 16.3(MB)
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for elem in nums:
            result = result ^ elem
        return result