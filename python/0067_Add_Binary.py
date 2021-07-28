"""
Question Link: https://leetcode.com/problems/add-binary/
Difficulty: Easy
Related Topics: Math, String, Bit Manipulation
Solved by 07.23.2021
Runtime: 32(ms), Memory Usage: 14.4(MB)
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            a, b = b, a
        b = '0'*(len(a)-len(b)) + b
        
        result = ''
        carry = 0
        
        for d1, d2 in zip(a[::-1], b[::-1]):
            carry += ord(d1) + ord(d2) - 2*ord('0')
            result += str(carry%2)
            carry //= 2
        if carry: result += '1'
            
        return result[::-1]
