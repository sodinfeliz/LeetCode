"""
Question Link: https://leetcode.com/problems/valid-number/
Difficulty: Hard
Related Topics: Math, String
Solved by 10.23.2020 
Runtime: 32(ms), Memory Usage: 14.2(MB)
"""

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip(' ')
        if 'e' in s:
            digit, exp = s.split('e', 1)
        else:
            digit, exp = s, None

        if digit is '' or exp is '':
            return False
        # checking for digit
        if digit[0] == '+' or digit[0] == '-':
            digit = digit[1:]
        if not digit.replace('.', '', 1).isnumeric():
            return False

        # cehcking for exp
        if exp is not None:
            if exp[0] == '+' or exp[0] == '-':
                exp = exp[1:]
            if not exp.isnumeric():
                return False

        return True
