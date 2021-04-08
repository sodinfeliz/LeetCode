"""
Question Link: https://leetcode.com/problems/summary-ranges/
Difficulty: Easy
Related Topics: Array
Solved by 10.28.2020 
Runtime: 28(ms), Memory Usage: 14.1(MB)
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not len(nums):
            return []

        start = end = nums[0]
        result = []

        for num in nums[1:]:
            if num != end+1:
                result.append(f"{start}" + (start!=end)*f"->{end}")
                start = num
            end = num

        result.append(f"{start}" + (start!=end)*f"->{end}")
        return result
