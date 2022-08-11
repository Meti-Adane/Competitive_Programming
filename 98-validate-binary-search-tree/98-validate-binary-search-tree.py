# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('inf'), float('-inf'))
        
    def dfs(self, node, low, high):
        if not node:
            return True
        
        if node.val >= low or node.val <= high:
            return False
        
        return self.dfs(node.left, node.val, high) and self.dfs(node.right, low, node.val)
    
    
    