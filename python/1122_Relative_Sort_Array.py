"""
Question Link: https://leetcode.com/problems/relative-sort-array/
Difficulty: Easy
Related Topics: Array, Sort
Solved by 07.16.2020 
Runtime: 40(ms), Memory Usage: 14.1(MB)
"""

# Runtime: 40(ms), Memory Usage: 14.1(MB)
import collections
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        elem1 = collections.Counter(arr1)
        for i in arr2:
            result.extend([i]*elem1[i])
        for i in sorted(set(arr1) - set(arr2)):
            result.extend([i]*elem1[i])
        return result
