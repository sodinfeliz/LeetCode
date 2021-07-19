"""
Question Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Difficulty: Easy
Related Topics: Array, Binary Search, Two Pointers
Solved by 10.15.2020 
Runtime: 56(ms), Memory Usage: 15.4(MB)
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        remain = []
        for i, num in enumerate(numbers):
            if num < target - num:
                remain.append((i, target - num))
            elif num == target - num:
                if numbers[i+1] == num:
                    return [i+1, i+2]
            else:
                while remain[-1][-1] < num:
                    del remain[-1]
                idx, r = remain[-1]
                if r == num:
                    return [idx+1, i+1]
