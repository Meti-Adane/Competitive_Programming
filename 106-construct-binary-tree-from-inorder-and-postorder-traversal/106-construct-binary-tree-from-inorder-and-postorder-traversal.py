# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mapper = dict()
        
        for pos, val in enumerate(inorder):
            mapper[val] = pos
        return self.construct(0, len(inorder), postorder, mapper)
    
    def construct(self, i, j, postorder, mapper):
        if not len(postorder):
            return 
        arr = postorder.copy()
        nodeValue = arr.pop()
        node = TreeNode(nodeValue)
        index = mapper[nodeValue]

        leftsideCount = index-i
        rightsideCount = len(arr) - (j-index-1)
        node.left = self.construct(i, index, arr[:leftsideCount], mapper)
        node.right = self.construct(index+1, j, arr[rightsideCount:], mapper)
        
        return node
    
    
        
        