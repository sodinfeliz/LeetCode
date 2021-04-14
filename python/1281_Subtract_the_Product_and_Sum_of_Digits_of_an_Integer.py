"""
Question Link: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
Difficulty: Easy
Related Topics: Math
Solved by 10.30.2020 
Runtime: 24(ms), Memory Usage: 14(MB)
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        summation = 0
        while n != 0:
            digit = n % 10
            n //= 10
            product *= digit
            summation += digit
        return product - summation

# one-liner
class Solution:
    def subtractProductAndSum(self, n):
        return eval('*'.join(str(n))) - eval('+'.join(str(n)))
