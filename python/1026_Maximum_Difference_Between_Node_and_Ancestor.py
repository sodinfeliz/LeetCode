"""
Question Link: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
Difficulty: Medium
Related Topics: DFS, Tree
Solved by 11.10.2020 
Runtime: 32(ms), Memory Usage: 19.3(MB)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.maxDiff = 0
        self.helper(root, root.val, root.val)
        return self.maxDiff
    
    def helper(self, node, curMax, curMin):
        if node is None: return
        curDiff = max(abs(curMax-node.val), abs(curMin-node.val))
        self.maxDiff = max(self.maxDiff, curDiff)
        
        curMax = max(curMax, node.val)
        curMin = min(curMin, node.val)
        self.helper(node.left, curMax, curMin)
        self.helper(node.right, curMax, curMin)
