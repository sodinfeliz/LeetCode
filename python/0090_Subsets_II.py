"""
Question Link: https://leetcode.com/problems/subsets-ii/
Difficulty: Medium
Related Topics: Array, Backtracking, Bit Manipulation
Solved by 08.02.2021 
Runtime: 36(ms), Memory Usage: 14.6(MB)
"""

# Runtime: 36(ms)(77.97%), Memory Usage: 14.6(MB)(27.44%)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        for k, v in Counter(nums).items():
            if not result:
                result = [[k]*i for i in range(v+1)]
            else:
                _tmp = result.copy()
                for i in range(1, v+1):
                    result.extend([elem+[k]*i for elem in _tmp])
        return result

# Runtime: 32(ms)(92.15%), Memory Usage: 14.4(MB)(82.87%)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for k, v in Counter(nums).items():
            _tmp = result.copy()
            for i in range(1, v+1):
                result.extend([elem+[k]*i for elem in _tmp])
        return result
