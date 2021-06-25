"""
Question Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Difficulty: Medium
Related Topics: Array, Binary Search
Solved by 06.25.2021
Runtime: 84(ms), Memory Usage: 15.5(MB)
"""
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find(T, arr, left=0):
            right = len(arr)
            while left < right:
                mid = left + right >> 1
                if arr[mid] < T:
                    left = mid + 1
                else:
                    right = mid
            return left
        Tleft = find(target, nums)
        if Tleft == len(nums) or nums[Tleft] != target: return [-1, -1]
        return [Tleft, find(target+1, nums, Tleft) - 1]