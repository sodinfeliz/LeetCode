"""
Question Link: https://leetcode.com/problems/palindrome-partitioning/
Difficulty: Medium
Related Topics: String, DP, Back Tracking
Solved by 08.03.2021
Runtime: 664(ms), Memory Usage: 26.6(MB)
"""

# Runtime: 664(ms)(74.43%), Memory Usage: 26.6(MB)(88.83%)
# DPS and Backtracking
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.is_palindrome = lambda s: s == s[::-1]
        self.result = []
        self.helper(s, [])
        return self.result
        
    def helper(self, s, path):
        if not s:
            self.result.append(path)
            return
        for i in range(1, len(s)+1):
            if self.is_palindrome(s[:i]):
                self.helper(s[i:], path + [s[:i]])