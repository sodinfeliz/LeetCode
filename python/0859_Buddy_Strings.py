"""
Question Link: https://leetcode.com/problems/buddy-strings/
Difficulty: Easy
Related Topics: Hash Table, String
Solved by 10.07.2021
Runtime: 36(ms), Memory Usage: 14.7(MB)
"""

# Runtime: 36(ms)(60.02%), Memory Usage: 14.7(MB)(12.21%)
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        ind = []
        for i, (ch1, ch2) in enumerate(zip(s, goal)):
            if ch1 != ch2:
                ind.append(i)
                
        if len(ind) == 0 and len(set(s)) < len(s):
            return True
        elif len(ind) == 2 and s[ind[0]] == goal[ind[1]] and s[ind[1]] == goal[ind[0]]:
            return True
        else:
            return False
