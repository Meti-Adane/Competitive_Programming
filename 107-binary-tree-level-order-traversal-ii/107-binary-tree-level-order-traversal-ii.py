# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = deque()
        ans = deque()

        if root:
            que.append(root)

        while que:
            level = []
            for _ in range(len(que)):
                temp = que.popleft()
                level.append(temp.val)
                if temp.left:
                    que.append(temp.left)
                if temp.right:
                    que.append(temp.right)
            ans.appendleft(level.copy())  
        return ans