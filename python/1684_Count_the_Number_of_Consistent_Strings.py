"""
Question Link: https://leetcode.com/problems/count-the-number-of-consistent-strings/
Difficulty: Easy
Related Topics: Array, Hash Table, String, Bit Manipulation
Solved by 07.27.2021 
Runtime: 204(ms), Memory Usage: 16.1(MB)
"""

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            consistent = True
            for ch in word:
                if ch not in allowed:
                    consistent = False
                    break
            if consistent:
                count += 1
        return count
