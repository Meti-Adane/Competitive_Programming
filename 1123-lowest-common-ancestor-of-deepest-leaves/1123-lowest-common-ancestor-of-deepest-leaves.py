# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        heights = defaultdict(int)
        
        def getdepth(node, h):
            if not node:
                return 0
            heights[node] = max(getdepth(node.left, h+1), getdepth(node.right, h+1)) + 1
            return heights[node] 
        
                
        def lca(node):
            left = heights[node.left]
            right = heights[node.right]
            
            if left == right:
                return node
            if left > right:
                return lca(node.left)
            return lca(node.right)
        
        getdepth(root, 0)
        return lca(root)
            
            
            
            
            
        