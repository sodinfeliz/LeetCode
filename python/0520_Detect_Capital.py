"""
Question Link: https://leetcode.com/problems/detect-capital/
Difficulty: Easy
Related Topics: String
Solved by 11.04.2020 
Runtime: 24(ms), Memory Usage: 14.2(MB)
"""

# Runtime: 24(ms), Memory Usage: 14.2(MB)
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        def isCapital(ch):
            return 65 <= ord(ch) <= 90

        if len(word) == 1:
            return True
        else:
            if isCapital(word[0]):
                if isCapital(word[1]):
                    for ch in word[2:]:
                        if not isCapital(ch): return False
                else:
                    for ch in word[2:]:
                        if isCapital(ch): return False 
            else:
                for ch in word[1:]:
                    if isCapital(ch): return False
        return True

# Using built-in function
# Runtime: 32(ms), Memory Usage: 14(MB)
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        else:
            if word[0].isupper():
                if word[1].isupper():
                    for ch in word[2:]:
                        if ch.islower(): return False
                else:
                    for ch in word[2:]:
                        if ch.isupper(): return False 
            else:
                for ch in word[1:]:
                    if ch.isupper(): return False
        return True

