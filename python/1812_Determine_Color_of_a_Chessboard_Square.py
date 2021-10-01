"""
Question Link: https://leetcode.com/problems/determine-color-of-a-chessboard-square/
Difficulty: Easy
Related Topics: String, Math
Solved by 09.13.2021
Runtime: 28(ms), Memory Usage: 14.1(MB)
"""

# Runtime: 28(ms)(83.76%), Memory Usage: 14.1(MB)(66.44%)
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        count = ord('a') - ord(coordinates[0]) + \
                ord('1') - ord(coordinates[1])
        return False if count % 2 == 0 else True
