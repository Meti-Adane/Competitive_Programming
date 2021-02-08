# question url :https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        temp = root
        if not temp:
            return None
        temp.left, temp.right = self.invertTree(temp.right), self.invertTree(temp.left)

        return temp