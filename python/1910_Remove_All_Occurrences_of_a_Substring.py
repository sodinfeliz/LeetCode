"""
Question Link: https://leetcode.com/problems/remove-all-occurrences-of-a-substring/
Difficulty: Medium
Related Topics: String
Solved by 09.14.2021
Runtime: 61(ms), Memory Usage: 14.5(MB)
"""

# Runtime: 59(ms), Memory Usage: 14.2(MB)
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if len(s) < len(part):
            return s
        res = []
        COMP_NUM = len(part)-1
        for ch in s:
            if ch == part[-1]:
                if COMP_NUM == 0:
                    continue
                elif ''.join(res[-COMP_NUM:]) == part[:-1]:
                    res[-COMP_NUM:] = []
                else:
                    res.append(ch)
            else:
                res.append(ch)
        return ''.join(res)

# Runtime: 39(ms), Memory Usage: 14.3(MB)
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, '', 1)
        return s

# Runtime: 39(ms), Memory Usage: 14.4(MB)
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res = ''
        for ch in s:
            res += ch
            if res[-len(part):] == part:
                res = res[:-len(part)]
        return res
