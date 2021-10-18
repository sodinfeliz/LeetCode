"""
Question Link: https://leetcode.com/problems/rotate-string/
Difficulty: Easy
Related Topics: String
Solved by 09.16.2021
Runtime: 24(ms), Memory Usage: 14.4(MB)
"""

# Runtime: 24(ms)(94.25%), Memory Usage: 14.4(MB)(11.46%)
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        find = False
        for i in range(len(s)):
            if s[:i] + s[i:] == goal or \
               s[i:] + s[:i] == goal:
                find = True
                break
            
        return find
