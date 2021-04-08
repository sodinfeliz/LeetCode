"""
Question Link: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
Difficulty: Easy
Related Topics: Array, Sort
Solved by 07.24.2020 
Runtime: 32(ms), Memory Usage: 13.9(MB)
"""

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) == 2: return True
    
        arr = sorted(arr)
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True
