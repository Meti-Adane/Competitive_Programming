# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        levelIndx = 0

        while queue:
            prevElement = 0 if levelIndx % 2 == 0 else float('inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                # If level is odd 
                if levelIndx % 2 == 1:
                    if node.val % 2 == 1 or node.val >= prevElement: return False

                # If level is even 
                else:
                    if node.val % 2 == 0 or node.val <= prevElement: return False 

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

                prevElement = node.val
            levelIndx += 1
        return True 