# 5:05 Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        ans = []
        
        def dfs(node, ans):
            if not node:
                return ans
            ans.append("(")
            ans.append(str(node.val))
            if not node.left and node.right:
                ans.append("()")
                dfs(node.right, ans)
            else:
                dfs(node.left, ans)
                dfs(node.right, ans)
            ans.append(")")
            return ans 
        dfs(root, ans)
        ans[0] = ""
        ans.pop()
        return "".join(ans)
        
        