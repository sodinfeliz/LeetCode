"""
Question Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
Difficulty: Medium
Related Topics: String, Stack
Solved by 09.14.2021
Runtime: 168(ms), Memory Usage: 19.3(MB)
"""

# Runtime: 168(ms)(28.94%), Memory Usage: 19.3(MB)(17.8%)
# Most voted post, Author: @lee215
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        res = [['#', 1]]
        for ch in s:
            if res[-1][0] == ch:
                res[-1][1] += 1
            else:
                res.append([ch, 1])
            if res[-1][1] == k:
                res.pop()
        return ''.join([ch*r for ch, r in res[1:]])
