# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        stack = []


        def dfs(node, path, runningSum, target):
            if not node:
                return 
            path.append(node.val)   
            if not node.left and not node.right and runningSum+node.val == target:
                ans.append(path.copy())

            dfs(node.left, path, runningSum+node.val, target)
            dfs(node.right, path, runningSum+node.val, target)

            path.pop()
            return 

        dfs(root, stack, 0, targetSum)
        return ans 