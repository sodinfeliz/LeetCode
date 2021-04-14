"""
Question Link: https://leetcode.com/problems/max-area-of-island/
Difficulty: Medium
Related Topics: Array, DFS
Solved by 08.06.2020 
Runtime: 236(ms), Memory Usage: 14.2(MB)
"""

# Reference by the solution
# Breadth First Search
# Time complexity: O(|V|+|E|), Space Complexity: O(?)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        max_area = 0
        for ri, row in enumerate(grid):
            for ci, elem in enumerate(row):
                if elem and elem not in seen:
                    area = 0
                    seen.add((ri, ci))
                    stack = [(ri, ci)]
                    while stack:
                        r, c = stack.pop()
                        area += 1
                        for nr, nc in ((r-1, c), (r+1, c), (r, c+1), (r, c-1)):
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and \
                               grid[nr][nc] and (nr, nc) not in seen:
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    max_area = max(max_area, area)
        return max_area
