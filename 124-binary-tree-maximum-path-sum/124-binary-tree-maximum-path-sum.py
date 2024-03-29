# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')
        def dfs(node):
            if not node:
                return 0
            leftSum = max(dfs(node.left), 0)
            rightSum = max(dfs(node.right), 0)
            
            path = max(node.val, leftSum + rightSum + node.val)
            
            self.ans = max(path, self.ans)
            return max(leftSum, rightSum) + node.val
        
        dfs(root)
        return self.ans
        
        