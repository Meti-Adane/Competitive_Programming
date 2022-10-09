# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hashmap = set()
        
        def dfs(node, hashmap, target):
            if not node:
                return False
            if target - node.val in hashmap:
                return True
            hashmap.add(node.val)
            return dfs(node.left, hashmap, target) or dfs(node.right, hashmap, target)
        
        return dfs(root, hashmap, k)