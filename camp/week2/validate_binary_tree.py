# questionurl : https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        inorderRes = self.inorder(root, [])
        return all(inorderRes[i] < inorderRes[i + 1] for i in range(len(inorderRes) - 1))

    def inorder(self, root, arr):
        temp = root
        if not temp:
            return temp

        self.inorder(temp.left, arr)
        arr.append(temp.val)
        self.inorder(temp.right, arr)
        return arr