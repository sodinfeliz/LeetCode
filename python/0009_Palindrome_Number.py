"""
Question Link: https://leetcode.com/problems/palindrome-number/
Difficulty: Easy
Related Topics: Math
Solved by 10.30.2020 
Runtime: 64(ms), Memory Usage: 14.2(MB)
"""

# converting to string method
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            for ch1, ch2 in zip(str(x), str(x)[::-1]):
                if ch1 != ch2:
                    return False
            return True

# no converting
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        
        result = 0
        while x > result:
            result = result * 10 + x % 10
            x //= 10

        return True if x == result or result // 10 == x else False