"""
Question Link: https://leetcode.com/problems/shuffle-the-array/
Difficulty: Easy
Related Topics: Array
Solved by 07.15.2020 
Runtime: 96(ms), Memory Usage: 14(MB)
"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for pair in zip(nums[:len(nums)//2], nums[len(nums)//2:]):
            result += list(pair)
        return result
