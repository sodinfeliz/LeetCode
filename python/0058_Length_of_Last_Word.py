"""
Question Link: https://leetcode.com/problems/length-of-last-word/
Difficulty: Easy
Related Topics: String
Solved by 10.29.2020 
Runtime: 24(ms), Memory Usage: 14.2(MB)
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for ch in s.strip()[::-1]:
            if ch.isalpha():
                length += 1
            else:
                break
        return length