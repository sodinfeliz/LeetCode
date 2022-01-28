"""
Question Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
Difficulty: Easy
Related Topics: Stack, DFS, Binary Tree
Solved by 01.27.2022
Runtime: 57(ms), Memory Usage: 13.9(MB)
"""

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        visited = []
        stack = [root]
        
        while stack:
            n = stack.pop()
            if isinstance(n, TreeNode):
                if n.right is not None:
                    stack.append(n.right)
                stack.append(n.val)
                if n.left is not None:
                    stack.append(n.left)
            else:
                visited.append(n)
                
        return visited