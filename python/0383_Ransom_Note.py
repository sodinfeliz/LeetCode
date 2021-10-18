"""
Question Link: https://leetcode.com/problems/ransom-note/
Difficulty: Easy
Related Topics: Hash Table, String, Counting
Solved by 10.15.2021
Runtime: 65(ms), Memory Usage: 14.4(MB)
"""

# Runtime: 65(ms)(57.66%), Memory Usage: 14.4(MB)(63.36%)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        dictm = collections.Counter(magazine)
        dictr = collections.Counter(ransomNote)
        for k, v in dictr.items():
            if k not in dictm or dictr[k] > dictm[k]:
                return False
        return True
