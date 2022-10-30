
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        totalTime = 0 
        graph = defaultdict(list)
        
        def constructGraph(node):
            if not node:
                return 
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            constructGraph(node.left)
            constructGraph(node.right)
        
        def dfs(node, time, visited):
            nonlocal totalTime
            if node in visited:
                return time 
            totalTime = max(totalTime, time+1)
            visited.add(node)
            
            for neighbor in graph[node]:
                dfs(neighbor, time+1, visited)
            return time
        
        constructGraph(root)
        dfs(start, -1, set())
        return totalTime
                
        