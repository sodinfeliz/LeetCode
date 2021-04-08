"""
Question Link: https://leetcode.com/problems/maximum-number-of-balloons/
Difficulty: Easy
Related Topics: String, Hash Table
Solved by 07.30.2020
Runtime: 32(ms), Memory Usage: 13.8(MB)
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for ch in text:
            if ch in count:
                count[ch] += 1
        return min(count['b'], count['a'], count['l']//2, count['o']//2, count['n'])
