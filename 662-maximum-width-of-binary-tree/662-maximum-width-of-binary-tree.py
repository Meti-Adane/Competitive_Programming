#9:17
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
       
       
        que = deque()
        ans = 0 
        que.append((root, 1))
        
        while que:
            levelWidth = que[-1][1] - que[0][1]
            ans = max(levelWidth, ans)
            
            for _ in range(len(que)):
                temp, idx = que.popleft()
                if temp.left:
                    que.append((temp.left, idx*2))
                if temp.right:
                    que.append((temp.right, idx*2+1))
        return ans+1
                
                
        