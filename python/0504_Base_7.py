"""
Question Link: https://leetcode.com/problems/base-7/
Difficulty: Easy
Related Topics: Math
Solved by 10.18.2021
Runtime: 32(ms), Memory Usage: 14.3(MB)
"""

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"
        
        sgn = '' if num >= 0 else '-'
        num, out = abs(num), ''
        while num > 0:
            num, r = divmod(num, 7)
            out = str(r) + out
            
        return f'{sgn}{out}'
