# question ur: https://leetcode.com/problems/minimum-depth-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:

        queue = deque([root])
        if not root:
            return 0
        level = 1

        while queue:
            for i in range(len(queue)):
                temp = queue.popleft()
                if not temp.left and not temp.right:
                    return level
                else:
                    if temp.left:
                        queue.append(temp.left)
                    if temp.right:
                        queue.append(temp.right)
            level += 1





