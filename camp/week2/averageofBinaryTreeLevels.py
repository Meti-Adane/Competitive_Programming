# question url : https://leetcode.com/problems/average-of-levels-in-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        bfsQ = deque()
        bfsQ.append(root)
        averages = []
        while bfsQ:
            levelsums = 0
            n = len(bfsQ)
            for i in range(len(bfsQ)):

                temp = bfsQ.popleft()
                levelsums += temp.val

                if temp.left:
                    bfsQ.append(temp.left)
                if temp.right:
                    bfsQ.append(temp.right)

            averages.append(levelsums / n)
        return averages
