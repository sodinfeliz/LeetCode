"""
Question Link: https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/
Difficulty: Easy
Related Topics: String
Solved by 09.17.2021
Runtime: 58(ms), Memory Usage: 14.4(MB)
"""

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.convertToNumber(firstWord) + \
               self.convertToNumber(secondWord) == \
               self.convertToNumber(targetWord)
        
    def convertToNumber(self, s):
        total = 0
        for ch in s:
            total = total*10 + ord(ch) - ord('a')
        return total
