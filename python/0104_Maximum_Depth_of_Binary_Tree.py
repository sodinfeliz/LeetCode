"""
Question Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Difficulty: Easy
Related Topics: DFS, BFS, Binary Tree
Solved by 01.27.2022
"""

# Runtime: 44(ms), Memory Usage: 15.8(MB)
# Iterative: BFS + Queue
from queue import SimpleQueue

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        max_depth = 0
        q = SimpleQueue()
        q.put([root, 1])
        
        while not q.empty():
            sz = q.qsize()
            for _ in range(sz):
                node, depth = q.get()
                if depth > max_depth:
                    max_depth = depth
                if node.left is not None:
                    q.put([node.left, depth + 1])
                if node.right is not None:
                    q.put([node.right, depth + 1])
                    
        return max_depth

# Runtime: 44(ms), Memory Usage: 16.3(MB)
# Recursive: DFS + Bottom-top Approach
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
