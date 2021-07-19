"""
Question Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
Difficulty: Easy
Related Topics: Bit Manipulation
Solved by 07.16.2020 
Runtime: 32(ms), Memory Usage: 13.6(MB)
"""
import collections

class Solution:
    def numberOfSteps (self, num: int) -> int:
        bin_num = bin(num)[2:]
        return collections.Counter(bin_num)['1'] + len(bin_num) - 1
