"""
Question Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
Difficulty: Easy
Related Topics: Stack, DFS, Binary Tree
Solved by 01.27.2022
Runtime: 32(ms), Memory Usage: 14.1(MB)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        visited = []
        stack = [root]
        
        while stack:
            n = stack.pop()
            if isinstance(n, TreeNode):
                stack.append(n.val)
                if n.right is not None:
                    stack.append(n.right)
                if n.left is not None:
                    stack.append(n.left)
            else:
                visited.append(n)
        
        return visited
