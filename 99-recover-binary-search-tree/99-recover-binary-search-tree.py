# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def inorder(node, arr):
            if not node:
                return 
            inorder(node.left, arr)
            arr.append(node)
            inorder(node.right, arr)
            
        inorderTraversal = []
        x, y = None, None
        inorder(root, inorderTraversal)
        sortedArr = sorted(inorderTraversal, key=lambda x:x.val)
        
        for i in range(len(inorderTraversal)):
            if sortedArr[i].val != inorderTraversal[i].val:
                if not x: x = inorderTraversal[i]
                elif not y: y = inorderTraversal[i]
            if x and y:
                break 
        x.val, y.val = y.val, x.val
                
        
        
        
        