class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        
        visited = set()
        result = set()
        
        for src,dest in edges:
            graph[src].add(dest)
            
        
        def dfs(src):
            visited.add(src)
            for dest in graph[src]:
                if dest not in visited:
                    dfs(dest)
                elif dest in result:
                    result.remove(dest)
                    
        
        for i in range(n):
            if i not in visited:
                result.add(i)
                dfs(i)
                
        return result