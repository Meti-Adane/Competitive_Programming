# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        columns = dict()
        indicies = [0, 0]
        self.dfs(root, 0, 0, columns, indicies)
        ans = []
        
        for i in range(indicies[0], indicies[1]+1):
            if i not in columns:
                continue
            columns[i].sort()
            arr = [x[1] for x in columns[i]]
            ans.append(arr)
        return ans
            
                
        
        
        
    def dfs(self, node, row, col, columns, indicies):
        if not node:
            return 0
        indicies[0] = min(indicies[0], col)
        indicies[1] = max(indicies[1], col)
        if col not in columns:
            columns[col] = []
        columns[col].append((row, node.val))
        self.dfs(node.left, row+1, col-1, columns, indicies)
        self.dfs(node.right, row+1, col+1, columns, indicies)