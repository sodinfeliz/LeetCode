"""
Question Link: https://leetcode.com/problems/minimum-absolute-difference/
Difficulty: Easy
Related Topics: Array
Solved by 07.23.2020
Runtime: 488(ms), Memory Usage: 27.7(MB)
"""

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        minimum = float('inf')
        result = []
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if diff < minimum:
                minimum = diff
                result = [[arr[i-1], arr[i]]]
            elif diff == minimum:
                result.append([arr[i-1], arr[i]])
        return result