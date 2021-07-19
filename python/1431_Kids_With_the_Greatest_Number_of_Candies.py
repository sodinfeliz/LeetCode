"""
Question Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
Difficulty: Easy
Related Topics: Array
Solved by 07.21.2020 
Runtime: 56(ms), Memory Usage: 13.7(MB)
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        return [i - maximum + extraCandies >= 0 for i in candies]
