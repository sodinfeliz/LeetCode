"""
Question Link: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
Difficulty: Easy
Related Topics: Array
Solved by 10.29.2020 
Runtime: 36(ms), Memory Usage: 14.2(MB)
"""

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        total = 0
        for i in range(n):
            total += (((n-i)*(i+1)+1)//2)*arr[i]
        return total
