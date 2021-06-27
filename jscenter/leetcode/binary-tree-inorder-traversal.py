# binary-tree-inorder-traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        answer = []
        if root == None :
            return None
        else :
            left = self.inorderTraversal(root.left)
            if left != None :
                answer += left
            answer.append(root.val)                
            right = self.inorderTraversal(root.right)
            if right != None :
                answer += right
        return answer
            