"""
Question Link: https://leetcode.com/problems/defuse-the-bomb/
Difficulty: Easy
Related Topics: Array
Solved by 11.26.2020 
Runtime: 40(ms), Memory Usage: 14.3(MB)
"""

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0]*len(code)
        
        dcode = code + code
        shift = len(code) if k < 0 else 0
        sign = k // abs(k)
        
        return [sum(dcode[shift+i+sign: shift+i+sign+k: sign]) for i in range(len(code))]
