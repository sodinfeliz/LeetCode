"""
Question Link: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
Difficulty: Easy
Related Topics: String
Solved by 11.04.2020 
Runtime: 28(ms), Memory Usage: 14.1(MB)
"""

class Solution:
    def reformatDate(self, date: str) -> str:
        mDict = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
             "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
             "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}

        day, month, year = date.split()
        return f'{year}-{mDict[month]}-{int(day[:-2]):02d}'
