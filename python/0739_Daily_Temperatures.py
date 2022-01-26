"""
Question Link: https://leetcode.com/problems/daily-temperatures/
Difficulty: Medium
Related Topics: Array, Stack
Solved by 01.26.2022
"""

# Runtime: 1903(ms)(18.20%), Memory Usage: 24.7(MB)(93.37%)
# Time complexity: O(n), Space Complexity: O(n)
# Monotonic Stack
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [[temperatures[-1], len(temperatures)-1]]
        result = [0]
        
        for i in range(len(temperatures)-2, -1, -1):
            while stack:
                if stack[-1][0] > temperatures[i]:
                    result.append(stack[-1][1] - i)
                    break
                else:
                    stack.pop()
            if not stack:
                result.append(0)
            stack.append([temperatures[i], i])
        
        return result[::-1]
