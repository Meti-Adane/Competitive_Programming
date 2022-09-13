# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        que = deque()
        que.append(root)
        
        
        while que:
            node1, node2 = None, None
            for _ in range(len(que)):
                temp = que.popleft()
                if not node1:
                    node1 = temp
                node2 = temp
                if temp.left:
                    que.append(temp.left)
                if temp.right:
                    que.append(temp.right)
                
        def lca(node, target1, target2):
            if not node or node.val == target1.val or node.val == target2.val:
                return node
            left = lca(node.left, target1, target2)
            right = lca(node.right, target1, target2)
            
            if left and right:
                return node
            if left and not right:
                return left
            return right
        
        return lca(root, node1, node2)
            
            
            
            
            
        