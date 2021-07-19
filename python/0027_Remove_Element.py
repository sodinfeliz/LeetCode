"""
Question Link: https://leetcode.com/problems/remove-element/
Difficulty: Easy
Related Topics: Array, Two Pointers
Solved by 07.19.2021
Runtime: 28(ms), Memory Usage: 14.3(MB)
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for elem in nums:
            if elem != val:
                nums[k] = elem
                k += 1
        return k
