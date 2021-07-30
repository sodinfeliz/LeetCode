"""
Question Link: https://leetcode.com/problems/n-th-tribonacci-number/
Difficulty: Easy
Related Topics: Math, DP
Solved by 07.30.2021
Runtime: 28(ms), Memory Usage: 14.2(MB)
"""

# Time complexity: O(n), Space Complexity: O(n)
class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0, 1, 1]
        if n < 3: return arr[n]
        
        for i in range(3, n+1):
            arr.append(arr[i-1] + arr[i-2] + arr[i-3])
        return arr[-1]
