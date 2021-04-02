"""
Question Link: https://leetcode.com/problems/plus-one/
Difficulty: Easy
Related Topics: Array
Solved by 07.20.2020 
Runtime: 40(ms), Memory Usage: 14(MB)
"""

class Solution:
    def plusOne(self, digits):
        num = int(('').join(map(str, digits)))
        return [int(ch) for ch in str(num+1)]

# recursive method
class Solution2:
    def plusOne(self, digits):
        if len(digits) == 1 and digits[0] == 9:
            return [1, 0]

        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits[:-1])
            return digits
