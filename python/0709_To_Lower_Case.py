"""
Question Link: https://leetcode.com/problems/to-lower-case/
Difficulty: Easy
Related Topics: String
Solved by 11.06.2020 
Runtime: 28(ms), Memory Usage: 14(MB)
"""

class Solution:
    def toLowerCase(self, str: str) -> str:
        def is_upper(ch):
            return 65 <= ord(ch) <= 90
        
        result = ''
        for ch in str:
            result += chr(ord(ch) + 32) if is_upper(ch) else ch
        return result
