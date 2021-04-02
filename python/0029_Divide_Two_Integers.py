"""
Question Link: https://leetcode.com/problems/divide-two-integers/
Difficulty: Medium
Related Topics: Math, Binary Search
Solved by 07.17.2020 
Runtime: 60(ms), Memory Usage: 13.9(MB)
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (-1)**(dividend * divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        if divisor == 1:
            return (2**31-1)*sign if dividend == 2**31 and sign > 0 else dividend*sign
        elif dividend < divisor:
            return 0

        low, high = 1, dividend
        while high - low > 1:
            mid = (low + high) // 2
            if mid * divisor > dividend:
                high = mid
            elif mid * divisor < dividend:
                low = mid
            else:
                return mid * sign

        return low * sign
