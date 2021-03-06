# question url: https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        l = self.traverseInOrder(root, k, [])
        return l[k - 1]

    def traverseInOrder(self, TreeNode, k, smallValuesContainer):
        temp = TreeNode
        if temp and len(smallValuesContainer) <= k:
            self.traverseInOrder(temp.left, k, smallValuesContainer)
            smallValuesContainer.append(temp.val)
            self.traverseInOrder(temp.right, k, smallValuesContainer)
        return smallValuesContainer
