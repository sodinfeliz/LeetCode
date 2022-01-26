"""
Question Link: https://leetcode.com/problems/open-the-lock/
Difficulty: Medium
Related Topics: Array, Hash Table, BFS, String
Solved by 01.18.2021
Runtime: 9490(ms), Memory Usage: 15.4(MB)
"""
from typing import List
from queue import SimpleQueue

class Solution:
    
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0
        elif '0000' in deadends:
            return -1
        
        self.deadends = deadends
        self.target = target
        self.visited = {'0000': None}
        self.min_depth = float("inf")
        self.bfs([0, 0, 0, 0])
        
        return -1 if self.min_depth == float("inf") else self.min_depth
        
    def bfs(self, node: List[int]):
        
        def rotate_wheel(node: List[int], depth: int, pos: int, incre: int):
            assert incre in [1, -1]
            new_node = node.copy()
            new_node[pos] = (node[pos] + incre) % 10
            
            new_node_str = ''.join(map(str, new_node))
            if new_node_str == self.target:
                self.min_depth = min(self.min_depth, depth + 1)
                self.visited[new_node_str] = None
            elif new_node_str not in self.deadends and \
                 new_node_str not in self.visited:
                q.put([new_node, depth + 1])
                self.visited[new_node_str] = None
                        
        q = SimpleQueue()
        q.put([node, 0])
        
        while not q.empty():
            node, depth = q.get()
            
            rotate_wheel(node, depth, 0, 1)
            rotate_wheel(node, depth, 0, -1)
            rotate_wheel(node, depth, 1, 1)
            rotate_wheel(node, depth, 1, -1)
            rotate_wheel(node, depth, 2, 1)
            rotate_wheel(node, depth, 2, -1)
            rotate_wheel(node, depth, 3, 1)
            rotate_wheel(node, depth, 3, -1)
            
            if self.min_depth == depth + 1: break


# Reference Code
# Runtime: 668(ms)(63.77%), Memory Usage: 15.9(MB)(17.25%)
from collections import deque
class Solution:
    def openLock(self, deadends, target):
        depth = -1
        visited, q = set(deadends), deque(['0000'])

        while q:
            size = len(q)
            depth += 1
            for _ in range(size):
                node = q.popleft()
                if node == target: return depth
                if node in visited: continue
                visited.add(node)
                q.extend(self.successors(node))
        return -1

    def successors(self, src):
        res = []
        for i, ch in enumerate(src):
            num = int(ch)
            res.append(src[:i] + str((num - 1) % 10) + src[i+1:])
            res.append(src[:i] + str((num + 1) % 10) + src[i+1:])
        return res
