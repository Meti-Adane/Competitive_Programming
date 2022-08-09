# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indexMapper = dict()
        
        for pos, val in enumerate(inorder):
            indexMapper[val] = pos
        
        def construct(i, j, arr):
            if not arr:
                return 
            
            nodeValue = arr.pop() #3
            index = indexMapper[nodeValue] #1
            
            leftCount = index - i #1
            rightCount = len(arr) - (j - index-1) #
            
            node = TreeNode(nodeValue)
            node.left = construct(i, index, arr[:leftCount]) #
            node.right = construct(index+1, j, arr[rightCount:]) #
            
            return node
        
        return construct(0, len(inorder), postorder)