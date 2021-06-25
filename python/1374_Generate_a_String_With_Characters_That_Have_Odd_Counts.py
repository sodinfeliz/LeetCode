"""
Question Link: https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/
Difficulty: Easy
Related Topics: String
Solved by 10.28.2020 
Runtime: 24(ms), Memory Usage: 14(MB)
"""

class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            return 'x' + (n-1)*'y'
        else:
            return n*'x'