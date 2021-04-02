"""
Question Link: https://leetcode.com/problems/richest-customer-wealth/
Difficulty: Easy
Related Topics: Array
Solved by 01.15.2021 
Runtime: 56(ms), Memory Usage: 14.3(MB)
"""

class Solution:
    def maximumWealth(self, accounts) -> int:
        mm = 0
        for person in accounts:
            if sum(person) > mm:
                mm = sum(person)
        return mm
