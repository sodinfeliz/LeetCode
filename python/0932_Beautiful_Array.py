"""
Question Link: https://leetcode.com/problems/beautiful-array/
Difficulty: Medium
Related Topics: Array, Math, Divide and Conquer
Solved by 07.29.2021
Runtime: 560(ms), Memory Usage: 14.4(MB)
"""

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        if n == 1: return [1]
        result = [1]
        for i in range(2, n+1):
            arr = []
            for j in result:
                odd = 2*j -1
                if odd <= i:
                    arr.append(odd)
            for j in result:
                even = 2*j
                if even <= i:
                    arr.append(even)
            result = arr
        return result
