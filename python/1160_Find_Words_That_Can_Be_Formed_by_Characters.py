"""
Question Link: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
Difficulty: Easy
Related Topics: Array, Hash Table
Solved by 03.12.2021
Runtime: 156(ms), Memory Usage: 14.6(MB)
"""

from collections import Counter
class Solution:
    def countCharacters(self, words, chars: str):
        ds = Counter(chars)
        count = 0
        for word in words:
            flag = 1
            for k, v in Counter(word).items():
                if k not in ds or v > ds[k]:
                    flag = 0
                    break
            count += (len(word) if flag else 0)
        return count
