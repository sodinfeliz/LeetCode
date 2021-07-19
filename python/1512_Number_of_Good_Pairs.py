"""
Question Link: https://leetcode.com/problems/number-of-good-pairs/
Difficulty: Easy
Related Topics: Array, Hash Table
Solved by 07.15.2020 
Runtime: 44(ms), Memory Usage: 14(MB)
"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        def freq(num):
            if num < 2:
                return 0
            elif num:
                return num * (num - 1) // 2
        
        sum = 0
        for elem in set(nums):
            sum += freq(nums.count(elem))
            
        return sum
