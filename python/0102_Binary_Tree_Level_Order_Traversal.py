"""
Question Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
Difficulty: Medium
Related Topics: BFS, Binary Tree
Solved by 01.27.2022
Runtime: 96(ms), Memory Usage: 14.3(MB)
"""

from queue import SimpleQueue

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        order = []
        q = SimpleQueue()
        q.put(root)
        
        while not q.empty():
            sz = q.qsize()
            visited = []
            for _ in range(sz):
                node = q.get()
                visited.append(node.val)
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
            order.append(visited)
            
        return order
