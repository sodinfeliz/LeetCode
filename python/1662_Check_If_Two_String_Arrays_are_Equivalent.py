"""
Question Link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
Difficulty: Easy
Related Topics: Array, String
Solved by 09.13.2021
Runtime: 32(ms), Memory Usage: 14.3(MB)
"""

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
