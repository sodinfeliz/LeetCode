"""
Question Link: https://leetcode.com/problems/decompress-run-length-encoded-list/
Difficulty: Easy
Related Topics: Array
Solved by 07.15.2020
Runtime: 72(ms), Memory Usage: 14(MB)
"""

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)//2):
            freq, val = nums[2*i:2*i+2]
            result.extend([val]*freq)
        return result