"""
Question Link: https://leetcode.com/problems/number-of-islands/
Difficulty: Medium
Related Topics: DFS, BFS, Union Find
Solved by 08.07.2020 
Runtime: 736(ms), Memory Usage: 18.6(MB)
"""

# Code mostly similar to (695. Max Area of Island)
class Solution:
    def numIslands(self, grid) -> int:
        seen = set()
        num_land = 0
        for ri, row in enumerate(grid):
            for ci, elem in enumerate(row):
                elem = eval(elem)
                if elem and (ri, ci) not in seen:
                    num_land += 1
                    seen.add((ri, ci))
                    stack = [(ri, ci)]
                    while stack:
                        r, c = stack.pop()
                        for nr, nc in ((r-1, c), (r+1, c), (r, c+1), (r, c-1)):
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and \
                               eval(grid[nr][nc]) and (nr, nc) not in seen:
                                stack.append((nr, nc))
                                seen.add((nr, nc))

        return num_land