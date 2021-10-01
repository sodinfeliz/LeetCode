"""
Question Link: https://leetcode.com/problems/shuffle-string/
Difficulty: Easy
Related Topics: Array, String
Solved by 09.07.2021
Runtime: 56(ms), Memory Usage: 14.4(MB)
"""

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        idx = list(range(len(s)))
        idx.sort(key=lambda k: indices[k])
        return ''.join([s[elem] for elem in idx])
