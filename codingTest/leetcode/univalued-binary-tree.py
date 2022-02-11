# https://leetcode.com/problems/univalued-binary-tree/submissions/
# univalued-binary-tree/submissions.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, v):
            if node == None:
                return True
            elif v == node.val:
                return dfs(node.left, v) and dfs(node.right, v)
            return False
            
        return dfs(root, root.val)