from collections import deque

# question url : https://leetcode.com/problems/binary-tree-right-side-view/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        temp = root

        if not root:
            return []

        rights = [root.val]

        bfsQ = deque()
        bfsQ.append(root)

        while bfsQ:

            for i in range(len(bfsQ)):
                temp = bfsQ.popleft()

                if temp.left:
                    bfsQ.append(temp.left)
                if temp.right:
                    bfsQ.append(temp.right)

            if bfsQ:
                rights.append(bfsQ[-1].val)
        return rights