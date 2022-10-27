# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        valid_depths = set()
        ans = 0 
        
        def dfs(node, depth):
            nonlocal ans 
            if not node:
                return 
            if depth in valid_depths:
                ans += node.val
            if node.val %2 == 0:
                valid_depths.add(depth+2)
                
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
            valid_depths.discard(depth+2)
            
        dfs(root, 0)
        return ans 
            
                                