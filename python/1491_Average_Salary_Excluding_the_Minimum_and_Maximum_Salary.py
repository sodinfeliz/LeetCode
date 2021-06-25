"""
Question Link: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
Difficulty: Easy
Related Topics: Array, Sort
Solved by 07.27.2020 
Runtime: 28(ms), Memory Usage: 13.9(MB)
"""
from typing import List

# time complexity: O(nlogn), Space Complexity: O(1)
class Solution:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary)[1:-1]
        return sum(salary) / len(salary)