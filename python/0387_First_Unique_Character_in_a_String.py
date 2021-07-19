"""
Question Link: https://leetcode.com/problems/first-unique-character-in-a-string/
Difficulty: Easy
Related Topics: String, Hash Table
Solved by 11.06.2021
Runtime: 188(ms), Memory Usage: 14.3(MB)
"""

# Going through two times in loop (No hashtable)
# Runtime: 188(ms), Memory Usage: 14.3(MB)
# Time complexity: O(n), Space Complexity: O(1)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = [0]*26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        for i, ch in enumerate(s):
            if count[ord(ch) - ord('a')] == 1:
                return i
        return -1

# Going through two times in loop (No hashtable)
# Runtime: 252(ms)(16.83%), Memory Usage: 14.2(MB)
# Time complexity: O(n), Space Complexity: O(1)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = [0]*26
        pos = [-1]*26
        for i, ch in enumerate(s):
            count[ord(ch) - ord('a')] += 1
            pos[ord(ch) - ord('a')] = i
        
        uni_pos = float('Inf')
        for i, freq in enumerate(count):
            if freq == 1:
                uni_pos = min(uni_pos, pos[i])
        return uni_pos if uni_pos < len(s) else -1


# Runtime: 60(ms)(96.73%), Memory Usage: 14.3(MB)
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for k, freq in Counter(s).items():
            if freq == 1:
                return s.index(k)
        return -1
