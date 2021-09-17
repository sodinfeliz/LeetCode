"""
Question Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/
Difficulty: Medium
Related Topics: Array, Hash Table
Solved by 09.07.2021
Runtime: 348(ms), Memory Usage: 21.9(MB)
"""

# Runtime: 348(ms)(82.33%), Memory Usage: 21.9(MB)(40.79%)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                result.append(abs(num))
            else:
                nums[idx] *= -1
        return result
