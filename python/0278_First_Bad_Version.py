"""
Question Link: https://leetcode.com/problems/first-bad-version/
Difficulty: Easy
Related Topics: Binary Search
Solved by 01.24.2022
Runtime: 45(ms), Memory Usage: 14.3(MB)
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 0, n
        while low < high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low
