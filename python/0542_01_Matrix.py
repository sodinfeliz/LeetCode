"""
Question Link: https://leetcode.com/problems/01-matrix/
Difficulty: Medium
Related Topics: Array, DP, DFS
Solved by 07.30.2021
Runtime: 716(ms), Memory Usage: 17.1(MB)
"""
from collections import deque

# Runtime: 716(ms)(58.14%), Memory Usage: 17.1(MB)(65.64%)
# Time complexity: O(mn), Space Complexity: O()
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dist = [[float('inf')]*n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append([i, j])
            
        dirc = [[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            coord = q.popleft()
            for sx, sy in dirc:
                x = coord[0] + sx
                y = coord[1] + sy
                if 0 <= x < m and 0 <= y < n and dist[x][y] > dist[coord[0]][coord[1]] + 1:
                    dist[x][y] = dist[coord[0]][coord[1]] + 1
                    q.append([x,y])
                
        return dist
