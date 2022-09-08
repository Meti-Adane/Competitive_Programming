# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        
        def lca(node, target1, target2):
            if not node or node.val == target1.val or node.val == target2.val:
                return node
            if node.val > target1.val and node.val > target2.val:
                return lca(node.left, target1, target2)
            if node.val < target1.val and node.val < target2.val:
                return lca(node.right, target1, target2)
            return node
        
        return lca(root, p, q)