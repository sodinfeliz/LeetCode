"""
Question Link: https://leetcode.com/problems/reformat-phone-number/
Difficulty: Easy
Related Topics: String
Solved by 09.30.2021 
Runtime: 20(ms), Memory Usage: 14.2(MB)
"""

# Runtime: 20(ms)(99.4%), Memory Usage: 14.2(MB)(49.8%)
class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', '').replace('-', '')
        result, ptr = [], 0
        while len(number) - ptr > 4:
            result.append(number[ptr: ptr+3])
            ptr += 3
        
        if len(number) - ptr < 4:
            result.append(number[ptr:])
        else:
            result.append(number[ptr: ptr+2])
            result.append(number[ptr+2:])
            
        return '-'.join(result)
