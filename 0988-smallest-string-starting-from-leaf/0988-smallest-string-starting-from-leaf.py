# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        words = []
        
        def dfs(node, stack):
            nonlocal words
            if not node:
                return 
            if not node.left and not node.right:
                words.append("".join([chr(node.val+97)]+stack[::-1]))
                return 
            stack.append(chr(node.val+97))
            dfs(node.left, stack)
            dfs(node.right, stack)
            stack.pop()
        dfs(root, [])
        
        return sorted(words)[0]