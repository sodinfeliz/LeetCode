"""
Question Link: https://leetcode.com/problems/increasing-decreasing-string/
Difficulty: Easy
Related Topics: String, Hash Table
Solved by 07.23.2020 
Runtime: 44(ms), Memory Usage: 14.1(MB)
"""

class Solution:
    def sortString(self, s: str) -> str:
        # Hashtable contruction
        htable = dict()
        for ch in s:
            htable[ch] = htable.get(ch, 0) + 1
        alpha = sorted(htable)
        
        if len(alpha) == 1: return s
        
        # Iterate Increasing/Decreasing
        result, step = "", 1
        all_zero = False
        
        while not all_zero:
            all_zero = True
            for ch in alpha[::step]:
                if htable[ch] > 0:
                    result += ch
                    htable[ch] -= 1
                    all_zero = False
            
            step = -step
                    
        return result