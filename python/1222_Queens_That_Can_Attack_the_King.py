"""
Question Link: https://leetcode.com/problems/queens-that-can-attack-the-king/
Difficulty: Medium
Related Topics: Array
Solved by 10.27.2020
Runtime: 36(ms), Memory Usage: 14.1(MB)
"""

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        def in_border(pos):
            return 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7

        attack_queen = []
        directions = [[0,1],[1,0],[1,1],[1,-1],
                      [0,-1],[-1,0],[-1,-1],[-1,1]]
        for d in directions:
            step = 1
            while True:
                next_pos = [king[0]+step*d[0], king[1]+step*d[1]]
                if not in_border(next_pos): break
                if next_pos in queens:
                    attack_queen.append(next_pos)
                    break
                step += 1

        return attack_queen
