# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = defaultdict(int)
        
        def dfs(node):
            if not node or node in dp :
                return dp[node]
            
            option1 = node.val 
            if node.left:
                option1 += dfs(node.left.left ) + dfs(node.left.right ) 
            if node.right:
                option1 += dfs(node.right.left) + dfs(node.right.right)
            
            option2 = dfs(node.left) + dfs(node.right)
            dp[node] = max(option1, option2)
            
            return dp[node] 
        
       
        return dfs(root)