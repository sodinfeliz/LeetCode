"""
Question Link: https://leetcode.com/problems/search-insert-position/
Difficulty: Easy
Related Topics: Array, Binary Search
Solved by 01.24.2022
Runtime: 69(ms), Memory Usage: 14.9(MB)
"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            else:
                low = mid + 1
        return low