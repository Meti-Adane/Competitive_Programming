# questionurl : https://leetcode.com/problems/range-sum-of-bst/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        return self.traverseTree(root, low, high, [0])

    def traverseTree(self, temp, low, high, sums):
        if not temp: return 0

        if temp and temp.val <= high and temp.val >= low:
            sums[0] += temp.val

        self.traverseTree(temp.left, low, high, sums)
        self.traverseTree(temp.right, low, high, sums)

        return sums[0]