"""
Question Link: https://leetcode.com/problems/robot-return-to-origin/
Difficulty: Easy
Related Topics: String
Solved by 11.04.2020 
Runtime: 64(ms), Memory Usage: 14.1(MB)
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        direction = {'U': 1, 'D': -1, 'L': -1, 'R': 1}
        pos = [0, 0]
        for step in moves:
            if step in ['U', 'D']:
                pos[1] += direction[step]
            else:
                pos[0] += direction[step]
        return pos[0] == 0 and pos[1] == 0
