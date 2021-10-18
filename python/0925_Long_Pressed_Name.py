"""
Question Link: https://leetcode.com/problems/long-pressed-name/
Difficulty: Easy
Related Topics: Two Pointers, String
Solved by 10.14.2021
Runtime: 32(ms), Memory Usage: 14.4(MB)
"""

# Runtime: 32(ms)(36.5%), Memory Usage: 14.4(MB)(30.37%)
# Most voted solution, Author: @lee215
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j-1]:
                return False
        return i == len(name)
