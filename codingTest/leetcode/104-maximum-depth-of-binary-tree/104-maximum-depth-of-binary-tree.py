# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, depth):
        if node:
            self.dfs(node.left, depth+1)
            self.dfs(node.right, depth+1)
        if depth > self.max_depth:
            self.max_depth = depth
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        self.dfs(root, 0)
        return self.max_depth
    
            