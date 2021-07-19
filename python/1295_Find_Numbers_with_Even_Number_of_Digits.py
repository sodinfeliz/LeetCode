"""
Question Link: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
Difficulty: Easy
Related Topics: Array
Solved by 07.26.2020 
Runtime: 56(ms), Memory Usage: 13.9(MB)
"""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([len(str(num))%2==0 for num in nums])
