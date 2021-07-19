"""
Question Link: https://leetcode.com/problems/running-sum-of-1d-array/
Difficulty: Easy
Related Topics: Array
Solved by 07.15.2020 
Runtime: 40(ms), Memory Usage: 14(MB)
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if result:
                result.append(num + result[-1])
            else:
                result.append(num)
        return result
