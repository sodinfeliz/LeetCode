"""
Question Link: https://leetcode.com/problems/reverse-string/
Difficulty: Easy
Related Topics: Two Pointers, String, Recursion
Solved by 10.08.2021
Runtime: 192(ms), Memory Usage: 18.4(MB)
"""

# Runtime: 192(ms)(91.89%), Memory Usage: 18.4(MB)(82.09%)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[-1-i] = s[-1-i], s[i]
