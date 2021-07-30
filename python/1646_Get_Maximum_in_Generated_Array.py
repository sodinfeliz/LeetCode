"""
Question Link: https://leetcode.com/problems/get-maximum-in-generated-array/
Difficulty: Easy
Related Topics: Array, DP
Solved by 07.29.2021
Runtime: 32(ms), Memory Usage: 14.3(MB)
"""

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2: return n
        arr, maximum = [0, 1], 1
        for i in range(2, n+1): # O(n)
            hf = i>>1
            if i % 2 == 0:
                arr.append(arr[hf])
            else:
                arr.append(arr[hf] + arr[hf+1])
            if arr[i] > maximum:
                maximum = arr[i]
        return maximum
