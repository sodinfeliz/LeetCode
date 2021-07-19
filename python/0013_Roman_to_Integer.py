"""
Question Link: https://leetcode.com/problems/roman-to-integer/
Difficulty: Easy
Related Topics: String
Solved by 07.16.2020 
Runtime: 44(ms), Memory Usage: 13.9(MB)
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        c = 0
        summation = 0
        for i in range(len(s)):
            if roman[s[~i]] < c:
                summation -= roman[s[~i]]
            else:
                c = roman[s[~i]]
                summation += c
        return summation
