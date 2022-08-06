# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(i, j):
            if i > j:
                return None
            
            mid = i + (j-i) // 2
            node = TreeNode(nums[mid])
          
            node.left = construct(i, mid-1)
            node.right = construct(mid+1, j)
            return node
        
        return construct(0, len(nums)-1)