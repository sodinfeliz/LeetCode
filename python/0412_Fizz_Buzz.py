"""
Question Link: https://leetcode.com/problems/fizz-buzz/
Difficulty: Easy
Related Topics: String, Math
Solved by 07.28.2021
Runtime: 40(ms), Memory Usage: 15.1(MB)
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            if i % 15 == 0:
                result.append('FizzBuzz')
            elif i % 3 == 0:
                result.append('Fizz')
            elif i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))
        return result
