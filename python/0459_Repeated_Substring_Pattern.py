"""
Question Link: https://leetcode.com/problems/repeated-substring-pattern/
Difficulty: Easy
Related Topics: String
Solved by 09.14.2021
Runtime: 52(ms), Memory Usage: 14.5(MB)
"""

# Runtime: 52(ms)(68.88%), Memory Usage: 14.5(MB)(11.58%)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)//2):
            if len(s) % (i+1) == 0 and s[:i+1]*(len(s)//(i+1)) == s:
                return True
        return False
