"""
Question Link: https://leetcode.com/problems/island-perimeter/
Difficulty: Easy
Related Topics: Hash Table
Solved by 08.07.2020 
Runtime: 640(ms), Memory Usage: 15(MB)
"""

# Breadth First Search
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def bfs(r0, c0):
            seen = set()
            num_edge = 0
            stack = [(r0, c0)]
            seen.add((r0, c0))
            while stack:
                r, c = stack.pop()
                for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                    if (nr, nc) in seen:
                        continue
                    elif not 0 <= nr < len(grid) or not 0 <= nc < len(grid[0]) or not grid[nr][nc]:
                        num_edge += 1
                        continue
                    else:
                        stack.append((nr, nc))
                        seen.add((nr, nc))
            return num_edge

        for ri, row in enumerate(grid):
            for ci, elem in enumerate(row):
                if elem: return bfs(ri, ci)
