# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        seen = dict()
        ans = 0
        
        def dfs(node, uniqueCount):
            nonlocal ans
            if node:
                if node.val in seen and seen[node.val] % 2 == 1:
                    uniqueCount -= 1
                if node.val not in seen or seen[node.val] % 2 == 0:
                    uniqueCount += 1
                    seen[node.val] = 0
                if not node.left and not node.right:
                    if uniqueCount == 0 or uniqueCount == 1:
                        ans += 1
                    return ans

                seen[node.val] += 1
                dfs(node.left, uniqueCount)
                dfs(node.right, uniqueCount)
                seen[node.val] -= 1
            return ans
        
        return dfs(root, 0)
