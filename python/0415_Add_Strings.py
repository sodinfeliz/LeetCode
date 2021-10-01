"""
Question Link: https://leetcode.com/problems/add-strings/
Difficulty: Easy
Related Topics: String, Math
Solved by 08.19.2021
Runtime: 28(ms), Memory Usage: 14.4(MB)
"""

# Runtime: 40(ms)(63.57%), Memory Usage: 14.4(MB)(36.04%)
# Time complexity: O(n), Space Complexity: O(n)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        max_len = max(len(num1), len(num2))
        num1 = num1.rjust(max_len, '0')
        num2 = num2.rjust(max_len, '0')
        
        result, remainder = '', 0
        for d1, d2 in zip(num1[::-1], num2[::-1]):
            remainder += ord(d1) + ord(d2) - 2*ord('0')
            result += chr(ord('0') + remainder%10)
            remainder //= 10
        if remainder:
            result += chr(ord('0') + remainder)
            
        return result[::-1]

# Runtime: 28(ms)(95.98%), Memory Usage: 14.4(MB)(61.12%)
# Time complexity: O(n), Space Complexity: O(1)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ptr1, ptr2 = len(num1)-1, len(num2)-1
        result, remainder = '', 0
        
        while ptr1 >= 0 or ptr2 >= 0:
            if ptr1 >= 0:
                remainder += ord(num1[ptr1]) - ord('0')
                ptr1 -= 1
            if ptr2 >= 0:
                remainder += ord(num2[ptr2]) - ord('0')
                ptr2 -= 1
            result += chr(ord('0') + remainder%10)
            remainder //= 10
            
        if remainder:
            result += chr(ord('0') + remainder)
            
        return result[::-1]
