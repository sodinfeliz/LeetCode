"""
Question Link: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
Difficulty: Easy
Related Topics: Array
Solved by 10.23.2020 
Runtime: 32(ms), Memory Usage: 14(MB)
"""

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        init = 1
        minimum = float("inf")
        for num in nums:
            init += num
            minimum = min(minimum, init)
        return 1 if minimum > 0 else 2 - minimum
