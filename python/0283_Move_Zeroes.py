"""
Question Link: https://leetcode.com/problems/move-zeroes/
Difficulty: Easy
Related Topics: Array
Solved by 07.29.2020 
Runtime: 52(ms), Memory Usage: 15.1(MB)
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        total_zeros = 0
        while index != (len(nums) - 1):
            if total_zeros + index >= len(nums):
                break 
            elif nums[index] == 0:
                nums.append(nums.pop(index))
                total_zeros += 1 
            else:
                index += 1
