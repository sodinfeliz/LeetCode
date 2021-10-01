"""
Question Link: https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
Difficulty: Easy
Related Topics: Hash Table, String
Solved by 09.07.2021
Runtime: 40(ms), Memory Usage: 14.2(MB)
"""

# Runtime: 40(ms)(42.56%), Memory Usage: 14.2(MB)(87.04%)
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        tbl = dict()
        for ch in s:
            tbl[ch] = tbl.get(ch, 0) + 1
        
        check_value = tbl[s[0]]
        for v in tbl.values():
            if v != check_value:
                return False
        return True
