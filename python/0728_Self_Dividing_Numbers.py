"""
Question Link: https://leetcode.com/problems/self-dividing-numbers/
Difficulty: Easy
Related Topics: Math
Solved by 10.30.2020 
Runtime: 60(ms), Memory Usage: 14(MB)
"""

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right+1):
						# skip the lopp if num contains digit 0
            if '0' in str(num):
                continue

            digits = set(map(int, str(num)))
            match = True
            for digit in digits:
                if num % digit != 0:
                    match = False
                    break
            if match:
                result.append(num)
        return result
