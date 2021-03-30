"""
Related Topics: Array, Divide and Conquer, Dynamic Programming
Language: Python
Solved by 11.02.2020 
Runtime: 60(ms), Memory Usage: 14.8(MB)
"""

class Solution:
    #
    def maxSubArray(self, nums) -> int:
        lmax = gmax = nums[0]
        for i in range(1, len(nums)):
            lmax = max(nums[i], lmax+nums[i])
            if lmax > gmax:
                gmax = lmax
        return gmax