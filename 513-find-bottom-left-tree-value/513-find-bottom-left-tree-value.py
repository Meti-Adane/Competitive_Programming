# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        que = deque()
        que.append(root)
        ans = root.val
        
        while que:
            ans = que[0].val
            for _ in range(len(que)):
                temp = que.popleft()
                if temp.left:
                    que.append(temp.left)
                if temp.right:
                    que.append(temp.right)
            
        return ans