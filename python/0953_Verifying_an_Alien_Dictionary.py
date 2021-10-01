"""
Question Link: https://leetcode.com/problems/verifying-an-alien-dictionary/
Difficulty: Easy
Related Topics: Array, Hash Table, String
Solved by 09.14.2021
Runtime: 63(ms), Memory Usage: 14.1(MB)
"""

# Runtime: 63(ms)(7.92%), Memory Usage: 14.1(MB)(97.99%)
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            equal_prefix = True
            for ch1, ch2 in zip(word1, word2):
                if order.index(ch1) < order.index(ch2):
                    equal_prefix = False
                    break
                if order.index(ch1) > order.index(ch2):
                    return False
            if equal_prefix and len(word1) > len(word2):
                return False
        return True
