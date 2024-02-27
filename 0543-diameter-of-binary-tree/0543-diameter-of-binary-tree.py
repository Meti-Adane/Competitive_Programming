# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def recurse(node):
            if not node: return (0, 0) 
            leftPath, leftDiameter = recurse(node.left)
            rightPath, rightDiameter = recurse(node.right)

            return 1 + max(rightPath, leftPath), max(leftDiameter, rightDiameter, rightPath+leftPath+1)
        
        return recurse(root)[1] - 1
            
            