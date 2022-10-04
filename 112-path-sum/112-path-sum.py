# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(node, target, runningSum):
            if not node:
                return False
            if not node.left and not node.right: 
                return runningSum+node.val == target
            return helper(node.left, target, runningSum+node.val) or helper(node.right, target, runningSum+node.val)
        
        return helper(root, targetSum, 0)