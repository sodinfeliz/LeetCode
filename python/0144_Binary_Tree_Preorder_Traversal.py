"""
Question Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
Difficulty: Easy
Related Topics: Stack, DFS, Binary Tree
Solved by 01.27.2022
Runtime: 28(ms), Memory Usage: 14.1(MB)
"""

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        visited = []
        stack = [root]
        
        while len(stack):
            node = stack.pop()
            visited.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        
        return visited
