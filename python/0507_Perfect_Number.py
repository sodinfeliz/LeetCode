"""
Question Link: https://leetcode.com/problems/perfect-number/
Difficulty: Easy
Related Topics: Math
Solved by 10.18.2021
Runtime: 64(ms), Memory Usage: 14.2(MB)
"""

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1: return False
        
        divisors = [1]
        for d in range(2, int(num**.5)+1):
            if num % d == 0:
                divisors.extend(set([d, num//d]))
        
        return sum(divisors) == num
