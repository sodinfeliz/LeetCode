"""
Question Link: https://leetcode.com/problems/minimum-height-trees/
Difficulty: Medium
Related Topics: Graph, BFS
Solved by 11.05.2020 
Runtime: 380(ms), Memory Usage: 18.3(MB)
"""

from queue import Queue

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        self.n = n # nodes #
        self.adj = dict((i, []) for i in range(n))
        self.deg = [0]*n
        
        for v, w in edges:
            self.add_edge(v, w)
            
        self.find_leaf()
        self.rootForMinimumHeight()
        
        return self.root
        
    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.deg[v] += 1
        self.deg[w] += 1
        
    def find_leaf(self):
        self.q = Queue()
        for i, deg in enumerate(self.deg):
            if deg == 1:
                self.q.put(i)
                
    def rootForMinimumHeight(self):
        N = self.n
        
        while N > 2:
            leaf_num = self.q.qsize()
            N -= leaf_num
            
            for _ in range(leaf_num):
                lNode = self.q.get()
                for adjNode in self.adj[lNode]:
                    self.deg[adjNode] -= 1
                    if self.deg[adjNode] == 1:
                        self.q.put(adjNode)
        
        self.root = list(self.q.get() for _ in range(self.q.qsize()))
