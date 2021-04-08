"""
Question Link: https://leetcode.com/problems/defanging-an-ip-address/
Difficulty: Easy
Related Topics: String
Solved by 07.16.2020 
Runtime: 60(ms), Memory Usage: 14(MB)
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
