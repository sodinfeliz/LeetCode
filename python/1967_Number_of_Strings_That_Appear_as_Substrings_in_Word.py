"""
Question Link: https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
Difficulty: Easy
Related Topics: String
Solved by 09.13.2021
Runtime: 32(ms), Memory Usage: 14.2(MB)
"""

# Runtime: 32(ms)(91.34%), Memory Usage: 14.2(MB)(68.61%)
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum([1 for pat in patterns if pat in word])
