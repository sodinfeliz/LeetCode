"""
Question Link: https://leetcode.com/problems/rotate-array/
Difficulty: Medium
Related Topics: Array, Math, Two Pointers
Solved by 01.25.2022
"""

# Runtime: 291(ms)(45.96%), Memory Usage: 25.4(MB)(96.71%)
# Time complexity: O(n), Space Complexity: O(n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k == 0: return
    
        new_nums = nums[-k:] + nums[:-k]
        for i in range(len(nums)):
            nums[i] = new_nums[i]

