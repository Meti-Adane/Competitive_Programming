class Solution:
    def maxDepth(self, node: Optional[TreeNode]) -> int:
        return 0 if not node else max(self.maxDepth(node.left) + 1, self.maxDepth(node.right) + 1)