"""
Question Link: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/
Difficulty: Easy
Related Topics: Array
Solved by 07.20.2020 
Runtime: 92(ms), Memory Usage: 14.2(MB)
"""

# Runtime: 92(ms), Memory Usage: 14.2(MB)
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        result = {}
        for i in target:
            result[i] = result.get(i, 0) + 1
        for i in arr:
            if i not in result:
                return False
            elif result[i] - 1 < 0:
                return False
            else:
                result[i] -= 1
        return True
