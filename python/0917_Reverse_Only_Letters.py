"""
Question Link: https://leetcode.com/problems/reverse-only-letters/
Difficulty: Easy
Related Topics: String
Solved by 10.28.2020 
Runtime: 28(ms), Memory Usage: 14(MB)
"""

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        result = ''
        right = len(S) - 1

        for ch in S:
            if ch.isalpha():
                while not S[right].isalpha():
                    right -= 1
                result += S[right]
                right -= 1
            else:
                result += ch

        return result
