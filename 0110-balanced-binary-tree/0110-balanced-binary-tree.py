# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            leftSubTree = dfs(node.left)
            rightSubTree = dfs(node.right)
            
            if abs(leftSubTree - rightSubTree) > 1:
                return float('inf')
            return max(leftSubTree, rightSubTree) + 1
        return dfs(root) < float('inf')
            