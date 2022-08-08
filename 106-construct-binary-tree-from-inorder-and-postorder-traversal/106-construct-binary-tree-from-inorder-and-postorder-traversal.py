# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def construct(inorder, postorder):
            if not inorder or not postorder:
                return None
            
            index = inorder.index(postorder.pop())
            node = TreeNode(inorder[index])
            
            node.left = construct(inorder[:index], postorder[:index])
            node.right = construct(inorder[index+1:], postorder[index:])
            return node
        
        return construct(inorder, postorder)