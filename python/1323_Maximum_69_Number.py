"""
Question Link: https://leetcode.com/problems/maximum-69-number/
Difficulty: Easy
Related Topics: Math
Solved by 07.17.2020 
Runtime: 28(ms), Memory Usage: 13.6(MB)
"""

class Solution:
    def maximum69Number (self, num: int) -> int:
        org_num = num
        place = 1
        diff = 0

        while num != 0:
            num, digit = num // 10, num %10
            if digit == 6:
                diff = place * 3
            place *=10

        return org_num + diff

# one-line
class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))
