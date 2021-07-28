"""
Question Link: https://leetcode.com/problems/check-if-the-sentence-is-pangram/
Difficulty: Easy
Related Topics: Hash Table, String
Solved by 07.23.2021
Runtime: 28(ms), Memory Usage: 14(MB)
"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return False if len(set(sentence)) < 26 else True