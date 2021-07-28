"""
Question Link: https://leetcode.com/problems/day-of-the-week/
Difficulty: Easy
Related Topics: Math
Solved by 07.27.2021
Runtime: 32(ms), Memory Usage: 14.4(MB)
"""

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = 0
        for y in range(1971, year):
            if y % 4 == 0: # leap year
                days += 366
            else: 
                days += 365
                
        days += sum(days_of_month[:month-1]) + day
        if month > 2 and year % 4 == 0 and year != 2100:
            days += 1
        
        return weekday[(4+days%7)%7]
