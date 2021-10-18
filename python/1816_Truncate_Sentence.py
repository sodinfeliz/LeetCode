"""
Question Link: https://leetcode.com/problems/truncate-sentence/
Difficulty: Easy
Related Topics: Array, String
Solved by 10.13.2021
Runtime: 43(ms), Memory Usage: 14.1(MB)
"""

# Runtime: 43(ms)(21.84%), Memory Usage: 14.1(MB)(92.46%)
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])
