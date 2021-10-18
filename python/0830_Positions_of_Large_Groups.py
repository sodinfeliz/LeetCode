"""
Question Link: https://leetcode.com/problems/positions-of-large-groups/
Difficulty: Easy
Related Topics: String
Solved by 10.04.2021 
Runtime: 36(ms), Memory Usage: 14.4(MB)
"""

# Runtime: 36(ms)(85.12%), Memory Usage: 14.4(MB)(29.75%)
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        start, end = 0, 0
        c, result = '', []
        s += ' '
        
        for i, ch in enumerate(s):
            if ch == c:
                end = i
            else:
                if end - start >= 2:
                    result.append([start, end])
                c, start, end = ch, i, i
        
        return result
