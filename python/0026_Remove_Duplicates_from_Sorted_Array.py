"""
Question Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Difficulty: Easy
Related Topics: Array, Two Pointers
Solved by 07.01.2021
Runtime: 88(ms), Memory Usage: 15.6(MB)
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count, num = 0, None
        for idx, elem in enumerate(nums):
            if elem == num:
                nums[idx] = '_'
            else:
                nums[count], nums[idx] = nums[idx], nums[count]
                count += 1
                num = elem
        return count
