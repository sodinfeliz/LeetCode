"""
Question Link: https://leetcode.com/problems/is-subsequence/
Difficulty: Easy
Related Topics: Two Pointers, String, DP
Solved by 07.29.2021
Runtime: 20(ms), Memory Usage: 14.2(MB)
"""

# Time complexity: O(mn), Space Complexity: O(1)
# where m, n is the length of s, t respectively 
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        ptr = 0 # pointer of string s
        for ch in t:
            if s[ptr] == ch:
                ptr += 1
            if ptr == len(s):
                break
        return ptr == len(s)
