# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        que = deque()
        ans = []
        if not root:
            return ans
        que.append(([root.val], root.val, root))
        
        while que:
            for _ in range(len(que)):
                path, runningSum, temp = que.popleft()
                if not temp.left and not temp.right and runningSum == targetSum:
                    ans.append(path.copy())
                    continue 
                if temp.left:
                    path.append(temp.left.val)
                    que.append((path.copy(), runningSum+temp.left.val, temp.left))
                    path.pop()
                if temp.right:
                    path.append(temp.right.val)
                    que.append((path.copy(), runningSum+temp.right.val, temp.right))
                    path.pop()
        return ans 
                    
                    
                


        