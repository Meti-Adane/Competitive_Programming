# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        levels = dict()
        ans = []
        
        
        def assignLevel(node, level, hashmap):
            if not node:
                return 
            hashmap[node.val] = level
            assignLevel(node.left, level+1, hashmap)
            assignLevel(node.right, level+1, hashmap)
            
    
        def findPath(node, target, direction, path, ans):
            if not node:
                return 
            path.append(direction)
            if node.val == target:
                ans.extend(path.copy())
                return 
            findPath(node.left, target, "L", path, ans)
            findPath(node.right, target, 'R', path, ans)
            path.pop()
        
        
        def findLCA(node, start, end, ):
            if not node:
                return 
            
            if node.val == start or node.val == end:
                return node
            
            leftsubtree = findLCA(node.left, start, end)
            rightsubtree = findLCA(node.right, start, end)
            
            if leftsubtree and rightsubtree:
                return node
            if leftsubtree and not rightsubtree:
                return leftsubtree
            return rightsubtree
        
        assignLevel(root, 0, levels)
        lca = findLCA(root, startValue, destValue)
        i = levels[startValue]
        while i > levels[lca.val]:
            ans.append("U")
            i -= 1
        findPath(lca, destValue, "", [], ans)
        return "".join(ans)