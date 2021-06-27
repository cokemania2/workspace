// https://leetcode.com/problems/binary-tree-pruning/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root == None :
            return None
        else :
            root.left = self.pruneTree(root.left)
            root.right = self.prunTree(root.right)
        if root.val == 1 and root.left == None and root.right == None :
            return None
        return root
