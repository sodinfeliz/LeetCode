"""
Question Link: https://leetcode.com/problems/find-lucky-integer-in-an-array/
Difficulty: Easy
Related Topics: Array
Solved by 07.23.2020 
Runtime: 68(ms), Memory Usage: 13.9(MB)
"""

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for i in arr:
            freq[i] = freq.get(i, 0) + 1
        try:
            return max(filter(lambda k: k==freq[k], freq))
        except ValueError:
            return -1
