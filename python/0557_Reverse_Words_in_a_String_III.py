"""
Question Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/
Difficulty: Easy
Related Topics: Two Pointers, String
Solved by 01.27.2022
Runtime: 43(ms), Memory Usage: 14.7(MB)
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words = list(map(lambda w: w[::-1], words))
        return ' '.join(words)


# Most voted Solution, Author: StefanPochmann
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])[::-1]
