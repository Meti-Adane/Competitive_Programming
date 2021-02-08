# question url: https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return self.helper(root, [])

    def helper(self, root, nodes=[]):
        temp = root
        if temp:
            self.helper(temp.left, nodes)
            self.helper(temp.right, nodes)
            nodes.append(temp.val)
        return (nodes)