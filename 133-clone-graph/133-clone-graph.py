"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        
        visited = dict()
        
        def dfs(n):
            if n in visited:
                return visited[n]
            
            nodecopy = Node(n.val)
            children = []
            visited[n] = nodecopy
            
            for c in n.neighbors:
                children.append(dfs(c))
            nodecopy.neighbors = children.copy()
            return nodecopy
            
        if not node:
            return node
        return dfs(node)
            
        
            