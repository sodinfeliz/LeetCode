"""
Question Link: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
Difficulty: Easy
Related Topics: Array, String, Simulation
Solved by 10.07.2021
Runtime: 44(ms), Memory Usage: 14.4(MB)
"""

# Runtime: 44(ms)(97.09%), Memory Usage: 14.4(MB)(16.43%)
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for op in operations:
            if op[0] == '+' or op[-1] == '+':
                result += 1
            else:
                result -= 1
        return result
