"""
Question Link: https://leetcode.com/problems/consecutive-characters/
Difficulty: Easy
Related Topics: String
Solved by 11.03.2020 
Runtime: 40(ms), Memory Usage: 14.1(MB)
"""

class Solution:
    def maxPower(self, s: str) -> int:
        maxLen = currLen = 1
        currCh = s[0]
        for ch in s[1:]:
            if ch == currCh:
                currLen += 1
            else:
                maxLen = max(maxLen, currLen)
                currLen = 1
                currCh = ch
        return max(maxLen, currLen)
