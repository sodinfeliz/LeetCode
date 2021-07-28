"""
Question Link: https://leetcode.com/problems/di-string-match/
Difficulty: Easy
Related Topics: Array, Math, String, Two Pointers
Solved by 07.28.2021
Runtime: 60(ms), Memory Usage: 15(MB)
"""

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        lptr, rptr = 0, len(s)
        result = []
        for ch in s:
            if ch == 'D':
                result.append(rptr)
                rptr -= 1
            else:
                result.append(lptr)
                lptr += 1
        result.append(lptr) # lptr and rptr will meet after iteration
        return result
