# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = None
        
        def dfs(node, stack):
            nonlocal ans
            if not node:
                return 
            stack.append(chr(node.val+97))
            if not node.left and not node.right:
                word = "".join(stack[::-1])
                ans = word if not ans else min(ans, word) 
                
            dfs(node.left, stack)
            dfs(node.right, stack)
            stack.pop()
        dfs(root, [])
        
        return ans