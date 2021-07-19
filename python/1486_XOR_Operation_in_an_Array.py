"""
Question Link: https://leetcode.com/problems/xor-operation-in-an-array/
Difficulty: Easy
Related Topics: Array, Bit Manipulation
Solved by 07.18.2020 
Runtime: 28(ms), Memory Usage: 13.7(MB)
"""

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = start
        current_value = start
        for _ in range(n-1):
            current_value += 2
            result ^= current_value
        return result
