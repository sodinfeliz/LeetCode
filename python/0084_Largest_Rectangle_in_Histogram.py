"""
Question Link: https://leetcode.com/problems/largest-rectangle-in-histogram/
Difficulty: Hard
Related Topics: Array, Stack
Solved by 09.06.2021 
Runtime: 808(ms), Memory Usage: 27.9(MB)
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ret, mono_stack = 0, []
        heights.append(0)
        for i, h in enumerate(heights):
            while mono_stack and heights[mono_stack[-1]] > h:
                height = heights[mono_stack.pop()]
                if mono_stack:
                    length = i - mono_stack[-1] - 1
                else:
                    length = i
                ret = max(ret, height*length)
            mono_stack.append(i)
        return ret