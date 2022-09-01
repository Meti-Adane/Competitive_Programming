# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque()
        count = 0
        queue.append((root,  float('-inf')))
        while queue:
            
            for _ in range(len(queue)):
                temp, maxi = queue.popleft()
                if temp.val >= maxi:
                    count += 1
                    
                if temp.left:
                    queue.append((temp.left, max(maxi, temp.val)))
                if temp.right:
                    queue.append((temp.right, max(maxi, temp.val)))
                    
        return count 
        
        
       