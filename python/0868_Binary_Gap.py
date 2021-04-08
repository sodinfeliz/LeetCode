"""
Question Link: https://leetcode.com/problems/binary-gap/
Difficulty: Easy
Related Topics: Math
Solved by 10.27.2020 
Runtime: 32(ms), Memory Usage: 14.1(MB)
"""

class Solution:
    def binaryGap(self, n: int) -> int:
        bin_num = list(bin(n)[2:])
        max_d = 0
        step = 0
        for bit in bin_num[1:]:
            step += 1
            if bit == '1':
                max_d = max(max_d, step)
                step = 0
        return max_d
