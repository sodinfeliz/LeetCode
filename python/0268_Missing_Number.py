"""
Question Link: https://leetcode.com/problems/missing-number/
Difficulty: Easy
Related Topics: Math
Solved by 10.30.2020 
Runtime: 116(ms), Memory Usage: 15.1(MB)
"""

# gauss formula
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums)*(len(nums)+1)//2 - sum(nums)
