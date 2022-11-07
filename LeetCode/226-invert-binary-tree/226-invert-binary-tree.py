# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invert(self, node):
        if node == None or node.left == None and node.right == None:
            return node
        temp = node.left
        node.left = node.right
        node.right = temp
        self.invert(node.left)
        self.invert(node.right)
        return node
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invert(root)