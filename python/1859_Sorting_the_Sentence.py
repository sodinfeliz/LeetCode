"""
Question Link: https://leetcode.com/problems/sorting-the-sentence/
Difficulty: Easy
Related Topics: Sorting, String
Solved by 09.30.2021
Runtime: 32(ms), Memory Usage: 14.3(MB)
"""

# Runtime: 32(ms)(59.94%), Memory Usage: 14.3(MB)(45.57%)
class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        s.sort(key=lambda w: w[-1])
        return ' '.join([word[:-1] for word in s])

# Most voted Python code, Author: @rock
#   reversed the input string so that the 
#   digits appear in front of each word
class Solution:
    def sortSentence(self, s: str) -> str:
        words = s[::-1].split()
        words.sort()
        result = [ word[1:][::-1] for word in words ]
        return ' '.join(result)
