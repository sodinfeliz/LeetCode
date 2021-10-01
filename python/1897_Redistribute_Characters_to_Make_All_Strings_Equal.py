"""
Question Link: https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/
Difficulty: Easy
Related Topics: Hash Table, String, Counting
Solved by 09.14.2021
Runtime: 108(ms), Memory Usage: 14.1(MB)
"""

# Runtime: 108(ms)(6.98%), Memory Usage: 14.1(MB)(96.78%)
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = collections.defaultdict(int)
        for word in words:
            for ch in word:
                count[ch] += 1
        for ch, v in count.items():
            if v % len(words) != 0:
                return False
        return True
