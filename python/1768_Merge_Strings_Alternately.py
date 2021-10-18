"""
Question Link: https://leetcode.com/problems/merge-strings-alternately/
Difficulty: Easy
Related Topics: String, Two Pointers
Solved by 09.15.2021
Runtime: 39(ms), Memory Usage: 14.4(MB)
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr, result = 0, ''
        while ptr < len(word1) and ptr < len(word2):
            result += f"{word1[ptr]}{word2[ptr]}"
            ptr += 1
        result += word1[ptr:] if len(word1) > len(word2) else word2[ptr:]
        return result

# Most voted post, Author: @lee215
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join([ch1 + ch2 for ch1, ch2 in itertools.zip_longest(word1, word2, fillvalue='')])
