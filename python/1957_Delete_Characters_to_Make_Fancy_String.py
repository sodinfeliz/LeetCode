"""
Question Link: https://leetcode.com/problems/delete-characters-to-make-fancy-string/
Difficulty: Easy
Related Topics: String
Solved by 10.07.2021
Runtime: 404(ms), Memory Usage: 16.2(MB)
"""

# Runtime: 404(ms)(97.72%), Memory Usage: 16.2(MB)(84.42%)
class Solution:
    def makeFancyString(self, s: str) -> str:
        c, l = '', 0
        result = []
        for ch in s:
            if ch !=c:
                c, l = ch, 1
                result.append(ch)
            elif l < 2:
                l += 1
                result.append(ch)
        return ''.join(result)
