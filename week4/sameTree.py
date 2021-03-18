# question url : https://leetcode.com/problems/same-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        bfsQ1 = deque()
        bfsQ2 = deque()
        bfsQ1.append(p)
        bfsQ2.append(q)

        if not p or not q:
            return not p and not q
        while bfsQ1 and bfsQ2:
            temp1 = bfsQ1.popleft()
            temp2 = bfsQ2.popleft()

            if temp1.val != temp2.val:
                return False

            if temp1.left and temp2.left:
                bfsQ1.append(temp1.left)
                bfsQ2.append(temp2.left)

            if temp1.right and temp2.right:
                bfsQ1.append(temp1.right)
                bfsQ2.append(temp2.right)

            if temp1.left and not temp2.left:
                return False
            if temp1.right and not temp2.right:
                return False
            if not temp1.left and temp2.left:
                return False
            if not temp1.right and temp2.right:
                return False

        return True