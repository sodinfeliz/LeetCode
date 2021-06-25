"""
Question Link: https://leetcode.com/problems/check-if-it-is-a-straight-line/
Difficulty: Easy
Related Topics: Math
Solved by 10.27.2020
Runtime: 64(ms), Memory Usage: 14.4(MB)
"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2: return True
    
        p1, p2 = coordinates[:2]
        if p1[0] == p2[0]: # vertical line
            for (x, _) in coordinates[2:]:
                if x != p1[0]: return False
        else:
            m = (p2[1] - p1[1]) / (p2[0] - p1[0])
            for (x, y) in coordinates[2:]:
                if x == p1[0]: return False
                if (y - p1[1]) / (x - p1[0]) != m:
                    return False
        return True