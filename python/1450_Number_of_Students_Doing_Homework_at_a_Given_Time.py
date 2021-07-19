"""
Question Link: https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
Difficulty: Easy
Related Topics: Array
Solved by 07.27.2020 
Runtime: 40(ms), Memory Usage: 14(MB)
"""

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum([start <= queryTime <= end for start, end in zip(startTime, endTime)])
