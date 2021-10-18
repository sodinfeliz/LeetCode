"""
Question Link: https://leetcode.com/problems/maximum-number-of-words-you-can-type/
Difficulty: Easy
Related Topics: Hash Table. String
Solved by 10.08.2021
Runtime: 36(ms), Memory Usage: 14.4(MB)
"""

# Runtime: 36(ms)(43.59%), Memory Usage: 14.4(MB)(59.01%)
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        for word in text.split():
            if not set(word).intersection(brokenLetters):
                count += 1
        return count
