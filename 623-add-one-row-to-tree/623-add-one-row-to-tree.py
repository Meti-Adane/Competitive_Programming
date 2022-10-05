# 6:55 Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        que = deque([(root, 1)])
        
        if depth == 1:
            return TreeNode(val, root, None)
        isFound = False
        while que:
            for _ in range(len(que)):
                node, height = que.popleft()
                if height == depth-1:
                    prevleft, prevright = node.left, node.right
                    newleftnode = TreeNode(val, prevleft, None)
                    newrightnode = TreeNode(val, None, prevright)
                    node.left = newleftnode
                    node.right = newrightnode
                    isFound = True 
                if not isFound and node.left:
                    que.append((node.left, height+1))
                if not isFound and node.right:
                    que.append((node.right, height+1))
            if isFound:
                break
        return root 