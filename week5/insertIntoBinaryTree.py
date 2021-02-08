# question url :https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        temp = root
        if not temp:
            return TreeNode(val)
        if val > temp.val:
                temp.right = self.insertIntoBST(temp.right, val)
        elif val < temp.val:
                temp.left = self.insertIntoBST(temp.left, val)
        return temp