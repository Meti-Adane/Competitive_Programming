# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        
        def finder(node):
            if not node:
                return node
            
            if p.val > node.val and q.val > node.val:
                return finder(node.right)
            if p.val < node.val and q.val < node.val:
                return finder(node.left)
            return node
        
        
        return finder(root)