"""
Question Link: https://leetcode.com/problems/valid-anagram/
Difficulty: Easy
Related Topics: Hash Table, Sorting, String
Solved by 09.08.2021
Runtime: 44(ms), Memory Usage: 15.1(MB)
"""

# Runtime: 44(ms)(80.85%), Memory Usage: 15.1(MB)(5.89%)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s, t = list(s), list(t)
        s.sort()
        t.sort()
        return s == t

# Runtime: 56(ms)(39.69%), Memory Usage: 14.5(MB)(82.14%)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        table = collections.Counter(s)
        for ch in t:
            if ch not in table:
                return False
            else:
                table[ch] -= 1;
        for _, v in table.items():
            if v != 0:
                return False
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return collections.Counter(s) == collections.Counter(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        NO_OF_CHAR = 256
        table = [0] * NO_OF_CHAR
        for i in range(len(s)):
            table[ord(s[i])] += 1
            table[ord(t[i])] -= 1
        
        for v in table:
            if v != 0:
                return False
        return True
