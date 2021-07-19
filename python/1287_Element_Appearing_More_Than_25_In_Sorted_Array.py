"""
Question Link: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
Difficulty: Easy
Related Topics: Array
Solved by 10.30.2020 
Runtime: 100(ms), Memory Usage: 15.2(MB)
"""
import collections

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq = collections.Counter(arr)
        return sorted(freq, key=lambda x: freq[x], reverse=True)[0]
