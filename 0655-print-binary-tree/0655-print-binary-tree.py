# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        level = self.getHeight(root)
        n, m = level, (2 ** level) -1 #number of rows, number of cols
        ans = [["" for _ in range(m)] for _ in range(n)]
        que = deque([(root, 0, 0, m)])
        
        while que:
            node, row, colmin, colmax = que.popleft()
            mid = (colmin+colmax)//2
            ans[row][mid] = str(node.val)
            if node.left:
                que.append((node.left, row+1, colmin, mid-1))
            if node.right:
                que.append((node.right, row+1, mid+1, colmax))
        return ans
    
    def getHeight(self, node):
            return 0  if not node else max(self.getHeight(node.left), self.getHeight(node.right))+1