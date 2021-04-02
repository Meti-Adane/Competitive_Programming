# question url: https://leetcode.com/problems/path-sum/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.pathfinder(root, 0, targetSum, False)

    def pathfinder(self, root, sums, target, isFound):
        temp = root
        if not temp:
            return isFound

        sums += temp.val
        if not temp.right and not temp.left and sums == target:
            isFound = True
        isFound = self.pathfinder(temp.left, sums, target, isFound)
        isFound = self.pathfinder(temp.right, sums, target, isFound)

        return isFound